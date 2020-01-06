import pygame


class Player:
    def __init__(self, x=0, y=0, width=20, height=20, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
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
        self.rect = (self.x, self.y, self.width, self.height)
    def checkCollision(self):
        if self.x >= self.widthWindow or self.x < 0 or self.y >= self.widthWindow or self.y < 0:
            return True
        else:
            False


