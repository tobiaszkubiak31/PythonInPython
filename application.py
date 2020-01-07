import time

import pygame
from game_window import GameWindow
from game import Game


class Application:
    def __init__(self, net):
        self.net = net


    def launch_game(self):
        pygame.init()  # now use display and fonts
        game_window = GameWindow()
        game = Game()
        game_window.set_game_object(game)
        game.create_players()
        game.create_fruits()

        clock = pygame.time.Clock()


        run = True
        while run:

            clock.tick(10)

            # while 1:
            #     clock.tick(500)
            #     self.net.send("hello")
            #     self.net.recv

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            if(game.player_one.check_collision_boundaries()):
                print("you lost")
                break

            game.player_one.move()
            game.player_one.check_fruitposition(game.fruits)
            game_window.redraw_window()

        game_window.draw_gameover()
        self.net.close()
