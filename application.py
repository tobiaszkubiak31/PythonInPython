import pygame
from game_window import GameWindow
from game import Game


class Application:
    def __init__(self, net):
        self.net = net

    def launch_game(self):
        game_window = GameWindow()
        game = Game()
        game_window.set_game_object(game)
        game.create_players()

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

            game.player_one.move()
            game_window.redraw_window()

        self.net.close()
