import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.types import*


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']

def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    '''transforming data into reguired dataset:
    
        Arguments:
            spark {object}: connection session.
            input_data {string}: dataset path.
            output_data {string}: dataset path as an output of a transformed data.

        Returns:
            N/A
    
    '''
    
    
    song_data = input_data +"/song_data/*/*/*/*.json" #input_data +"song_data/*/*/*/*.json" to get data from s3   
    df = spark.read.json(song_data)

    songs_table = df.select("song_id","title","artist_id","year","duration").drop_duplicates()
    songs_table.write.partitionBy("year","artist_id").parquet(output_data+"/song")

    artists_table = df.select("artist_id","artist_name","artist_location","artist_latitude","artist_longitude").drop_duplicates()
    artists_table.write.parquet(output_data+"/artist")


def process_log_data(spark, input_data, output_data):
    
    '''transforming data into reguired dataset:
    
        Arguments:
            spark {object}: connection session to spark.
            input_data {string}: dataset path.
            output_data {string}: dataset path as an output of a transformed data.

        Returns:
            N/A
    '''
    
    log_data = input_data + "/*.json" #input_data + "log_data/*.json" to get data from s3
    df = spark.read.json(log_data)
    df = df.filter(df.page == 'NextSong')

    users_table = df.select("userId","firstName","lastName","gender","level").drop_duplicates()
    users_table.write.parquet(output_data+"/users")

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x/1000), TimestampType())
    df = df.withColumn('date_time', get_timestamp('ts'))
    time_table = df.select("date_time",
                           hour("date_time").alias('hour'),
                           dayofmonth("date_time").alias('day'),
                           weekofyear("date_time").alias('week'),
                           month("date_time").alias('month'),
                           year("date_time").alias('year'),
                           date_format("date_time","u").alias('weekday')).distinct()    
    
    time_table.write.partitionBy("year","month").parquet(output_data+"/time")

    # reading song data from paraquet file
    song_df = spark.read.parquet(output_data+"/song")
    
    songplays_table = df.join(song_df,  [(df.song == song_df.title) & (df.artist ==song_df.artist_id)]).select(
        df['date_time'].alias('date_time'),
        df['userId'].alias('userId'),
        df['level'].alias('level'),
        df['sessionId'].alias('sessionId'),
        df['location'].alias('location'),
        df['userAgent'].alias('userAgent'),
        song_df['song_id'].alias('song_id'),
        song_df['artist_id'].alias('artist_id')).drop_duplicates()
    songplays_table.withColumn("year",year("date_time")).withColumn("month",month("date_time")).write.partitionBy("year","month").parquet(output_data+"/songplays")


def main():
    
    '''create spark session and passing them as an arrgument with data path.
    
        Arguments:
            spark {object}: connection session.
            input_data {string}: dataset path.
            output_data {string}: dataset path as an output for the transformed data.
            
        Returns:
            N/A
    '''

    spark = create_spark_session()
    
    #using the data resind in a local file-data by runing the !unzip command in the terminal
    input_data = "data" #"s3a://udacity-dend/" in case we are using AWS 
    output_data = "output"
    
    #calling function to do data transformation
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
