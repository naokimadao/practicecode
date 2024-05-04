import sqlite3

def insert_record(timestamp, data):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    # テーブルが存在するか確認し、存在しなければ作成する
    cur.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')

    # レコードの挿入
    cur.execute('INSERT INTO records (timestamp, data) VALUES (?, ?)', (timestamp, data))

    conn.commit()
    conn.close()
