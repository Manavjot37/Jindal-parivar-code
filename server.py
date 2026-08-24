import http.server
import socketserver
import json
from pathlib import Path

PORT = 8010
ROOT = Path(__file__).parent

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            html_content = (ROOT / "index.html").read_text(encoding="utf-8")
            self.wfile.write(html_content.encode('utf-8'))
            return

        if self.path == '/api/summary':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "summary": {
                    "total_cases": 12,
                    "high_risk": 5,
                    "critical_nodes": 2,
                    "active_alerts": 8
                },
                "cases": [
                    {"alias": "nightmarket_17", "platform": "Telegram", "risk": 86},
                    {"alias": "greenparcel", "platform": "DarkNet", "risk": 93},
                    {"alias": "blueorbit", "platform": "Signal", "risk": 71},
                    {"alias": "wallet_X2", "platform": "Crypto", "risk": 82}
                ],
                "alerts": [
                    {"timestamp": "17:30", "text": "High volume transaction detected on Wallet_X2"},
                    {"timestamp": "17:15", "text": "New cluster linked to nightmarket_17"}
                ]
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return

        super().do_GET()

print(f"SentinelTrace V2 running at http://127.0.0.1:{PORT}")
with socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler) as httpd:
    httpd.serve_forever()