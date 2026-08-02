import sqlite3

class PortfolioHandler:
    def __init__(self, filename):
        self.filename = filename

    def _connect(self):
        self.cnx = sqlite3.connect(self.filename)
        self.cur = self.cnx.cursor()
        self.cur.execute('SELECT name FROM sqlite_master')

        if self.cur.rowcount == -1:
            #DB is non existent
            self._prime()


    def _prime(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS tickers ( \
            id INTEGER PRIMARY KEY, \
            name text NOT NULL); \
            ')
        self.cur.execute('CREATE TABLE IF NOT EXISTS movements ( \
            id INTEGER PRIMARY KEY, \
            date DATE NOT NULL, \
            type INT NOT NULL, \
            ticker INT, \
            value REAL NOT NULL, \
            qty INT); \
            ')

    def add_movement(self):
        if self._connect()
