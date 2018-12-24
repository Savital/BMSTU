import threading
import shutil
from http.server import HTTPServer, BaseHTTPRequestHandler

class MiniServerA(HTTPServer):
    def __init__(self, url, processor):
        self.server = HTTPServer(url, processor)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.deamon = True

    def up(self):
        self.thread.start()
        print('starting server on port {}'.format(self.server.server_port))

    def down(self):
        self.server.shutdown()
        print('stopping server on port {}'.format(self.server.server_port))

class SimpleProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Welcome to sevice2!</h1>")
            self.wfile.write(b"<button><a href='./tmp'>Result :D</a></button>")
        elif self.path == '/tmp':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open('media/after.jpg', 'rb') as content:
                shutil.copyfileobj(content, self.wfile)
        elif self.path == "/media/after.jpg":
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open('media/after.jpg', 'rb') as content:
                shutil.copyfileobj(content, self.wfile)

        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'404 :(')


mini = MiniServerA(('localhost', 8004), SimpleProcessor)
mini.up()
text = ""
while (text != "quit"):
    text = input()
mini.down()