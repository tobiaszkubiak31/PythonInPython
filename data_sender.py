

class Sender:
    def __init__(self, net, game):
        self._running = True
        self.net = net
        self.game = game
        self.i = 0

    def send_data(self, data):
        self.net.send(str(data))

    def run(self):
        while self._running:
            data = self.game.player_one.get_position()
            self.send_data(data)

    def terminate(self):
        self._running = False
