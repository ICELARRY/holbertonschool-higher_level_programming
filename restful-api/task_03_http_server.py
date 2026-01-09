#!/usr/bin/env python3
import http.server
import json

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self, code, content_type="text/html"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers(200)
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._set_headers(200, "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps({"message": "OK"}).encode())
        else:
            self._set_headers(404, "application/json")
            self.wfile.write(json.dumps({"message": "Endpoint not found"}).encode())

if __name__ == "__main__":
    print(f"Starting server on port {PORT}...")
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        httpd.server_close()
