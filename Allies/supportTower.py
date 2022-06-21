import pygame
from .Tower import Tower
import os
import math
import time

range_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower","range_tower.png")),(85,90)),
                pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower","range_tower1.png")),(85,90))]

class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = range_imgs[:]
        self.effect = [0.2, 0.4]
        self.width=85
        self.height=90

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()


    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def support(self,towers):
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x-x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level -1])






damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "damage_tower.png")),(85,90)),
                pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "damage_tower1.png")),(85,90))]

class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs = damage_imgs[:]
        self.effect = [0.2,0.4]
        self.width=85
        self.height=90

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def support(self, towers):
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2 :
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.damage * self.effect[self.level -1])