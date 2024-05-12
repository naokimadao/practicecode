import sqlite3

def fetch_record(record_id):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, timestamp, data, name, pass FROM records WHERE id = ?", (record_id,))
        record = cur.fetchone()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        record = None
    finally:
        conn.close()
    return record
