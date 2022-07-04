import pygame
import os
pygame.font.init
coin = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu", "coin.png")),(40,40))
coin2 = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu", "coin.png")),(20,20))

class Button:
    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x
        self.y = menu.y
        self.menu=menu
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

    def update(self):
        self.x = self.menu.x +60
        self.y = self.menu.y+10
        if self.name=="delete":
            self.x = self.menu.x + 60
            self.y = self.menu.y -60


class PlayPauseButton(Button):
    def __init__(self, play_img, pause_img, x, y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self,win):
        if self.paused:
            win.blit(self.play,(self.x,self.y))
        else:
            win.blit(self.pause, (self.x, self.y))


class VerticalButton(Button):
    def __init__(self, x,y, img,name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


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
        self.buttons.append(Button(self, img, name))



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

        for item in self.buttons:
            if item.name == "Upgrade":
                win.blit(self.bg, (self.x + 30, self.y - 20))
                item.draw(win)
                win.blit(coin, (item.x + item.width + 25, item.y -10))
                text = self.font.render(str(self.item_cost[self.tower.level-1]),1,(255,255,255))
                win.blit(text, (item.x + item.width + 25, item.y + coin.get_height()-10))
            elif item.name == "delete":
                item.draw(win)

    def get_clicked(self, x, y):
        """
        devuelve el item clicado en el menu
        :param X: int
        :param Y: int
        :return: bool
        """
        for btn in self.buttons:
            if btn.click(x,y):

                return btn.name

        return None

    def update(self):
        for btn in self.buttons:
            btn.update()



class VerticalMenu(Menu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 20)

    def add_btn(self, img, name, cost):
        """
        añade botones al menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        btn_x = self.x -35
        btn_y = self.y -110 + (self.items-1)*95
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))

    def get_item_cost(self,name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, win):
        """
        dibuja botones y menu
        :param win:surface
        :return: None
        """

        win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 145))
        for item in self.buttons:

            item.draw(win)
            win.blit(coin2, (item.x, item.y + item.height ))
            text = self.font.render(str(item.cost),1,(255,255,255))
            win.blit(text, (item.x +25, item.y +item.height-5))
