from models.block import Block
from models.fruit import Fruit
from models.player import Player
import random


class Game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.fruit = None
        self.enemy_fruit = None
        self.checkerboard_colors = ()
        self.map_width = None
        self.map_height = None
        self.game_over = False
        self.you_won = False
        self.block_size = 40

    def set_checkerboard_colors(self, color1, color2):
        self.checkerboard_colors = (color1, color2)

    def set_map_size(self, width, height):
        self.map_width = width
        self.map_height = height

    def create_players(self):
        self.player = Player()
        self.player.block_size = self.block_size
        self.player.load_snake_pics()
        self.enemy = Player()
        self.enemy.block_size = self.block_size
        self.enemy.load_snake_pics()

    def spawn_fruit(self):
        x = random.randrange(0, self.map_width) // self.block_size * self.block_size
        y = random.randrange(0, self.map_height) // self.block_size * self.block_size
        self.fruit = Fruit(x, y, self.block_size)

    def check_for_collisions(self):
        self.check_fruit_collision()
        self.check_player_collision()
        self.check_boundary_collision()
        self.check_with_enemy_collision()

    def check_with_enemy_collision(self):
        for block in self.enemy.snake_body:
            if self.player.snake_body[0].position() == block.position():
                self.game_over = True

    def check_player_collision(self):
        for i in range(1, len(self.player.snake_body)):
            print(self.player.snake_body[0].position(), self.player.snake_body[i].position())
            if self.player.snake_body[0].position() == self.player.snake_body[i].position():
                self.game_over = True

    def check_boundary_collision(self):
        if self.player.snake_body[0].x > self.map_width:
            self.game_over = True

        if self.player.snake_body[0].x < 0:
            self.game_over = True

        if self.player.snake_body[0].y > self.map_height:
            self.game_over = True

        if self.player.snake_body[0].y < 0:
            self.game_over = True

    def check_fruit_collision(self):
        if self.fruit is not None and self.fruit is not False \
                and self.player.snake_body[0].position() == self.fruit.position():
            self.player.eat()
            self.fruit = False
        if self.enemy_fruit is not None and self.enemy_fruit is not False \
                and self.player.snake_body[0].position() == self.enemy_fruit.position():
            self.player.eat()
            self.enemy_fruit = False

    # def get_fruit_vector(self):
    #     vector = []
    #     for f in self.fruits:
    #         vector.append(f.position())
    #     return vector
    #
    # def set_fruits(self, vector):
    #     self.fruits = []
    #     for v in vector:
    #         self.fruits.append(Block(v[0], v[1]))
