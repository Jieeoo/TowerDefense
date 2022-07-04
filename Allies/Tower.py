import pygame
from Menu.menu import Menu
import os
import math

menu_bg= pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","menu.png")), (200,100))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","upgrade.png")), (50,50))
delete_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","delete.png")),(50,50))
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        #define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_bg, [1500, "MAX"])
        self.menu.add_btn(upgrade_btn,"Upgrade")
        self.menu.add_btn(delete_btn,"delete")
        self.tower_imgs = []
        self.damage = 1
        self.place_color = (0,255,0,100)

        self.delet=False



    def draw(self, win):

        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        #Draw menu
        if self.selected:
            self.menu.draw(win)


    def draw_radius(self, win):
        if self.selected:
            #draw range radious
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self, win):

        #draw range radious
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (64, 64), 64, 0)

        win.blit(surface, (self.x-64, self.y-64))


    def click(self, X, Y):
        """
        return if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y:int
        :return:bool
        """
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False



    def upgrade(self):
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage = self.damage*1.2


    def get_ugrade_cost(self):
        return self.price[self.level - 1]

    def get_delete_sell(self):
        return self.price[self.level-1]

    def move(self, x, y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        width = otherTower.width
        height = otherTower.height
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((((x2+width/2) - (self.x+self.width/2))**2 + ((y2+height) -(self.y+self.height))**2))
        if dis >= 128:
            return False
        else:
            return True






