import pygame
from models import colors
from models.block import block


class Player:
    def __init__(self, x=0, y=0, color=colors.black):
        self.head = block(0,0)
        self.color = color
        self.block_size = 20
        self.direction = 0;
        self.length = 2
        self.snake_body = []
        self.snake_body.append(block(x,y))
        self.snake_body.append(block(x+20,y))

        self.score = 0
        self.widthWindow = 500
        self.heightWindow = 500


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
            self.head.x -= self.block_size

        if self.direction == 2:
            self.head.x += self.block_size

        if self.direction == 3:
            self.head.y -= self.block_size

        if self.direction == 4:
            self.head.y += self.block_size

        self.update()

    def update(self):
        #update head
        self.snake_body.append(block(self.head.x,self.head.y))
        if(self.score + 2>self.length):
            self.length = self.length + 1
            return
        del self.snake_body[0]

    def check_collision_boundaries(self):
        if self.head.x+20 >= self.widthWindow or self.head.x < 0 or self.head.y >= self.widthWindow-20 or self.head.y < 0:
            return True
        else:
            False

    def collision_with_self(self):
        for  block in self.snake_body[0:len(self.snake_body)]:
            if ((self.head.x >= block.x and self.head.x <= block.x + 20)
                and
                (self.head.y >= block.y and self.head.y <= block.y + 20)):
                return True
            else:
                False

    def check_fruitposition(self,fruits):
        for  fruit in fruits:
            print(fruit.x)
            print(fruit.y)
            # print(head + fruit.x + ' ' +  fruit.y)
            for block in self.snake_body:
                if((block.x>=fruit.x and block.x<=fruit.x+20) and (block.y>=fruit.y and block.y<=fruit.y+20)):
                    self.score = self.score + 1
                    fruit.generate_position()





