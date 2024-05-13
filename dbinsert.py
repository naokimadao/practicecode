import sqlite3
import bcrypt


def insert_record(timestamp, data, name, password):
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

        # パスワードのハッシュ化
    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


    # 削除されたIDを探す
    cur.execute('SELECT id FROM records')
    existing_ids = set(id for (id,) in cur.fetchall())
    all_ids = set(range(1, max(existing_ids) + 2))
    deleted_ids = all_ids - existing_ids


    if deleted_ids:
        new_id = min(deleted_ids)
    else:
        new_id = max(existing_ids) + 1

   
    # レコードの挿入
    cur.execute('INSERT INTO records (id, timestamp, data, name, pass) VALUES (?, ?, ?, ?, ?)', 
                (new_id, timestamp, data, name, password))

    conn.commit()
    conn.close()
