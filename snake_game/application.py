import pygame

from snake_game.game_window import GameWindow
from snake_game.game import Game
from models.fruit import Fruit
from ast import literal_eval as make_tuple
from network.network import Network
from threading import Thread


class Application:
    def __init__(self):
        self.net = None
        self.game = None
        self.game_window = None

    def set_environment(self):
        pygame.init()
        self.game_window = GameWindow(width=900, height=900, block_size=30)
        self.game = Game()

        self.game_window.set_game_object(self.game)
        self.game.set_map_size(self.game_window.width, self.game_window.height)

        self.game.create_players()
        self.game.spawn_fruit()

        color1 = (90, 240, 90)
        color2 = (80, 220, 80)
        self.game.set_checkerboard_colors(color1, color2)

    def launch_game(self):
        clock = pygame.time.Clock()

        counter = 0
        run = True
        while run:
            clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

            self.game.check_for_collisions()

            if counter % 60 == 0:
                self.game.player.move_forward()

            if counter % 10 == 0:
                self.game.player.move()

            self.update_game()

            if self.game.game_over:
                self.game_window.draw_gameover()
            if self.game.you_won:
                self.game_window.draw_you_win()

            self.game_window.redraw_window()

            counter += 1

        self.net.close()

    def update_game(self):
        player_lost_flag = self.game.game_over
        player_vector = self.game.player.get_player_vector()
        player_color_flag = self.game.player.color
        fruit1 = self.game.fruit.position() if isinstance(self.game.fruit, Fruit) else self.game.fruit
        fruit2 = self.game.enemy_fruit.position() if isinstance(self.game.enemy_fruit, Fruit) else self.game.enemy_fruit
        direction = self.game.player.direction

        data_to_send = player_vector, player_lost_flag, player_color_flag, fruit1, fruit2, direction

        self.send_data(data_to_send)

        data_received = self.receive_data()
        if data_received is None:
            return

        received_player_vector = data_received[0]
        received_player_lost_flag = data_received[1]
        received_player_color = data_received[2]
        received_enemy_fruit = data_received[3]
        received_fruit = data_received[4]
        received_direction = data_received[5]

        self.game.enemy_fruit = received_enemy_fruit

        if received_enemy_fruit is not False:
            self.game.enemy_fruit = Fruit(*received_enemy_fruit, self.game.block_size)

        if received_fruit is False:
            self.game.spawn_fruit()

        self.game.enemy.set_body(received_player_vector)
        self.game.you_won = received_player_lost_flag
        self.game.enemy.color = received_player_color
        self.game.enemy.direction = received_direction

    def send_data(self, data):
        self.net.send(str(data))

    def receive_data(self):
        data = self.net.recv()
        data = data.split('\n')[0]
        try:
            return make_tuple(data)
        except SyntaxError:
            return None

    def establish_network(self, ip="localhost", port=5555):
        self.net = Network(ip=ip, port=port)
        self.net.start()
        Thread(target=self.net.accept).start()

    def connect_to_peer(self, ip, port):
        self.net.connect(ip=ip, port=port)

    def set_snake_color(self, color):
        self.game.player.color = color

    def set_snake_position(self, x, y):
        self.game.player.init_body(x, y)
