import time
import pygame
from models import colors


class GameWindow:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.win = None
        self.game = None
        self.set_window()
        self.block_size = block_size

    def set_window(self):
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake for 2 players")

    def set_game_object(self, game):
        self.game = game
        self.game.block_size = self.block_size

    def draw_checkerboard(self):
        for y in range(0, self.width, 2*self.block_size):
            for x in range(0, self.height, 2*self.block_size):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[0], [x, y, self.block_size, self.block_size])
            for x in range(self.block_size, self.height, 2*self.block_size):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[1], [x, y, self.block_size, self.block_size])
        for y in range(self.block_size, self.width, 2*self.block_size):
            for x in range(self.block_size, self.height, 2*self.block_size):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[0], [x, y, self.block_size, self.block_size])
            for x in range(0, self.height, 2*self.block_size):
                pygame.draw.rect(self.win, self.game.checkerboard_colors[1], [x, y, self.block_size, self.block_size])

    def draw_player(self, player):
        # for block in player.snake_body:
        #     pygame.draw.rect(self.win, player.color, [block.x, block.y, self.block_size, self.block_size])

        angle = 0
        if player.direction == 1:
            angle = 90
        elif player.direction == 2:
            angle = -90
        elif player.direction == 3:
            angle = 0
        elif player.direction == 4:
            angle = 180
        self.win.blit(pygame.transform.rotate(player.snake_top, angle),
                      player.snake_body[0].position())

        for i in range(1, len(player.snake_body)-1):
            if player.snake_body[i-1].x == player.snake_body[i].x and player.snake_body[i+1].x == player.snake_body[i].x:
                self.win.blit(pygame.transform.rotate(player.snake_straight, 90),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].y == player.snake_body[i].y and player.snake_body[i+1].y == player.snake_body[i].y:
                self.win.blit(pygame.transform.rotate(player.snake_straight, 0),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].x == player.snake_body[i].x and player.snake_body[i+1].x < player.snake_body[i].x and player.snake_body[i-1].y < player.snake_body[i].y:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, -90),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].x == player.snake_body[i].x and player.snake_body[i+1].x < player.snake_body[i].x and player.snake_body[i-1].y > player.snake_body[i].y:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 0),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].x == player.snake_body[i].x and player.snake_body[i+1].x > player.snake_body[i].x and player.snake_body[i-1].y < player.snake_body[i].y:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 180),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].x == player.snake_body[i].x and player.snake_body[i+1].x > player.snake_body[i].x and player.snake_body[i-1].y > player.snake_body[i].y:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 90),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].y == player.snake_body[i].y and player.snake_body[i+1].x == player.snake_body[i].x and player.snake_body[i-1].y > player.snake_body[i+1].y and player.snake_body[i-1].x < player.snake_body[i+1].x:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, -90),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].y == player.snake_body[i].y and player.snake_body[i+1].x == player.snake_body[i].x and player.snake_body[i-1].y < player.snake_body[i+1].y and player.snake_body[i-1].x > player.snake_body[i+1].x:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 90),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].y == player.snake_body[i].y and player.snake_body[i+1].x == player.snake_body[i].x and player.snake_body[i-1].y < player.snake_body[i+1].y and player.snake_body[i-1].x < player.snake_body[i+1].x:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 0),
                              player.snake_body[i].position())
            elif player.snake_body[i-1].y == player.snake_body[i].y and player.snake_body[i+1].x == player.snake_body[i].x and player.snake_body[i-1].y > player.snake_body[i+1].y and player.snake_body[i-1].x > player.snake_body[i+1].x:
                self.win.blit(pygame.transform.rotate(player.snake_turn_pic, 180),
                              player.snake_body[i].position())
            else:
                pygame.draw.rect(self.win, player.color, [player.snake_body[i].x, player.snake_body[i].y, self.block_size, self.block_size])

        if player.snake_body[-2].x < player.snake_body[-1].x:
            angle = -90
        elif player.snake_body[-2].y < player.snake_body[-1].y:
            angle = 180
        elif player.snake_body[-2].x > player.snake_body[-1].x:
            angle = 90
        else:
            angle = 0

        self.win.blit(pygame.transform.rotate(player.snake_end, angle), player.snake_body[-1].position())

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


