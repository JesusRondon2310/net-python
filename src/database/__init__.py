import psycopg
from datetime import datetime


def establish_connection(hostname, database, username, psswd, port_id):
    try:
        conn = psycopg.connect(
            host=hostname, dbname=database, user=username, password=psswd, port=port_id
        )
        cur = conn.cursor()
        print("connection succesfull!")
        conn.commit()
        return (conn, cur, None)
    except Exception as error:
        return (None, None, error)


def create_table(connection, cursor):
    try:
        create_script = """CREATE TABLE IF NOT EXISTS system (
            memory VARCHAR(20), timestamp TIMESTAMP
            )"""
        cursor.execute(create_script)
        connection.commit()
        return ("successfully created table!", None)
    except Exception as error:
        return (None, error)


def add_records(connection, cursor, memory: str, timestamp: datetime):
    try:
        insert_script = "INSERT INTO system (memory, timestamp) VALUES (%s, %s)"
        insert_value = (memory, timestamp)
        cursor.execute(insert_script, insert_value)
        connection.commit()
        return ("successfully added records!", None)
    except Exception as error:
        return (None, error)


def fetch_data(connection, cursor):
    try:
        cursor.execute("SELECT * FROM system")
        specs = []
        for record in cursor.fetchall():
            memory = record[0]
            timestamp = record[1]
            specs.append({"memory": memory, "timestamp": timestamp})
        connection.commit()
        return (specs, None)
    except Exception as error:
        return (None, error)
