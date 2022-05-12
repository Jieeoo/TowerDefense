import pygame
from .Tower import Tower
import os
import math

class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=[]
        self.archer_imgs =[]
        self.archer_count = 0
        self.range = 200
        self.inRange = False
        self.left=False

        for x in range(3):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")), (90, 100)))
        for x in range(22):
            add_str= str(x)
            if x < 10:
                add_str = "0" + add_str
            self.archer_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Shoot_Stand", "shoot_stand_0" + add_str + ".png")), (32, 32)))

    def draw(self, win):
        surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA,32)
        pygame.draw.circle(surface, (128,128,128,100),(self.range,self.range),self.range,0)

        win.blit(surface, (self.x-self.range, self.y-self.range))
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs):
            self.archer_count = 0

        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs):
                self.archer_count = 0
        else:
            self.archer_count =0

        archer = self.archer_imgs[self.archer_count]
        if self.left == True:
            add = -25
        else:
            add = a-archer.get_width()/2
        win.blit(archer,((self.x + self.width / 2) - (archer.get_width() / 2), (self.y - archer.get_height() - 25)))

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

            if first_enemy.pos[0] > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img,True,False)
            elif self.left and first_enemy.pos[0] < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
