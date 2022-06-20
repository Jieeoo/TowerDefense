import pygame
from .Tower import Tower
import os
import math
import time

tower_imgs = []
wizard_imgs = []
#load wizard towers images
for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(10):
    add_str = str(x)
    wizard_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Wizard_imgs", "Elf_03__ATTACK_00" + str(x) + ".png")), (256, 128)))


class WizardTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs
        self.wizard_imgs =wizard_imgs
        self.width=90
        self.height=100
        self.wizard_count = 0
        self.range = 150
        self.original_range = self.range
        self.inRange = False
        self.left= False
        self.damage = 15
        self.original_damage = self.damage


    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)
        if self.wizard_count >= len(self.wizard_imgs):
            self.wizard_count = 0

        if self.inRange:
            self.wizard_count += 1
            if self.wizard_count >= len(self.wizard_imgs):
                self.wizard_count = 0
        else:
            self.wizard_count = 0

        wizard = self.wizard_imgs[self.wizard_count]
        if self.left == True:
            add = -25
        else:
            add = wizard.get_width() / 2
        win.blit(wizard, ((self.x ) - (wizard.get_width() / 2), (self.y - wizard.get_height())))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.pos[0]
            y = enemy.pos[1]

            dis = math.sqrt((self.x -x)**2 + (self.y - y)**2)
            if dis < self.range:
                print(dis)
                self.inRange =True
                enemy_closest.append(enemy)
        enemy_closest.sort(key=lambda x: x.x)
        if len(enemy_closest)>0:
            first_enemy = enemy_closest[0]
            if self.wizard_count == 9:

                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)

            if first_enemy.pos[0] < self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.wizard_imgs):
                    self.wizard_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.pos[0] > self.x:
                self.left = False
                for x, img in enumerate(self.wizard_imgs):
                    self.wizard_imgs[x] = pygame.transform.flip(img, True, False)
