import pygame
import os
pygame.font.init
coin = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu", "coin.png")),(40,40))
class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def click(self, X, Y):
        """
        Devuelve si la posición tiene colisión con el menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x +self.width and X >= self.x:
            if Y <= self.y +self.height and Y >=self.y:
                return True
        return False
    def draw(self, win):
        win.blit(self.img, (self.x,self.y))
class Menu:
    """
    menu para selecionar items
    """
    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans",20)
        self.tower = tower

    def add_btn(self, img, name):
        """
        añade botones al menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        btn_x = self.x - self.bg.get_width() / 2 + 30
        if self.y > 140:
            btn_y= self.y - 130
        else:
            btn_y = self.y +25
        self.buttons.append(Button(btn_x,btn_y,img,name))

    def get_item_cost(self):
        """
        gets cost of upgrade to next level
        :return: int
        """
        return self.item_cost[self.tower.level-1]

    def draw(self, win):
        """
        dibuja botones y menu
        :param win:surface
        :return: None
        """
        if self.y > 140:
            win.blit(self.bg, (self.x-self.bg.get_width()/2, self.y-150))
        else:
            win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y))
        for item in self.buttons:
            item.draw(win)
            win.blit(coin, (item.x + item.width +25, item.y -10))
            text = self.font.render(str(self.item_cost[self.tower.level-1]),1,(255,255,255))
            win.blit(text, (item.x +item.width + 25, item.y + coin.get_height()-10))
    def get_clicked(self, X, Y):
        """
        devuelve el item clicado en el menu
        :param X: int
        :param Y: int
        :return: bool
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name

        return None
