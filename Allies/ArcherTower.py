import pygame
from .Tower import Tower
import os
import math
import time

tower_imgs = []
archer_imgs = []
#load archer towers images
for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(10):
    add_str = str(x)
    archer_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Archer_imgs", "Elf_01__ATTACK_00" + str(x) + ".png")), (256, 128)))


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs
        self.archer_imgs =archer_imgs
        self.archer_count = 0
        self.range = 200
        self.inRange = False
        self.left= False
        self.damage = 20


    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs):
            self.archer_count = 0

        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs):
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count]
        if self.left == True:
            add = -25
        else:
            add = archer.get_width()/2
        win.blit(archer,((self.x + self.width / 2) - (archer.get_width() / 2), (self.y - archer.get_height())))

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
            if self.archer_count == 9:

                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)

            if first_enemy.pos[0] < self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img,True,False)
            elif self.left and first_enemy.pos[0] > self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)


