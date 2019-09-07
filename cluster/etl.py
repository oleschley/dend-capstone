import configparser
import psycopg2

from queries import drop, create, insert

def execute(cur, conn):

    # Drop existing tables
    for query in drop:
        cur.execute(query)
        conn.commit()
    
    # Create empty tables
    for query in create:
        cur.execute(query)
        conn.commit()

    # Load data into tables
    for query in insert:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.conf')

    host = config['CLUSTER']['HOST']
    db = config['CLUSTER']['DB_NAME']
    user = config['CLUSTER']['DB_USER']
    pwd = config['CLUSTER']['DB_PASSWORD']
    port = config['CLUSTER']['DB_PORT']

    conn = psycopg2.connect(f'host={host} dbname={db} user={user} password={pwd} port={port}')
    cur = conn.cursor()
    execute(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()