import pygame

from models.fruit import Fruit
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
        pygame.init
        self.game_window = GameWindow()

        self.game = Game()

        self.game_window.set_game_object(self.game)
        self.game.create_players()
        self.game.create_fruits()

    def launch_game(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False




            self.game.player_one.move()

            self.game.player_one.check_collision_with_self()
            self.game.player_one.check_boundaries()
           # self.game.player_one.check_collision_with_player(self.game.player_enemy)

            self.game.player_one.check_fruitposition(self.game.fruits)
            self.update_game()

            if(self.game.player_enemy.game_over == True):
                self.update_game()
                self.game_window.draw_you_win()
            if (self.game.player_one.game_over == True):
                self.update_game()
                self.game_window.draw_gameover()

            self.game_window.redraw_window()


        self.net.close()

    def update_game(self):
        player_lost_flag = self.game.player_one.game_over
        player_vector = self.game.player_one.get_vector()
        player_color_flag = self.game.player_one.color
        fruit = self.game.fruits[0]
        fruit_cord = (fruit.x,fruit.y)

        data_to_send = player_vector, player_lost_flag, player_color_flag,fruit_cord

        self.send_data(data_to_send)

        data_received = self.receive_data()
        received_player_vector = data_received[0]
        received_player_lost_flag = data_received[1]
        received_player_color = data_received[2]
        received_fruit = data_received[3]

        self.game.player_enemy.update_position(received_player_vector)
        self.game.player_enemy.gameover = received_player_lost_flag
        self.game.player_enemy.color = received_player_color
        self.game.append_enemy_fruit(received_fruit)


    def send_data(self, data):
        self.net.send(str(data))

    def receive_data(self):
        data = self.net.recv()
        data = data.split('\n')[0]
        try:
            x, y , z , w= make_tuple(data)
            # print(x, y)
            return x, y, z , w
        except SyntaxError:
            return self.game.player_one.get_vector()


    def establish_network(self, ip="localhost", port=5555):
        self.net = Network(ip=ip, port=port)
        self.net.start()
        Thread(target=self.net.accept).start()

    def connect_to_peer(self, ip, port):
        self.net.connect(ip=ip, port=port)

    def set_snake_color(self, color):
        self.game.player_one.color = color
    def set_snake_position(self,x,y):
        self.game.player_one.init_body(x,y)
    def snake_init_body(self):
        self.game.player_one.init_body()


