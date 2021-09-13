import sqlite3

def create_DB():
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS stock(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INTEGER
    )""")