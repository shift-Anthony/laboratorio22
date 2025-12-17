from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            #HTML
            html = """
            <!DOCTYPE html>
            <html>
            <head><title>Ejercicio 5</title></head>
            <body>
                <h1>Bienvenido al Servidor</h1>
                <p>Respuesta HTML estática.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))

        elif self.path == "/saludo":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            data = {"msg": "Hola"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
# Configuracion
if __name__ == "__main__":
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), Servidor)
    print(f"Servidor corriendo en http://{host}:{port}")
    print(f"Prueba HTML: http://{host}:{port}/")
    print(f"Prueba JSON: http://{host}:{port}/saludo")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        server.server_close()