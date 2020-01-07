from networking.network import Network
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

    # net = establish_network()
    # print("lol")
    # net.send("hello")
    net = Network(ip="localhost", port=5555)
    application = Application(net)
    application.launch_game()


if __name__ == '__main__':
    main()
