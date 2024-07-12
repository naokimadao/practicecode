import requests

# 定数
CLIENT_ID = 'bc3e79d8ede3af71028fd6cf899fef9a03b8d9b367b92c50b11a5fe909130328'
CLIENT_SECRET = '94ed312678e805fae62fb5fb673de4d0e46cfb935800db9f5c2863b3dddff6cf'
REFRESH_TOKEN = '3d53eab07157cfcedeb122fbdb247f69dbc659913f6e35df32e0009e46f10c3f'
TOKEN_URL = 'https://accounts.secure.freee.co.jp/public_api/token'

# トークンのリフレッシュ
def refresh_access_token():
    data = {
        'grant_type': 'refresh_token',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN
    }
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to refresh token: {response.json()}")

# アクセストークンの取得
ACCESS_TOKEN = refresh_access_token()
HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

print("Access token refreshed:", ACCESS_TOKEN)



# // Webアプリ認証用URL// https://accounts.secure.freee.co.jp/public_api/authorize?client_id=bc3e79d8ede3af71028fd6cf899fef9a03b8d9b367b92c50b11a5fe909130328&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&prompt=select_company
# //Client Secret//94ed312678e805fae62fb5fb673de4d0e46cfb935800db9f5c2863b3dddff6cf
# //Client ID//bc3e79d8ede3af71028fd6cf899fef9a03b8d9b367b92c50b11a5fe909130328
# //コールバックURL//urn:ietf:wg:oauth:2.0:oob
# 事業所ID:11449504
# アクセストークン：3d53eab07157cfcedeb122fbdb247f69dbc659913f6e35df32e0009e46f10c3f
