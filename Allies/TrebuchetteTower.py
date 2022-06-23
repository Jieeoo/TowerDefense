import pygame
from .Tower import Tower
import os
import math
import time
from Menu.menu import Menu

menu_bg= pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","menu.png")), (200,100))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","upgrade.png")), (50,50))

tower_imgs = []
trebuchette_imgs = []
#load wizard towers images
for x in range(3):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower", "Tower" + str(x) + ".png")),
                               (90, 100)))
for x in range(9):
    add_str = str(x)
    trebuchette_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Tower_NPC/Trebuchette_imgs", "trebuchette_0" + str(x) + ".png")), (128, 128)))


class TrebuchetteTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=tower_imgs
        self.trebuchette_imgs =trebuchette_imgs
        self.trebuchette_count = 0
        self.range = 250
        self.original_range = self.range
        self.inRange = False
        self.left= False
        self.damage = 20
        self.original_damage = self.damage
        self.width=90
        self.height=100
        self.menu = Menu(self, self.x, self.y, menu_bg, [5000, 10000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.name = "catapulta"

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)
        if self.trebuchette_count >= len(self.trebuchette_imgs):
            self.trebuchette_count = 0

        if self.inRange:
            self.trebuchette_count += 1
            if self.trebuchette_count >= len(self.trebuchette_imgs):
                self.trebuchette_count = 0
        else:
            self.trebuchette_count = 0

        trebuchette = self.trebuchette_imgs[self.trebuchette_count]
        if self.left == True:
            add = -25
        else:
            add = trebuchette.get_width() / 2
        win.blit(trebuchette, ((self.x ) - (trebuchette.get_width() / 2), (self.y - trebuchette.get_height())))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
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
            if self.trebuchette_count == 8:

                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            if first_enemy.pos[0] < self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.trebuchette_imgs):
                    self.trebuchette_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.pos[0] > self.x:
                self.left = False
                for x, img in enumerate(self.trebuchette_imgs):
                    self.trebuchette_imgs[x] = pygame.transform.flip(img, True, False)
        return money