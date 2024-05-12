import sqlite3

def insert_record(timestamp, data, name, password):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    # テーブルが存在するか確認し、存在しなければ作成する
    cur.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            data TEXT NOT NULL,
            name TEXT NOT NULL,
            pass TEXT NOT NULL
        )
    ''')

    # レコードの挿入
    cur.execute('INSERT INTO records (timestamp, data, name, pass) VALUES (?, ?, ?, ?)', 
                (timestamp, data, name, password))

    conn.commit()
    conn.close()
