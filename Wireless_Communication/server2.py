from http.server import HTTPServer, BaseHTTPRequestHandler

class MyTCPHandler(BaseHTTPRequestHandler):
    def handle(self):
        print("Connection Detected")
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote")
        print(self.data)
        self.request.sendall(self.data.upper())
        
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    server = HTTPServer(HOST, PORT, MyTCPHandler)
    server.serve_forever()
    