

# **Query Description**

## *select * from song_details_by_sessions*

    A Query to verify the data was entered into the table. 
        CAUTION:htis is not an appropriate select statment to do with big datasets.

## *select artist,length,song from song_details_by_sessions where sessionid=num and iteminsession=num*

    A Query retraives songs and artists details for a given sessionid and iteminsession.

## *select artist,song,iteminsession,firstname,lastname from song_details_for_userid where userid=num and sessionid=num*

    A Query retraives user name who are listening to a specific song ordered by iteminsession

## *select firstName, lastName from user_name_listen_to_asong where song='SONG NAME'*

        A Query that retraive user name who are listening to a specific song. to make sure that this guery retraive all the names we have specified a userid as a clustering key and song as partition key
