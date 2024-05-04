import sqlite3

def create_records_table():
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()
    
    cur.execute(''' 
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    data TEXT
                    )''')
    
    conn.commit()
    conn.close()

# レコードテーブルを作成
create_records_table()

