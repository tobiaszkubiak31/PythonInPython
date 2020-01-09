import pygame
from models import colors
from models.block import Block


class Player:
    def __init__(self):
        self.color = colors.black
        self.block_size = 20
        self.direction = 2
        self.body_length = 4
        self.snake_body = []

        self.snake_top = None
        self.snake_turn_pic = None
        self.snake_straight = None
        self.snake_end = None
        self.load_snake_pics()

    def init_body(self, x, y):
        for i in range(self.body_length):
            self.snake_body = [Block(x, y)] + self.snake_body
            x += self.block_size

    def load_snake_pics(self):
        self.snake_top = pygame.image.load('graphics/snake_top.png')
        self.snake_top = pygame.transform.scale(self.snake_top, (20, 20))
        self.snake_top = pygame.transform.scale(self.snake_top, (20, 20))
        self.snake_turn_pic = pygame.image.load('graphics/snake_angle_left.png')
        self.snake_turn_pic = pygame.transform.scale(self.snake_turn_pic, (20, 20))
        self.snake_straight = pygame.image.load('graphics/snake_straight.png')
        self.snake_straight = pygame.transform.scale(self.snake_straight, (20, 20))
        self.snake_end = pygame.image.load('graphics/snake_end.png')
        self.snake_end = pygame.transform.scale(self.snake_end, (20, 20))

    def move_forward(self):
        if self.direction == 1:
            self.snake_body.pop()
            self.snake_body = [Block(self.snake_body[0].x - self.block_size, self.snake_body[0].y)] + self.snake_body

        if self.direction == 2:
            self.snake_body.pop()
            self.snake_body = [Block(self.snake_body[0].x + self.block_size, self.snake_body[0].y)] + self.snake_body

        if self.direction == 3:
            self.snake_body.pop()
            self.snake_body = [Block(self.snake_body[0].x, self.snake_body[0].y - self.block_size)] + self.snake_body

        if self.direction == 4:
            self.snake_body.pop()
            self.snake_body = [Block(self.snake_body[0].x, self.snake_body[0].y + self.block_size)] + self.snake_body

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.direction != 2:
            self.direction = 1
            self.move_forward()

        if keys[pygame.K_RIGHT] and self.direction != 1:
            self.direction = 2
            self.move_forward()

        if keys[pygame.K_UP] and self.direction != 4:
            self.direction = 3
            self.move_forward()

        if keys[pygame.K_DOWN] and self.direction != 3:
            self.direction = 4
            self.move_forward()
        
    def eat(self):
        self.snake_body.append(self.snake_body[-1].copy())
        self.body_length += 1

    def get_player_vector(self):
        vector = []
        for block in self.snake_body:
            vector.append((block.x, block.y))
        return vector

    def set_body(self, vector):
        self.snake_body = []
        for v in vector:
            self.snake_body.append(Block(v[0], v[1]))
