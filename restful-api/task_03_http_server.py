#!/usr/bin/env python3
import http.server
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, code=200, ctype="text/plain"):
        self.send_response(code)
        self.send_header("Content-type", ctype)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self._set_headers("200", "application/json")
            self.wfile.write(json.dumps({"name":"John","age":30,"city":"New York"}).encode())
        elif self.path == "/status":
            self._set_headers("200","application/json")
            self.wfile.write(json.dumps({"status":"OK"}).encode())
        else:
            self._set_headers(404,"application/json")
            self.wfile.write(json.dumps({"error":"Endpoint not found"}).encode())

def run():
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    print(f"Starting server on port {PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.server_close()

if __name__ == "__main__":
    run()
