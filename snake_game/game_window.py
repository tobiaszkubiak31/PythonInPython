import time
import pygame
from models import colors


class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = None
        self.game = None
        self.set_window()

    def set_window(self):
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake for 2 players")

    def set_game_object(self, game):
        self.game = game

    def draw_checkerboard(self):
        for y in range(0, 500, 40):
            for x in range(0, 500, 40):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[0], [x, y, 20, 20])
            for x in range(20, 500, 40):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[1], [x, y, 20, 20])
        for y in range(20, 500, 40):
            for x in range(20, 500, 40):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[0], [x, y, 20, 20])
            for x in range(0, 500, 40):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[1], [x, y, 20, 20])

    def draw_player(self, player):
        for block in player.snake_body:
            pygame.draw.rect(self.win, player.color, [block.x, block.y, 20, 20])
            # self.win.blit(self.game.player.snake_straight, (block.x, block.y))

    def draw_fruits(self):
        fruit = self.game.fruit
        if fruit is not None and fruit is not False:
            # pygame.draw.rect(self.win, colors.blue, [fruit.x, fruit.y, 20, 20])
            self.win.blit(fruit.apple_image, (fruit.x, fruit.y))
        enemy_fruit = self.game.enemy_fruit
        if enemy_fruit is not None and enemy_fruit is not False:
            # pygame.draw.rect(self.win, colors.blue, [enemy_fruit.x, enemy_fruit.y, 20, 20])
            self.win.blit(enemy_fruit.apple_image, (enemy_fruit.x, enemy_fruit.y))

    def redraw_window(self):
        # self.win.fill((255, 255, 255))
        self.draw_checkerboard()
        self.draw_fruits()
        self.draw_player(self.game.player)
        self.draw_player(self.game.enemy)
        pygame.display.update()

    def draw_gameover(self):
        # pygame.init()
        self.win.fill((0, 0, 0))
        self.font_style = pygame.font.SysFont(None, 50)
        mesg = self.font_style.render("Game Over", True, (255, 255, 255))
        self.win.blit(mesg, [self.width / 2 - 80, self.height / 2 - 50])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()

    def draw_you_win(self):
        # pygame.init()
        self.win.fill((0, 0, 0))
        self.font_style = pygame.font.SysFont(None, 50)
        mesg = self.font_style.render("You Win", True, (255, 255, 255))
        self.win.blit(mesg, [self.width / 2 - 80, self.height / 2 - 50])
        pygame.display.update()
        time.sleep(5)
        pygame.quit()


