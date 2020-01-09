import pygame


class Fruit:
    def __init__(self, x, y):
        self.apple_image = pygame.image.load('graphics/apple.png')
        self.apple_image = pygame.transform.scale(self.apple_image, (20, 20))
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y
