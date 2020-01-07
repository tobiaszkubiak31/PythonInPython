import pygame
from snake_game.game_window import GameWindow
from snake_game.game import Game
from ast import literal_eval as make_tuple
from network.network import Network
from threading import Thread


class Application:
    def __init__(self):
        self.net = None
        self.game = None
        self.game_window = None

    def set_environment(self):
        self.game_window = GameWindow()
        self.game = Game()

        self.game_window.set_game_object(self.game)
        self.game.create_players()

    def launch_game(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

            self.update_game()

            self.game_window.redraw_window()

        self.net.close()

    def update_game(self):
        self.game.player_one.move()

        data_to_send = self.game.player_one.get_position(), self.game.player_one.color
        self.send_data(data_to_send)

        data_received = self.receive_data()
        x, y = data_received[0]
        color = data_received[1]
        self.game.player_two.set_position(x, y)
        self.game.player_two.color = color

    def send_data(self, data):
        self.net.send(str(data))

    def receive_data(self):
        data = self.net.recv()
        data = data.split('\n')[0]
        try:
            x, y = make_tuple(data)
            # print(x, y)
            return x, y
        except SyntaxError:
            return self.game.player_two.get_position()

    def set_snake_color(self, color):
        self.game.player_one.color = color

    def establish_network(self, ip="localhost", port=5555):
        self.net = Network(ip=ip, port=port)
        self.net.start()
        Thread(target=self.net.accept).start()

    def connect_to_peer(self, ip, port):
        self.net.connect(ip=ip, port=port)
