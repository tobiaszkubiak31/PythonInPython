from network import Network
import logging


logging.basicConfig(level=logging.INFO)

net = Network(ip="192.168.0.196", port=5555)
net.start()

net.accept()

net.connect(ip="192.168.0.196", port=5556)

net.close()

