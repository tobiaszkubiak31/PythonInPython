class Block:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def position(self):
        return self.x, self.y

    def copy(self):
        return Block(self.x, self.y)
