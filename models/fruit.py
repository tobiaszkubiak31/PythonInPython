import random

import pygame

class Fruit:
    def __init__(self):
        # self.apple_image = pygame.image.load('fruit.jpg')
        self.lenght_widthx = 480
        self.lenght_widthy = 480
        self.x  = round(random.randrange(0, self.lenght_widthx) / 20.0) * 20.0
        self.y = round(random.randrange(0, self.lenght_widthy) / 20.0) * 20.0
    def generate_position(self):
        self.x = round(random.randrange(0, self.lenght_widthx) / 20.0) * 20.0
        self.y = round(random.randrange(0, self.lenght_widthy) / 20.0) * 20.0