import pygame


class Fruit:
    def __init__(self, x, y, block_size):
        self.apple_image = pygame.image.load('graphics/apple.png')
        self.apple_image = pygame.transform.scale(self.apple_image, (block_size, block_size))
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y
