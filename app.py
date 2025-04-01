from flask import Flask
from src.database import fetch_data, establish_connection
from dotenv import load_dotenv
from os import getenv


load_dotenv()


app = Flask(__name__)


@app.get("/")
def home():
    host = getenv("DATABASE_HOSTNAME")
    database = getenv("DATABASE_NAME")
    username = getenv("DATABASE_USERNAME")
    passwd = getenv("DATABASE_PASSWORD")
    port = getenv("DATABASE_PORT_ID")
    (connection, cursor, connection_error) = establish_connection(
        host, database, username, passwd, port
    )
    fetching = fetch_data(connection, cursor)
    return fetching
