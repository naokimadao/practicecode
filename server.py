from http.server import HTTPServer, SimpleHTTPRequestHandler
from dbinsert import insert_record  # dbinsert.pyからinsert_recordをインポート
from dbdelete import delete_specific_records  # dbdelete.pyからdelete_specific_recordsをインポート
from dbseartch import fetch_records  # fetch_records をインポート
import json

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # 静的ファイルの場合は親クラスのメソッドを使用
        if self.path in ('/index.html', '/ugoku.js', '/design.css'):
            return super().do_GET()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # index.html を直接返す
        with open('index.html', 'r') as file:
            self.wfile.write(file.read().encode())

        

    def do_POST(self):
        if self.path == '/add-record':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # データベースに記録
                timestamp = data['timestamp']
                insert_record(timestamp, "sample_data")

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
                response = {'status': 'success', 'message': f'Record with ID {record_id} has been deleted.'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, 'Server Error: {}'.format(e))
        
        elif self.path == '/get-records':
            try:
                records = fetch_records()
                if records:
                    response_data = [{'id': record[0], 'timestamp': record[1], 'data': record[2]} for record in records]
                else:
                    response_data = []

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode('utf-8'))

                # 成功レスポンスを送信
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'status': 'success', 'message': f'Record with ID {record_id} has been deleted.'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, 'Server Error: {}'.format(e))

# アドレス
server_address = ('localhost', 8080)

# Webサーバー起動
with HTTPServer(server_address, CustomHTTPRequestHandler) as server:
    print("Server running on port 8080...")
    server.serve_forever()
