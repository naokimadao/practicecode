
import sqlite3

# データベースに接続
conn = sqlite3.connect('sample.db')
cur = conn.cursor()

# データベース内のレコードを取得
cur.execute("SELECT * FROM records")
records = cur.fetchall()

# レコードを表示
for record in records:
    print(record)

# データベース接続を閉じる
conn.close()
