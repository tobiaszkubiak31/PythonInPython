import pygame
from game_window import GameWindow
from game import Game
from data_sender import Sender
from data_receiver import Receiver
from threading import Thread


class Application:
    def __init__(self, net):
        self.net = net

    def launch_game(self):
        game_window = GameWindow()
        game = Game()
        game_window.set_game_object(game)
        game.create_players()

        clock = pygame.time.Clock()

        sender = Sender(self.net, game)
        receiver = Receiver(self.net, game)
        sender_thread = Thread(target=sender.run)
        receiver_thread = Thread(target=receiver.run)
        sender_thread.start()
        receiver_thread.start()

        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False

            game.player_one.move()
            game_window.redraw_window()

        sender.terminate()
        receiver.terminate()
        self.net.close()
