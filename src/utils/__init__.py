from time import sleep
from src.ssh import init, exit_ssh, command
from src.database import establish_connection, create_table, add_records
from datetime import datetime
from dotenv import load_dotenv
from os import getenv


load_dotenv()


def worker(cmd, timer):
    host = getenv("DATABASE_HOSTNAME")
    database = getenv("DATABASE_NAME")
    username = getenv("DATABASE_USERNAME")
    passwd = getenv("DATABASE_PASSWORD")
    port = getenv("DATABASE_PORT_ID")

    try:
        channel = init()
        (connection, cursor, connection_error) = establish_connection(
            host, database, username, passwd, port
        )
        print(connection_error)
        (table, table_error) = create_table(connection, cursor)
        print(table_error)
        while True:
            sleep(timer)
            error, result = command(channel=channel, cmd=cmd)
            if error:
                raise Exception(f"{result}")
            now = datetime.now()
            (add_data, add_data_error) = add_records(
                connection, cursor, result.replace("Memory: ", ""), now
            )
            print(add_data_error)
            print(f"output:\n{result}Time: {now}\n", flush=True)
    except Exception as e:
        print(f"error found: {str(e)}")
        exit_ssh(channel=channel)
