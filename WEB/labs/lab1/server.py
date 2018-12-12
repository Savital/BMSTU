from http.server import BaseHTTPRequestHandler, HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<h1 align='center'>Service #1!</h1>")
            self.wfile.write(b"<p align='center'>Click here to see photo</p>")
            self.wfile.write(b"<p align='center'><a href='./images'>My Photo</a></p>")
        elif self.path == '/images':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<img src='https://pp.userapi.com/c850128/v850128816/4ef64/RKzWYhNmfNU.jpg' />")
        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'404 :(')

serv = HTTPServer(("127.0.0.1", 8003), HttpProcessor)
print("Server is running...")
serv.serve_forever()
