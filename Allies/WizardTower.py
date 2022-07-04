import pygame
from .AttackTower import AttackTower
import os

tower_imgs = []
wizard_imgs = []
#load wizard towers images
for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(10):
    add_str = str(x)
    wizard_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Wizard_imgs", "Elf_03__ATTACK_00" + str(x) + ".png")), (256, 128)))


class WizardTower(AttackTower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs[:]
        self.trop_imgs =wizard_imgs[:]
        self.width=90
        self.height=100
        self.range = 150
        self.original_range = self.range
        self.damage = 15
        self.price=[300,500,1000]
        self.original_damage = self.damage
        self.name = "wizard"
