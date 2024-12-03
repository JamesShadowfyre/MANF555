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
        if kwargs['fields'] == None:
            kwargs['fields'] = '*'
        return self.db.execute('SELECT ' + kwargs['fields'] + ' FROM ' + kwargs['table'] + ' WHERE ' + kwargs['conditions'])

    def insert(self, **kwargs):
        self.db.execute

    def update(self, **kwargs):
        self.db.execute