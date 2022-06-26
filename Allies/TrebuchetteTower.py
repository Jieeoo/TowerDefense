import pygame
from .AttackTower import AttackTower
import os


tower_imgs = []
trebuchette_imgs = []

for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(9):
    add_str = str(x)
    trebuchette_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Trebuchette_imgs", "trebuchette_0" + str(x) + ".png")), (128, 128)))


class TrebuchetteTower(AttackTower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs[:]
        self.trop_imgs =trebuchette_imgs[:]
        self.range = 250
        self.original_range = self.range
        self.damage = 20
        self.original_damage = self.damage
        self.width=90
        self.height=100
        self.name = "trebuchette"

