"""Static file server for Zeabur deployment.
Listens on $PORT env var (default 8080).
"""
import os
import http.server
import socketserver

PORT = int(os.environ.get('PORT', 8080))
Handler = http.server.SimpleHTTPRequestHandler

class NoCacheHandler(Handler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
    print(f"Serving HTTP on 0.0.0.0 port {PORT}")
    httpd.serve_forever()
