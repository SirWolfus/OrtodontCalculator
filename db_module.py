import sqlite3 as sq
import pickle



def db_drope():
    with sq.connect('DBFile/dbortocalc.db') as db:
        cur = db.cursor()
        cur.execute('DROP TABLE IF EXISTS patients')

def db_connect():
    with sq.connect('DBFile/dbortocalc.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        formula TEXT
        )""")

def db_insert(n, data):
    with sq.connect('DBFile/dbortocalc.db') as db:
        new_data = '*'.join([str(i) for i in data])
        cur = db.cursor()
        cur.execute(f"""INSERT INTO patients (name, formula) VALUES ('{str(n)}', '{new_data}')""")
        # print(f"""INSERT INTO patients (name, formula) VALUES ('{str(n)}', '{new_data}')""")

db_drope()
db_connect()
# db_insert('Test Pat','10')

