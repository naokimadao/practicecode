from http.server import HTTPServer, SimpleHTTPRequestHandler
from dbinsert import insert_record  # dbinsert.pyからinsert_recordをインポート
from dbdelete import delete_specific_records  # dbdelete.pyからdelete_specific_recordsをインポート
from dbseartch import fetch_record  # fetch_records をインポート
from urllib.parse import urlparse, parse_qs
from dbupdate import update_record
from dballrecords import get_all_records
from dbdelete_all_records import delete_all_records
from loginpass_name import verify_user
from http.cookies import SimpleCookie
from urllib.parse import quote
from dbrecordinsert import insert_day_records
import json
import requests
import secrets

#-----------------------------------------------------------------------------------------------------
#このファイルは、検索、追加、削除、更新の機能を全て実現したバージョンとなる。細かい修正と、コードの読みにくさは改善してない。
#これからその修正と改善を挿入していく。2024/05/11
#これらのファイルを編集して加筆修正した際には、.pycファイルを削除して
#新しいバイトコードを自動生成させる必要があることに気づく2024/05/12
#-----------------------------------------------------------------------------------------------------

# このファイルは、HTTPサーバーを起動し、リクエストを受け取るためのものです。




class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # def is_authenticated(self):
    #     # ユーザー認証の確認
    #     pass

    # def get_username(self):
    #     # ユーザー名を取得
    #     pass

    def do_GET(self):#getメソッドによるリクエストをここで受け取る。
        # URLの解析
        
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_components = parse_qs(parsed_url.query)

        
        # ログインページへのリダイレクト
        if path == '/':
            self.send_response(302)
            self.send_header('Location', '/html/login.html')
            self.end_headers()
            return

        # if path == '/get-user':
        #     if not self.is_authenticated():
        #         self.send_response(302)
        #         self.send_header('Location', '/login.html')
        #         self.end_headers()
        #         return

            # # ユーザー名を取得
            # username = self.get_username()

            # ユーザー名をレスポンスに含める
            # self.send_response(200)
            # self.send_header('Content-type', 'application/json')
            # self.end_headers()
            # self.wfile.write(json.dumps({'username': username}).encode())



        # `/get-record` エンドポイントの処理
        if path == '/get-record':
            record_id = query_components.get('id', [None])[0]
            if not record_id:
                self.send_error(400, 'Bad Request: No ID provided')
                return

            try:
                record = fetch_record(record_id)
                if record:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'id': record[0], 'timestamp': record[1], 'data': record[2], 'name': record[3], 'pass': '********'
                    }).encode())
                else:
                    self.send_error(404, 'お探しのレコードはありません')
            except Exception as e:
                self.send_error(500, 'Internal Server Error: {}'.format(e))
            return  # APIエンドポイントの処理後にreturnする

        elif path == '/get-all-records':
            try:
                records = get_all_records()  # ここで record_list が records として取得されます
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(records).encode('utf-8'))  # records を JSON 形式でクライアントに送信します
            except Exception as e:
                self.send_error(500, 'Internal Server Error: {}'.format(e))
            return
 

        # 静的ファイルの処理
        return super().do_GET()
    

    def do_POST(self):
        if self.path == '/add-record':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # データベースに記録
                timestamp = data['timestamp']
                user_data = data['data']
                name = data['name']
                password = data['pass']
                insert_record(timestamp, user_data, name, password)

                # 成功レスポンスを送信
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, 'Server Error: {}'.format(e))

        elif self.path == '/delete-record':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # 特定のIDに基づいてデータベースからレコードを削除
                record_id = data['id']
                delete_specific_records(record_id)

                # 成功レスポンスを送信
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'message': f'レコードのID {record_id} 削除されました。.'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, 'Server Error: {}'.format(e))
    

        elif self.path == '/update-record':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            record_id = data['id']
            new_data = data['data']

            try:
                update_record(record_id, new_data)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'message': 'レコードは更新されました。'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except ValueError as ve:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'error', 'message': str(ve)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'error', 'message': 'サーバーに正しいデータが送信できていません: {}'.format(str(e))}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
        
        elif self.path == '/login':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                credentials = json.loads(post_data.decode('utf-8'))
                username = credentials.get('username')
                password = credentials.get('password')
                valid, message = verify_user(username, password)
                if valid:
                    encoded_username = quote(username)#ユーザー名をquote関数でエンコードしている。「この記述がないとローマ字しか読み取れない。」
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {'status': 'success','message': message, 'username': encoded_username}#この場所で、ユーザー名をエンコードしている。漢字などのひらがな、カタカナ、漢字などをエンコード「jsonから読み取れる様に」するためには、quote関数を使う必要がある。
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                else:
                    self.send_response(401)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {'status': 'fail', 'message': message}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'error', 'message': str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))

        elif self.path == '/saveDayRecords':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                username = data.get('username')
                records = data.get('records')

                insert_day_records(username, records)

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'error', 'message': str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))


    def do_DELETE(self):
        if self.path == '/delete-all-records':
            try:
                delete_all_records()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'message': 'All records have been deleted'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, 'Server Error: {}'.format(e))
    
    # def is_authenticated(self):
    #     # クッキーからユーザー名を取得
    #     if 'Cookie' in self.headers:
    #         cookie = SimpleCookie(self.headers.get('Cookie'))
    #         return 'username' in cookie
    #     return False

    # def get_username(self):
    #     # クッキーからユーザー名を取得
    #     if 'Cookie' in self.headers:
    #         cookie = SimpleCookie(self.headers.get('Cookie'))
    #         if 'username' in cookie:
    #             return cookie['username'].value
    #     return None
    

# アドレス
server_address = ('localhost', 8005)

# Webサーバー起動
with HTTPServer(server_address, CustomHTTPRequestHandler) as server:
    print("Server running on port 8005...")
    server.serve_forever()