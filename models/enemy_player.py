import pygame
from models import colors
from models.block import block


class Player_enemy:
    def __init__(self, x=0, y=0, color=colors.black):

        self.color = color
        self.block_size = 20
        self.snake_body = []


        self.score = 0
        self.widthWindow = 500
        self.heightWindow = 500

    def update_position(self,vector):
        self.snake_body.clear
        for end in vector:
            self.snake_body.append(block(end[0],end[1]))
        print(vector)

    def check_fruitposition(self,fruits):
        for  fruit in fruits:
            # print(head + fruit.x + ' ' +  fruit.y)
            for block in self.snake_body:
                if(self.head.x==fruit.x) and (self.head.y == fruit.y):
                    self.score = self.score + 1
                    fruit.generate_position()





