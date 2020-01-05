import pygame
from game_window import GameWindow
from game import Game
from player import Player


class Application:
    def __init__(self, net):
        self.net = net

    def launch_game(self):
        game_window = GameWindow()
        game = Game()
        start_pos = (0, 0)
        player = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))

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

        self.net.close()
