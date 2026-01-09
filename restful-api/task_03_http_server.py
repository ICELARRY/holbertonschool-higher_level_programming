#!/usr/bin/env python3
import http.server
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, code=200, ctype="text/plain"):
        # code həmişə integer olmalıdır
        self.send_response(code)
        self.send_header("Content-type", ctype)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._set_headers(200, "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self._set_headers(200, "application/json")
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
        else:
            self._set_headers(404, "application/json")
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode())

def run():
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    print(f"Starting server on port {PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    finally:
        server.server_close()

if __name__ == "__main__":
    run()
