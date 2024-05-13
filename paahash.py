import bcrypt

# パスワードをハッシュ化する関数
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
