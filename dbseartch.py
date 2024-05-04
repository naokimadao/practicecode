import sqlite3

def fetch_records(record_id):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()
    cur.execute("SELECT id, timestamp, data FROM records WHERE id = ?", (record_id,))
    record = cur.fetchone()
    conn.close()
    return record
