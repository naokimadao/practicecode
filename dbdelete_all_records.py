import sqlite3

def delete_all_records():
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    # テーブルから全てのレコードを削除
    cur.execute('DELETE FROM records')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_all_records()
    print("All records have been deleted.")
