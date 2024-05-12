import sqlite3

def update_record(record_id, new_data):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()
    try:
        cur.execute("UPDATE records SET data = ? WHERE id = ?", (new_data, record_id))
        conn.commit()
        if cur.rowcount == 0:
            raise ValueError("更新されたレコードがありません。IDが正しいか確認してください。")
    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")
        raise e
    except ValueError as ve:
        print(f"更新エラー: {ve}")
        raise ve
    finally:
        conn.close()