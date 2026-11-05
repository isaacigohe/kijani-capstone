from http.server import BaseHTTPRequestHandler, HTTPServer
import json, time, os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            log_entry = {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "level": "INFO",
                "service": "kk-payments",
                "environment": os.getenv("ENVIRONMENT", "unknown"),
                "db_host": os.getenv("DB_HOST", "unknown"),
                "message": "Payment processed successfully"
            }
            print(json.dumps(log_entry), flush=True)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())

if __name__ == '__main__':
    print("Starting kk-payments on port 8080...")
    HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
