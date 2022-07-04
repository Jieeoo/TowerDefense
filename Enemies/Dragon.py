import pygame
import os
from Unit import Unit

imgs = []
for x in range(3):
    add_str = str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Dragon", "Dragon_00" + add_str + ".png")), (80, 80)))

class Dragon(Unit):
    def __init__(self):
        super() .__init__()
        self.name = "Dragon"
        self.money = 50
        self.max_health = 200
        self.vel=25
        self.health = self.max_health
        self.imgs = imgs[:]