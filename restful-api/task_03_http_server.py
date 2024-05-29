#!/usr/bin/python3
"""`http.server` module"""

# Importer les modules nécessaires
import http.server
import socketserver
import json


# Définir une classe de gestionnaire de requêtes
class MyHandler(http.server.BaseHTTPRequestHandler):
    """subclass"""
    def do_GET(self):
        if self.path == "/data":
            # Préparer les données JSON
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            # Retourner le statut OK
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode())
        elif self.path == "/info":
            # Retourner les informations de l'API
            info = {"vers": "1.0", "descript": "Une API sim const http.server"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())
        else:
            # Gérer les endpoints non définis
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(
                {"error": "Endpoint non trouvé"}).encode())


# Définir le port du serveur
PORT = 8000


# Créer le serveur
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serveur actif sur le port {PORT}")
    # Démarrer le serveur
    httpd.serve_forever()
