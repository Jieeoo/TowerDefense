import pygame
import os
from Unit import Unit

imgs = []
for x in range(22):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Ent", "6_animation_walk_0" + add_str + ".png")), (64, 64)))

class Orc(Unit):
    def __init__(self):
        super() .__init__()
        self.max_health = 25
        self.health = self.max_health
        self.imgs = imgs[:]

