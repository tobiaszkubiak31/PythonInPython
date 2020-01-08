import pygame
from models import colors
from models.block import block


class Player:
    def __init__(self):
        self.color = colors.black
        self.block_size = 20
        self.direction = 2
        self.length = 2
        self.snake_body = []
        self.you_lost_flag = False
        self.score = 0
        self.widthWindow = 500
        self.heightWindow = 500


    def init_body(self,x,y):
        self.snake_body.append(block(x,y))
        self.snake_body.append(block(x + 20, y))
        self.snake_body.append(block(x + 40,y))
        self.head = block(x + 40, y)
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
        # print("x")
        # print(self.head.x)
        # print("y")
        # print(self.head.y)
        self.update()

    def update(self):
        #update head
        self.snake_body.append(block(self.head.x,self.head.y))
        if(self.score + 2>self.length):
            self.length = self.length + 1
            return
        del self.snake_body[0]
        print("snake body in update")
        print(self.snake_body)

    def get_vector(self):
        vector = []
        for block in self.snake_body:
            vector = vector + [(block.x,block.y)]

        return vector


    def check_boundaries(self):

        if(self.head.y > 500 or self.head.y < 0 or self.head.x > 500 or self.head.x < 0):
            self.you_lost_flag = True
            return True
        else:
            False
        #without collision to fix
        # for block in self.snake_body:
        #     if self.head.y < 0:
        #         self.head.y = 500
        #     if block.y < 0:
        #         block.y = 500
        #         return
        #
        #     if self.head.x < 0:
        #         self.head.x = 500
        #     if block.x < 0:
        #         block.x = 500
        #         return
        #
        #     if self.head.x >= self.widthWindow - 20:
        #         self.head.x = -20
        #     if block.x > self.widthWindow - 20:
        #         block.x = -20
        #         return
        #
        #     if self.head.y >= self.widthWindow - 20:
        #         self.head.y = -20
        #     if block.y > self.widthWindow - 20:
        #         block.y = -20
        #         return

    def check_collision_with_player(self,player):
        for block in player.snake_body[0:len(player.snake_body)]:
            if (self.head.y == block.x and self.head.y == block.y):
                self.you_lost_flag = True
                return True


    def check_collision_with_self(self):
        for  block in self.snake_body[0:len(self.snake_body)]:
            if ((self.head.x == block.x and self.head.y == block.y)):
                self.you_lost_flag = True
                return True
            else:
                return False

    def check_fruitposition(self,fruits):
        for  fruit in fruits:
            # print(head + fruit.x + ' ' +  fruit.y)
            for block in self.snake_body:
                if(self.head.x==fruit.x) and (self.head.y == fruit.y):
                    self.score = self.score + 1
                    fruit.generate_position()





