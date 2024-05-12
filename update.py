import sqlite3

# データベースに接続
conn = sqlite3.connect('sample.db')
cur = conn.cursor()

try:
    # ユーザーからレコードIDを入力
    record_id = input("更新するレコードのIDを入力してください: ")
    
    # ユーザーから新しいデータを入力
    new_data = input("新しいデータを入力してください: ")

    # レコードの更新
    cur.execute("UPDATE records SET data = ? WHERE id = ?", (new_data, record_id))
    conn.commit()
    print(f"レコードID {record_id} が更新されました。")

except sqlite3.Error as e:
    print(f"エラーが発生しました: {e}")

    # データベース接続を閉じる
    

conn.close()
