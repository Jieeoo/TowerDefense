import pygame
from .Tower import Tower
import os
import math
from Menu.menu import Menu

menu_bg= pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","menu.png")), (200,100))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","upgrade.png")), (50,50))
delete_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","delete.png")),(50,50))

class AttackTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_imgs=[]
        self.trop_imgs =[]
        self.width=0
        self.height=0
        self.animation_count = 0
        self.range = 0
        self.original_range = 0
        self.inRange = False
        self.left= False
        self.damage = 0
        self.moving = False
        self.original_damage = 0
        self.price=[1,1,1]
        self.menu = Menu(self, self.x, self.y, menu_bg, [1250, 2500, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(delete_btn,"delete")
        self.name = ""

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win,pause):
        super().draw_radius(win)
        super().draw(win)
        if self.animation_count >= len(self.trop_imgs):
            self.animation_count = 0

        if self.inRange and not self.moving and not pause:
            self.animation_count += 1
            if self.animation_count >= len(self.trop_imgs):
                self.animation_count = 0
        else:
            self.animation_count = 0
        character = self.trop_imgs[self.animation_count]
        if self.left == True:
            add = -25
        else:
            add = character.get_width() / 2
        win.blit(character, ((self.x) - (character.get_width() / 2), (self.y - character.get_height())))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.pos[0]
            y = enemy.pos[1]

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.animation_count == 8:

                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money
                    enemies.remove(first_enemy)

            if first_enemy.pos[0] < self.x and not (self.left):
                self.left = True
                for x, img in enumerate(self.trop_imgs):
                    self.trop_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.pos[0] > self.x:
                self.left = False
                for x, img in enumerate(self.trop_imgs):
                    self.trop_imgs[x] = pygame.transform.flip(img, True, False)
        return money
