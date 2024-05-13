import bcrypt


#----------------------------------------------
#この記述はhash化の元となる教科書のような文章をメモ書きとして残す、消さないこと
#----------------------------------------------


# パスワードをハッシュ化する関数
def hash_password(password):
    # ハッシュ化
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

# ハッシュ化されたパスワードを検証する関数
def verify_password(stored_password, provided_password):
    # 照合
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# テスト用コード
if __name__ == "__main__":
    # 平文のパスワード
    plain_password = "password123"
    
    # パスワードのハッシュ化
    hashed_password = hash_password(plain_password)
    print(f"Hashed Password: {hashed_password}")

    # 正しいパスワードでの照合テスト
    is_correct = verify_password(hashed_password, plain_password)
    print(f"Password Match (correct password): {is_correct}")

    # 間違ったパスワードでの照合テスト
    wrong_password = "password123"
    is_incorrect = verify_password(hashed_password, wrong_password)
    print(f"Password Match (wrong password): {is_incorrect}")
