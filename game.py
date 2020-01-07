from models.player import Player
from models.fruit import Fruit

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.fruits = []

    def create_players(self):
        self.player_one = Player()
        self.player_two = Player()
    def create_fruits(self):
        self.fruits.append(Fruit())
        self.fruits.append(Fruit())

    def update(self):
        pass
