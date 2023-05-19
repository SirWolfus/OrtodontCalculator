import sqlite3 as sq


def db_drope():
    with sq.connect('DBFile/dbortocalc.db') as db:
        cur = db.cursor()
        cur.execute('DROP TABLE IF EXISTS patients')
        cur.execute('DROP TABLE IF EXISTS pdata')


def db_first_connect():
    with sq.connect('DBFile/dbortocalc.db') as db:
        cur = db.cursor()
        # Создание таблицы пациентов
        cur.execute("""CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        name TEXT NOT NULL,        
        date DATETIME NOT NULL, 
        UNIQUE ("name","date") ON CONFLICT IGNORE      
        )""")
        # Создание таблицы формул
        cur.execute("""CREATE TABLE IF NOT EXISTS pdata (
        id_pat INTEGER,        
        formula TEXT,
        findex TEXT        
        )""")


def db_pat_insert(first_name, surname, fathername, date):
    try:
        with sq.connect('DBFile/dbortocalc.db') as db:
            cur = db.cursor()
            cur.execute(f"SELECT * FROM patients WHERE name = '{first_name} {surname} {fathername}' AND date = '{date}'")
            if cur.fetchone() == None:
                cur.execute(f"""INSERT INTO patients (name,date) VALUES ('{first_name} {surname} {fathername}','{date}')""")
                return 'Все ОК!!'
            else:
                return 'Повтор данных'
    except:
        return ValueError('Ошибка записи данных')

def db_pdata_insert(n, data, findex):
    try:
        with sq.connect('DBFile/dbortocalc.db') as db:
            data = '*'.join([str(i) for i in data])
            findex = '*'.join([str(i) for i in findex])
            cur = db.cursor()
            cur.execute(f"""INSERT INTO pdata (id_pat, formula, findex) 
            VALUES ({n}, '{data}', '{findex}')""")

    except:
        return ValueError('Ошибка записи данных')

def db_pat_box():
    with sq.connect('DBFile/dbortocalc.db') as db:
        cur = db.cursor()
        cur.execute(f"SELECT name FROM patients")

        return sorted([i[0] for i in cur])



# db_drope()
# db_first_connect()

