from player import Player


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.fruits = []

    def create_players(self):
        self.player_one = Player()
        self.player_two = Player()

    def update(self):
        pass
