# purpose of this project.

*Sparkify has grown data therefore, they have upgrade their infrastructure and use **cloud** instead of **on-premisses**. Their data resides in S3, in a directories JSON logs on user activity and JSON metadata on the songs.*

*the main task were to build an ETL pipeline that extracts the data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.*

# etl.py database schema and ETL pipeline justification.
> we have worked with AWS credentials to load the data from and into s3 bucket. the data resiend in s3://udacity-dend/ where we find song_data and log_data files(json). we have worked on this project with a smaller dataset found in the workspace (zip file).

*there were two functions for processing log and song data. passing data path and spark session as function parameters
so we can do extract data to preform reading, saving and processing data using spark*

# reading, processing and writting data**

	READING DATA: 
	we have used .json() to read and create spark dataframe (obtaining data) from log and song data. then we extracted the required data to build the song, artist, user, time and songsplays tables.
     
	PROCESSING DATA:
	the song, artist and user tables where straight forward process, where the select statment were enough to build the required tables. the time table were required a transformation of one cloumn to a new column type. where we have used a udf to build a function which preform a time converter. then added the new column of type timestamp using withcolumn function. finally, the songplays table requier join statment of two different spark df to build the required table, the song_df which is holding song_id and artist_id, and df which holds the rest of the required data.

	WRITTING DATA:
	all the tables were saved into parquet files some with partition and others not. using parquet is Better compression also better read the input and output.


# Explanation for the files in the repository
1. data folder: contain song and log data 
>the data allocated in two different folders of json type. song_data partitioned by three letters, and log_data partitioned by year and month.]


2. output folder: contain the parquet files
3. dl.cfg: configuration file contains the access keys for the AWS
4. etl.py: python file contain the code for accessing and transforming data
5. readme file: explain, summerise the project files

# How to run the project
1. runing etl.py in the terminal by typeing python etl.py
2. the etl.py will start to build a connection session to spark using dl.cfg values.
3. then the  process_song_data and  process_log_data perform the data transformation and creating the required data using the data path and spark session connection.
