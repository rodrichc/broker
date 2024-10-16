import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='argbroker',
            port='3306'
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()
