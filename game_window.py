import time
from models import colors

import pygame


class GameWindow:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.win = None
        self.game = None
        self.set_window()

    def set_window(self):
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake for 2 players")

    def set_game_object(self, game):
        self.game = game

    def draw_player(self, player):
        for block in player.snake_body:
            pygame.draw.rect(self.win, player.color, [block.x,block.y,20,20])

    def draw_fruits(self,fruit):
        pygame.draw.rect(self.win, colors.blue, [fruit.x, fruit.y, 20, 20])
        #with graphic
        #self.win.blit(fruit.apple_image, (fruit.x, fruit.y))
    def redraw_window(self):
        self.win.fill((255, 255, 255))
        self.draw_player(self.game.player_one)
        self.draw_player(self.game.player_two)
        self.draw_fruits(self.game.fruits[0])
        self.draw_fruits(self.game.fruits[1])
        pygame.display.update()
    def draw_gameover(self):
        self.win.fill((0, 0, 0))
        self.font_style = pygame.font.SysFont(None, 50)
        mesg = self.font_style.render("Game Over", True, (255, 255, 255))
        self.win.blit(mesg, [self.width / 2 - 80, self.height / 2-50])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
