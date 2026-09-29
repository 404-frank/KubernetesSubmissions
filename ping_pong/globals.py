import psycopg2
import os
#from psycopg2.extensions import connection


def create_connection():
    postgres_host = os.environ['POSTGRES_HOST']
    postgres_port = int(os.environ['POSTGRES_PORT'])
    postgres_database = os.environ['POSTGRES_DATABASE_NAME']
    postgres_user = os.environ['POSTGRES_USER']
    postgres_password = os.environ['POSTGRES_PASSWORD']
    _conn = psycopg2.connect(
        database=postgres_database, # enter your database name
        user=postgres_user,         # enter your postgres username
        password=postgres_password, # enter your password
        host=postgres_host,         # the service name
        port=postgres_port          # port number
    )
    _conn.autocommit = True
    return _conn

def update_and_get_counter():
    print("creating connection")
    _conn = create_connection()
    print(f"getting a cursor")
    _cursor = _conn.cursor()
    print(f"get the current counter")
    _cursor.execute("select counter from pingpongs where id=1")
    current_counter = int(_cursor.fetchone()[0])
    new_counter = current_counter + 1
    print(f"update row to {new_counter}")
    _cursor.execute(f"update pingpongs set counter = %s where id = 1", (new_counter,))
    _cursor.close()
    _conn.close()
    return new_counter

def get_counter():
    print("creating connection")
    _conn = create_connection()
    print(f"getting a cursor")
    _cursor = _conn.cursor()
    print(f"get the current counter")
    _cursor.execute("select counter from pingpongs where id=1")
    current_counter = int(_cursor.fetchone()[0])
    _cursor.close()
    _conn.close()
    return current_counter
