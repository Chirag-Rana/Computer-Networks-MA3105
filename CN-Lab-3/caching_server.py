import http.server
import socketserver
import os
import hashlib
from datetime import datetime
import time

PORT = 8000
FILE_TO_SERVE = "index.html"

class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    This request handler implements caching logic using ETag and Last-Modified headers.
    It checks client-sent If-None-Match and If-Modified-Since headers to determine
    whether to send the full file content or a 304 Not Modified response.
    """
    def do_GET(self):
        if self.path == '/':
            self.path = FILE_TO_SERVE
        
        try:
            # Get file stats for modification time and content for ETag
            file_path = self.translate_path(self.path)
            last_modified_time = os.path.getmtime(file_path)
            last_modified_header = self.date_time_string(last_modified_time)

            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Generate ETag using MD5 hash of the file content
            etag = f'"{hashlib.md5(content).hexdigest()}"'
            
            # Check client's cache validation headers
            client_etag = self.headers.get('If-None-Match')
            client_last_modified = self.headers.get('If-Modified-Since')

            # Validate ETag (strong validator)
            if client_etag and client_etag == etag:
                self.send_response(304, "Not Modified")
                self.end_headers()
                return

            # Validate Last-Modified (weak validator)
            if client_last_modified:
                try:
                    # Parse the date string from the header using the correct format
                    # --- THIS IS THE CORRECTED LINE ---
                    client_modified_time = time.mktime(
                        time.strptime(client_last_modified, "%a, %d %b %Y %H:%M:%S GMT")
                    )
                    # If file hasn't been modified since client's last request, send 304
                    if last_modified_time <= client_modified_time:
                        self.send_response(304, "Not Modified")
                        self.end_headers()
                        return
                except (ValueError, TypeError):
                    # Ignore invalid date formats
                    pass

            # If cache is invalid or non-existent, send the full response
            self.send_response(200, "OK")
            self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Last-Modified", last_modified_header)
            self.send_header("ETag", etag)
            self.end_headers()
            self.wfile.write(content)
            
        except FileNotFoundError:
            self.send_error(404, "File Not Found: %s" % self.path)

# Ensure the index.html file exists
if not os.path.exists(FILE_TO_SERVE):
    with open(FILE_TO_SERVE, 'w') as f:
        f.write("<!DOCTYPE html>\n<html>\n<head><title>Test Page</title></head>\n")
        f.write("<body><h1>Hello, World! This is the first version.</h1></body>\n</html>\n")

# Set up and run the server
Handler = CachingHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print("Open your browser to http://localhost:8000")
    print("Modify index.html to see caching in action (check browser's developer tools).")
    httpd.serve_forever()
