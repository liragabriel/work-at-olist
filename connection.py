import mysql.connector

config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'books'
}

class Connection:

    def __init__(self):
        self.connection = mysql.connector.connect(**config) 

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()
