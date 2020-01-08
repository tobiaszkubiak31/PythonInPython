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
        self.fruits.append(Fruit())

    def update(self):
        pass


