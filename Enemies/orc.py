import pygame
import os
from Unit import Unit

imgs = []
for x in range(7):
    add_str = str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Orc", "WALK_00" + add_str + ".png")), (64, 64)))

class Orc(Unit):
    def __init__(self):
        super() .__init__()
        self.name = "orc"
        self.money = 20
        self.max_health = 50
        self.health = self.max_health
        self.imgs = imgs[:]


