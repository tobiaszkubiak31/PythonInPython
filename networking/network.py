import socket
import logging


class Network:
    def __init__(self, ip="localhost", port=5555):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.socket = None  # socket for writing data
        self.conn = None  # socket for listening for incoming data

    def start(self):
        """Start server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # to prevent "address already in use" error
        self.socket.bind(self.address)
        self.socket.listen(1)   # limit number of connections to 1
        logging.info("Server Started")

    def accept(self):
        """Accept incoming connection from other player."""
        logging.info("Waiting for a connection...")
        conn, addr = self.socket.accept()
        logging.info("Connected to: " + str(addr))
        return conn, addr

    def connect(self, ip, port):
        """Connect to other player."""
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((ip, port))

    def send(self, data):
        try:
            return self.socket.send(str.encode(data))
        except socket.error as e:
            print(e)

    def recv(self):
        return self.conn.recv(2048).decode()

    def close(self):
        self.socket.close()
        self.conn.close()

