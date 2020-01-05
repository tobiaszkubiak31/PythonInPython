from network import Network
from application import Application
import logging


def establish_network():
    net = Network(ip="localhost", port=5555)
    net.start()
    net.connect(ip="localhost", port=5556)
    net.accept()
    return net


def main():
    logging.basicConfig(level=logging.INFO)

    net = establish_network()

    application = Application(net)
    application.launch_game()


if __name__ == '__main__':
    main()
