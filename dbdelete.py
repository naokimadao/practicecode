import sqlite3

def delete_specific_records(record_id):
    conn = sqlite3.connect('sample.db')
    try:
        cur = conn.cursor()
        # 特定のIDに基づいてレコードを削除
        cur.execute('DELETE FROM records WHERE id = ?', (record_id,))
        if cur.rowcount == 0:
            return "No record found with ID {}".format(record_id)
        conn.commit()
        return "Record with ID {} has been deleted.".format(record_id)
    except sqlite3.Error as e:
        print("Database error:", e)  # エラーロギング
        return "An error occurred: {}".format(e)
    finally:
        conn.close()

if __name__ == "__main__":
    try:
        record_id = int(input("Enter the ID of the record to delete: "))
        result = delete_specific_records(record_id)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
