import sqlite3

class Database:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
            return cls.instance
        return cls.instance
    
    def connect(self):
        self.db = sqlite3.connect("database.db")
        with open(r'src\backend\externalCommunication\database.sql') as sql_file:
            sql_script = sql_file.read()
        self.db.executescript(sql_script)

    def select(self, **kwargs):
        self.db.execute

    def write(self, **kwargs):
        self.db.execute