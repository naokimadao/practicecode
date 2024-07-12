
#-------------------------------------------------------
#id=1のレコード以外を削除する場合は以下のように変更する
#-------------------------------------------------------

import sqlite3

def delete_all_records():
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    # テーブルからidが1以外の全てのレコードを削除
    cur.execute('DELETE FROM records WHERE id != 1')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    delete_all_records()
    print("All records have been deleted.")
