from ast import literal_eval as make_tuple


class Receiver:
    def __init__(self, net, game):
        self._running = True
        self.net = net
        self.game = game

    def receive_data(self):
        return self.net.recv()

    def run(self):
        while self._running:
            data = self.receive_data()
            data = data.split('\n')[0]
            try:
                x, y = make_tuple(data)
                # print(x, y)
            except SyntaxError:
                continue
            self.game.player_two.set_position(x, y)
            self.game.player_two.update()

    def terminate(self):
        self._running = False
