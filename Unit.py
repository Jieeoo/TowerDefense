import pygame
import math
class Unit:
    imgs = []

    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(1187, 146), (400, 141), (394, 325), (882, 341), (878, 537), (160, 517), (132, 155)]
        self.img = None
        self.path_pos = 0
    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.animation_count +=1
        self.img = self.imgs[self.animation_count]
        ff

        if self.animation_count >= len(self.imgs):
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

    def move(self,change):
        """
        Move enemy
        :return: None
        """
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path)
            x2, y2 =(-10, 155)
        else:
            x2, y2 =self.path[self.path_pos+1]
        """37:18"""


        math.tan(change_y/change_x)

        slope = (y2 -y1) / (x2 -x1)
        move_y = slope*change + y2

    def hit(self):
        """
        Returns if a enemy has died and removes one health each call
        :return:Bool
        """

        self.health -=1
        if self.health <= 0:
            return True