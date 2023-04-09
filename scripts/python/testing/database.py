import psycopg2
import os

class Database: 
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="soccer",
            port=5432,
            user="postgres",
            password=os.getenv("SQLPASSWORD")
        )
        self.cursor = self.connection.cursor()
    
    def query(self, prompt):
        self.cursor.execute(prompt)

    def end(self):
        self.connection.commit()
        self.connection.close()