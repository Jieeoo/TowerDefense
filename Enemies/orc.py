import pygame
import os
from Unit import Unit

class Orc(Unit):
    imgs = []
    for x in range(7):
        add_str = str(x)
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/Orc","WALK_00"+add_str+".png")),(64,64)))

