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
        pygame.display.set_caption("Some Amazing Game")

    def set_game_object(self, game):
        self.game = game

    def draw_player(self, player):
        pygame.draw.rect(self.win, player.color, player.rect)

    def draw_fruits(self):
        pass

    def redraw_window(self):
        self.win.fill((255, 255, 255))
        self.draw_player(self.game.player_one)
        self.draw_player(self.game.player_two)
        # self.draw_fruits()
        pygame.display.update()
