import sqlite3


class DB:
    def __init__(self, name):
        self.name = "data.db"
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()

    def init_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS stock(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER
        )""")

    def add_item(self, name, price, quantity):
        self.c.execute("""INSERT INTO stock(name, price, quantity)
            VALUES(?, ?, ?)""", (name, price, quantity))
        self.conn.commit()

    def remove_item(self, name):
        self.c.execute("""DELETE FROM stock WHERE name=?""", (name,))
        self.conn.commit()

    def create_item(self, name, price, quantity):
        self.c.execute("""INSERT INTO stock(name, price, quantity)
            VALUES(?, ?, ?)""", (name, price, quantity))
        self.conn.commit()

    def delete_item(self, name):
        self.c.execute("""DELETE FROM stock WHERE name=?""", (name,))
        self.conn.commit()

    def get_item(self, name):
        self.c.execute("""SELECT * FROM stock WHERE name=?""", (name,))
        return self.c.fetchone()

    def get_all(self):
        self.c.execute("""SELECT * FROM stock""")
        return self.c.fetchall()

    def close(self):
        self.conn.close()