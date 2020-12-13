purpose of this project.
------------------------
*Sparkify has grown data therefore, they have upgrade their infrastructure and use **cloud** instead of **on-premisses**. Their data resides in S3, in a directories JSON logs on user activity and JSON metadata on the songs.*

*the main task were to build an ETL pipeline that extracts the data from S3, stages them in Redshift, then transforms them into a fact table and set of dimensional tables so Sparkify analytics team can find insights in what songs their users are listening to.*

database schema and ETL pipeline justification.
-----------------------------------------------
>as we were working in redshift we need a staging step were we load the data from S3 to staging tables.then using staging tables the data can be manibulated by executing SQL statements to create and fill the desire database tables.

**1. staging**

*the idea of staging is to prepare the data so it can be transoform into redshift datbase. by extracting data from json files log_data and song_data into event_log_data and songs_ifo tables. know we can use the event_log_data and songs_ifo tables to build the desire database schema.*

**2. building database**

*in this step we implement the database schema, where the fact table was playsongs and the dimentonal tables were users, songs, artists and time. the data were extracted from event_log_data and songs_ifo tables into playsongs, users, songs, artists and time by executing inserting SQL statments.*

**3. files and queries**

>the sql_queries.py has all the querys to preforme the staging steps and building the database.

- create_table_queries
    
    *this command execute all the create tables statments.*


- copy_table_queries

    *this command execute the staging tables inseartion.*


- insert_table_queries

    *this command execute the inserting statment for the fact and dimentional tables.*


*the fact table (**songplays**) has the forgn keys of dimentional tables:*
1. user_id for users table
2. song_id for songs table
3. artist_id for artists table 
4. start_time for time table  

