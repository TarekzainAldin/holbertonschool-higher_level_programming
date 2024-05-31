#!/usr/bin/python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHandler(BaseHTTPRequestHandler):
    """Handles HTTP requests"""

    def do_GET(self):
        """Handles GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            status_data = {"status": "OK"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(status_data).encode('utf-8'))
        elif self.path == '/info':
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def do_POST(self):
        """Handles POST requests"""
        self.send_response(405)
        self.send_header('Allow', 'GET')
        self.end_headers()
        self.wfile.write(b"Method not allowed for this endpoint")


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    """Runs the HTTP server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
