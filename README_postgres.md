
# **Introduction**

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. to understanding what songs users are listening to.the aim is to create a Postgres database with tables designed to optimize queries on song play. so the role is to create a database schema and ETL pipeline

# **Database**

we will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables.
Song Dataset contains data about song and artist of that song.
Log Dataset consists of log files based on the songs in the dataset above


# **Files in repository**


## sql_queries.py

	I have to implements drop, create and insert statements which was straightforwrad.also, there were a select statement which help me to obtain song_id and artisit_id from songs and artist tables.

## etl.py

	this python file help me to integrate all the work done in section 1 into single working space using the whole dataset (log_data, song_data). I have copied the subwork in etl.ipynb into the missing part then compile the file in the terminal to make sure the work is completed without any error.


the test.ipynb helped me to make sure that the tables were created and the data were inserted correctly.
the create_tables.py runing the queries written in section 2 (sql_queries.py)
each time I have change any thing in the sql_queries.py I need to restart the kernel in both (test and etl) and rerun create_tables.py 

# **tables schema**

1.fact table

	the songplays is the fact tabl holds *level*,*song_id*,*artist_id*,*location* and *user_agent* attributes with forgen keys *start_time*,*user_id* and *session_id*.

2.dimenssion table

	1. the users table indiate information about the users as *user_id*,*first_name*,*last_name*,*gender* and *level*.
	2. the songs table indicate information about *song_id*,*title*,*artist_id*,*year* andd *song duration*.
	3. the artists tables give us information about the artist such as *artist_id*,*artist name*,*location*, *artist latitude* and *artist longitude*.
	4. the time table give us time and date details. information includes *hours*,*day*, *week*, *month*, *year* and *weekday*.


# **run the python scripts**

follow the instruction on etl.ipynb.run reate_table and test.ipynb when you finish the work in each section to make sure the work is correct and table and the data were created. restart the kerenel if needed to do the next section in etl.ipynb.
when you have finished doing etl.ipynb implement the required statments of ETL into etl.py and run the script using terminal @python etl.py@.
