from models import colors
from models.enemy_player import Player_enemy
from models.fruit import Fruit
from models.player import Player


class Game:
    def __init__(self):
        self.player_one = None
        self.player_enemy = None
        self.fruits = []

    def create_players(self):
        self.player_one = Player()
        self.player_enemy = Player_enemy()

    def create_fruits(self):
        self.fruits.append(Fruit())
    def append_enemy_fruit(self,fruit_cord):
        self.fruits = self.fruits[:1]
        fruit = Fruit()
        fruit.x = fruit_cord[0]
        fruit.y = fruit_cord[1]
        self.fruits.append(fruit)


    def update(self):
        pass


