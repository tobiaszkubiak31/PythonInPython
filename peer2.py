from network import Network
import pygame
from game_window import GameWindow
from game import Game
from player import Player
import logging


logging.basicConfig(level=logging.INFO)

net = Network(ip="localhost", port=5556)
net.start()

net.connect(ip="localhost", port=5555)

net.accept()

net.close()
