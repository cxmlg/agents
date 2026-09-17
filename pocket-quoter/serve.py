"""本地预览服务器：带 no-cache 响应头 + IPv4 绑定，确保手机/浏览器总能拿到最新页面。用法：python serve.py [端口]"""
import http.server
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class Server(http.server.ThreadingHTTPServer):
    address_family = __import__('socket').AF_INET
    allow_reuse_address = True

if __name__ == '__main__':
    Server(('0.0.0.0', PORT), Handler).serve_forever()
