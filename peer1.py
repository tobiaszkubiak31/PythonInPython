from network import Network
from application import Application
import logging


def establish_network():
    net = Network(ip="localhost", port=5555)
    net.start()
    net.accept()
    net.connect(ip="localhost", port=5556)
    return net


def main():
    logging.basicConfig(level=logging.INFO)

    net = establish_network()

    application = Application()
    application.set_network(net)
    application.set_environment()
    application.set_snake_color((100, 0, 100))
    application.launch_game()


if __name__ == '__main__':
    main()
