import sqlite3
import bcrypt



# パスワードを照合する関数
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

def verify_user(username, password):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT pass FROM records WHERE name = ?", (username,))
        result = cur.fetchone()
        if result:
            stored_password = result[0]
            provided_password = password
            if verify_password(stored_password, provided_password):
                return True, "ログイン成功"
            else:
                return False, "パスワードが違います"
        else:
            return False, "ユーザー名が存在しません"
    except sqlite3.Error as e:
        return False, f"データベースエラー: {e}"
    finally:
        conn.close()
