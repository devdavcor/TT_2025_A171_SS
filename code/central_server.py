import socket
import threading

class CentralServer:
    def __init__(self, host='localhost', puerto=12345, max_conexiones=5):
        self.host = host
        self.puerto = puerto
        self.max_conexiones = max_conexiones
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.puerto))
        self.servidor.listen(self.max_conexiones)
        print(f"Servidor iniciado en {self.host}:{self.puerto}")

    def manejar_cliente(self, conn, addr):
        print(f"[Conexión] Cliente conectado desde {addr}")
        conn.sendall(b"Hola cliente, soy el servidor central\n")
        while True:
            datos = conn.recv(1024)
            if not datos:
                break
            print(f"[{addr}] Mensaje recibido:", datos.decode())
            conn.sendall(b"Mensaje recibido.\n")
        conn.close()
        print(f"[Desconectado] Cliente {addr} desconectado")

    def iniciar(self):
        print(f"[Esperando] Hasta {self.max_conexiones} conexiones...")
        while True:
            conn, addr = self.servidor.accept()
            hilo = threading.Thread(target=self.manejar_cliente, args=(conn, addr))
            hilo.start()
            print(f"[Activo] Clientes conectados: {threading.active_count() - 1}")

if __name__ == "__main__":
    server = CentralServer(puerto=8000, max_conexiones=10)
    server.iniciar()
