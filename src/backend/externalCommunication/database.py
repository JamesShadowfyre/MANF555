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
        print('SELECT ' + kwargs['fields'] + ' FROM ' + kwargs['table'] + ' WHERE ' + kwargs['conditions'])
        return self.db.execute('SELECT ' + kwargs['fields'] + ' FROM ' + kwargs['table'] + ' WHERE ' + kwargs['conditions']) 

    def insert(self, **kwargs):
        print('INSERT INTO ' + kwargs['table'] + ' (' + kwargs['columns'] + ') values (' + kwargs['values'] + ')')
        self.db.execute('INSERT INTO ' + kwargs['table'] + ' (' + kwargs['columns'] + ') values (' + kwargs['values'] + ')') 
        self.db.commit()

    def update(self, **kwargs):
        print('UPDATE ' + kwargs['table'] + ' SET ' + kwargs['arguments'] + ' WHERE ' + kwargs['conditions'])
        self.db.execute('UPDATE ' + kwargs['table'] + ' SET ' + kwargs['arguments'] + ' WHERE ' + kwargs['conditions'])
        self.db.commit()

    def delete(self, **kwargs):
        print('DELETE FROM ' + kwargs['table'] + ' WHERE ' + kwargs['conditions'])
        self.db.execute('DELETE FROM ' + kwargs['table'] + ' WHERE ' + kwargs['conditions'])
        self.db.commit()

