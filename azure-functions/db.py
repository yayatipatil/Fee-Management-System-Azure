import os
import pyodbc


def get_connection():
    connection_string = os.environ.get("SQL_CONNECTION_STRING")

    if not connection_string:
        raise ValueError("SQL_CONNECTION_STRING is not configured")

    return pyodbc.connect(connection_string)