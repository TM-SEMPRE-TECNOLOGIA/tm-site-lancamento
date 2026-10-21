import http.server
import socketserver
import json
import base64
import os

PORT = 4010
TARGET_DIR = os.path.abspath("assets/logos")

class SaveHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            data = json.loads(body.decode('utf-8'))
            filename = data['filename']
            b64data = data['data']
            if ',' in b64data:
                b64data = b64data.split(',', 1)[1]
            raw_bytes = base64.b64decode(b64data)
            
            filepath = os.path.join(TARGET_DIR, filename)
            with open(filepath, 'wb') as f:
                f.write(raw_bytes)
            print(f"SAVED: {filename} ({len(raw_bytes)} bytes)")
            
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        else:
            self.send_response(404)
            self.end_headers()

print(f"Starting Logo Saver Server on port {PORT}...")
with socketserver.TCPServer(("127.0.0.1", PORT), SaveHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
