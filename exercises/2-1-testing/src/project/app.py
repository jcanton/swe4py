import os
from dataclasses import dataclass

class Driver:

    def __init__(self, dbname):
        self.dbname = dbname
        self.username = os.getenv('USERNAME')

    def connect(self):
        password = os.getenv('PASSWORD')
        self.connection = DB(self.dbname).connect(self.username, password)


@dataclass
class DB:
    dbname: str

    def connect(self, username, password):
        import time
        time.sleep(10)
        _ = password
        return {
            'status': 'connected',
            'username': username
        }
