import pygame
from .Tower import Tower
import os
import math
import time

range_imgs = [pygame.image.load(os.path.join("game_assets/Tower","range_tower.png")),
               pygame.image.load(os.path.join("game_assets/Tower","range_tower1.png"))]

class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = range_imgs[:]
        self.effect = [0.2, 0.4]

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def support(self,towers):
        pass




damage_imgs = [pygame.image.load(os.path.join("game_assets/Tower", "damage_tower.png")),
                pygame.image.load(os.path.join("game_assets/Tower", "damage_tower1.png"))]

class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = damage_imgs[:]
        self.effect = [1,2]

    def support(self, towers):
        pass
