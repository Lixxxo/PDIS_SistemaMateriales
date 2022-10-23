import pyodbc
from Database.connection import connection_string


class MSSQLConnector:
    cursor = pyodbc.connect(connection_string)
