import random


class Fruit:
    def __init__(self):
        lenght_widthx = 480
        lenght_widthy = 480
        self.x  = round(random.randrange(0, lenght_widthx) / 10.0) * 10.0
        self.y = round(random.randrange(0, lenght_widthy) / 10.0) * 10.0
