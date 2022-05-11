import pygame
import math
class Unit:
    imgs = []

    def __init__(self):
        self.widht = 32
        self.height = 32
        self.animation_count = 0
        self.health = 1
        self.vel = 1
        self.path = [(1187, 146), (400, 141), (394, 325), (882, 341), (878, 537), (160, 517), (132, 155)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count =0
        self.move_dis = 0
        self.dis=0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """

        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1

        if self.animation_count >= len(self.imgs)*3:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, x, y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <=self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        
        """Move enemy
        :return: None

        """
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10,155)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis=math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.move_count += 1

        dirn = (x2-x1, y2-y1)

        move_x, move_y = (self.x + dirn[0] * self.move_count,self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False

        self.x = move_x
        self.y = move_y
        return True
    def hit(self):
        """
        Returns if a enemy has died and removes one health each call
        :return:Bool
        """

        self.health -=1
        if self.health <= 0:
            return True