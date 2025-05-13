from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import sqlite3
from pathlib import Path

# SQLite database setup
DB_NAME = "auction_db.sqlite"

def init_db():
    """Initialize the SQLite database with a users table"""
    if not Path(DB_NAME).exists():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        # Add a test user
        cursor.execute("INSERT INTO users VALUES (?, ?)", ("Sid", "sid123"))
        conn.commit()
        conn.close()

# HTTP Server Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            username = data.get("username", [None])[0]
            password = data.get("password", [None])[0]

            if username and password:
                # Connect to the SQLite database
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                
                # Check if the user exists
                cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
                user = cursor.fetchone()
                conn.close()

                self.send_response(200 if user else 401)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                if user:
                    response = {"success": True, "message": "Login successful"}
                else:
                    response = {"success": False, "message": "Invalid username or password"}
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(400)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(
                    {"success": False, "message": "Missing username or password"}
                ).encode())

# Start the server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    # Initialize the database first
    init_db()
    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()