import socket
import logging


class Network:
    def __init__(self, ip="localhost", port=5555):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None  # listens for connection requests
        self.sender = None  # sends data to the other player
        self.receiver = None  # listens for incoming data

    def start(self):
        """Start server."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # to prevent "address already in use" error
        self.server.bind(self.address)
        self.server.listen(1)   # limit number of connections to 1
        logging.info("Server Started")

    def accept(self):
        """Accept incoming connection from other player."""
        logging.info("Waiting for a connection...")
        self.receiver, addr = self.server.accept()
        logging.info("Connected to: " + str(addr))

    def connect(self, ip, port):
        """Connect to the other player."""
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sender.connect((ip, port))
            return True
        except ConnectionRefusedError:
            return False

    def send(self, data):
        data_str = str(data) + '\n'
        self.sender.sendall(data_str.encode())

    def recv(self):
        return self.receiver.recv(4096).decode()

    def close(self):
        self.server.close()
        self.sender.close()
        self.receiver.close()
