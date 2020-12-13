import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    this function will execute the copying queries in sql_queries.py
    for staging events and songs. which will fill the staging tables.
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    this function will execute the insertion queries in sql_queries.py
    for all tables (facts and dimintional)
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    in the main we will configer the values of aconnection.
    then call functions to preforme copying and insertion.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
