import psycopg2
import os
from configparser import ConfigParser

class Database: 
    def __init__(self):

        # obtain information from the creds.ini file
        parser = ConfigParser()
        parser.read('creds.ini')
        pgcreds = {}
        if parser.has_section('pgdb'):
            items = parser.items("pgdb")
            for item in items:
                pgcreds[item[0]] = item[1]

        self.connection = psycopg2.connect(**pgcreds)
        self.cursor = self.connection.cursor()
    
    def query(self, prompt):
        self.cursor.execute(prompt)

    def end(self):
        self.connection.commit()
        self.connection.close()