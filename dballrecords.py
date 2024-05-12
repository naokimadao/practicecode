
import sqlite3

def get_all_records():
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM records')
    records = cur.fetchall()

    conn.close()

    # 辞書形式に変換
    record_list = []
    for record in records:
        record_dict = {'id': record[0], 'timestamp': record[1], 'data': record[2], 'name': record[3], 'pass': record[4]}
        record_list.append(record_dict)

    return record_list
