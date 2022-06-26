import pygame
from .AttackTower import AttackTower
import os

tower_imgs = []
archer_imgs = []
#load archer towers images
for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(10):
    add_str = str(x)
    archer_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Archer_imgs", "Elf_01__ATTACK_00" + str(x) + ".png")), (256, 128)))


class ArcherTower(AttackTower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs[:]
        self.trop_imgs =archer_imgs[:]
        self.range = 200
        self.original_range = self.range
        self.damage = 10
        self.original_damage = self.damage
        self.width = 90
        self.height = 90
        self.name = "archer"
