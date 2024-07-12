
import sqlite3
import bcrypt

def checktebleflag():
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

        # テーブルが存在するか確認し、存在しなければ作成する
    cur.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            data TEXT NOT NULL,
            name TEXT NOT NULL,
            pass TEXT NOT NULL
        )
    ''')

    # テーブル内にレコードが存在するか確認

    cur.execute('SELECT * FROM records')
    rows = cur.fetchall()

    if rows == []:

        new_id = 1
        timestamp = '2021-01-01 00:00:00'
        data = 'Hello, World!'
        name = 'admin'
        password = 'password'
        def insert_record_first(timestamp, data, name, password):

            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                # レコードの挿入
            cur.execute('INSERT INTO records (id, timestamp, data, name, pass) VALUES (?, ?, ?, ?, ?)', 
                        (new_id, timestamp, data, name, password))
        insert_record_first(timestamp, data, name, password)
        print('レコードを挿入しました。')

        
    else:
        
        print('レコードが存在します。')
        conn.close()



    conn.close()

if __name__ == "__main__":
    checktebleflag()