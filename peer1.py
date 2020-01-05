from network import Network
import pygame
from game_window import GameWindow
from game import Game
from player import Player
import logging


logging.basicConfig(level=logging.INFO)

net = Network(ip="localhost", port=5555)
net.start()

net.accept()

net.connect(ip="localhost", port=5556)

################################################################

game_window = GameWindow()
game = Game()
startPos = (0, 0)
player = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    player.move()
    game_window.redraw_window()


net.close()
