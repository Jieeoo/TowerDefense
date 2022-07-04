import pygame
import os
from Unit import Unit

imgs = []
for x in range(10):
    add_str = str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Troll", "Troll_01_1_WALK_00" + add_str + ".png")), (100,100 )))
class Troll(Unit):
    def __init__(self):
        super() .__init__()
        self.name = "troll"
        self.money = 100
        self.max_health = 200
        self.vel=5
        self.health = self.max_health
        self.imgs = imgs[:]
        self.alt = -30