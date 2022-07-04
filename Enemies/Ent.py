import pygame
import os
from Unit import Unit

imgs = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Ent", "6_animation_walk_0" + add_str + ".png")), (80, 80)))

class Ent(Unit):
    def __init__(self):
        super() .__init__()
        self.name = "ent"
        self.money = 50
        self.max_health = 75
        self.vel=8
        self.health = self.max_health
        self.imgs = imgs[:]

