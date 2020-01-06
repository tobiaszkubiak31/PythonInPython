import pygame
import colors

class Player:
    def __init__(self, x=0, y=0, width_snake_block=20, height_snake_block=20, color=colors.black):
        self.x = x
        self.y = y
        self.width_snake_block = width_snake_block
        self.height_snake_block = height_snake_block
        self.color = color
        self.rect = (x, y, width_snake_block, height_snake_block)
        self.speed = 1 #speed
        self.direction = 0;
        self.length = 3

        self.widthWindow = 500
        self.heightWindow = 500
    def draw(self, win):
        #:todo draw a lot of rects
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction = 1

        if keys[pygame.K_RIGHT]:
            self.direction = 2

        if keys[pygame.K_UP]:
            self.direction = 3

        if keys[pygame.K_DOWN]:
            self.direction = 4


        if self.direction == 1:
            self.x -= self.speed

        if self.direction == 2:
            self.x += self.speed

        if self.direction == 3:
            self.y -= self.speed

        if self.direction == 4:
            self.y += self.speed

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width_snake_block, self.height_snake_block)
    def checkCollision(self):
        if self.x >= self.widthWindow or self.x < 0 or self.y >= self.widthWindow or self.y < 0:
            return True
        else:
            False

    def check_fruitposition(self,fruits):
        #todo: implement after snake 
        print("got fruit")




