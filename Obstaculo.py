import pygame
import Settings
import os
import math

W = Settings.width
H = Settings.height
clock = pygame.time.Clock()
window = pygame.display.set_mode((W, H))
path = [(W, H / 6.5), (W / 3.3, H / 6.5), (W / 3.3, H / 2.25), (W / 1.4, H / 2.25), (W / 1.4, H / 1.25),
                     (W / 11, H / 1.4), (W / 11, H / 4)]
path_bg=[(0,0),(W/3.2,H/4),(W/1.35,0),(W,H/6),(W/1.32,H/4),(W,H/1.6),(W/1.14,H/1.6),(W,H),(0,H/1.4),(W/4.5,H)]
bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
bg = pygame.transform.scale(bg, (W, H))


class obstaculo():
    def __init__(self):
        self.color=(255,0,0,100)
        self.width=64
        self.height=64

    def draw(self,win,obs):

        surface= pygame.Surface(pygame.Rect(obs).size,pygame.SRCALPHA,32)
        pygame.draw.rect(surface,self().color,surface.get_rect())

        win.blit(surface,obs)

    def rectangulo_camino(self):
        lista=[]
        for x in range(len(path)-1):
            X=path[x][0]
            Y=path[x][1]
            X1=path[x + 1][0]
            Y1=path[x + 1][1]
            width= obstaculo.Width(self,X, X1)
            height=obstaculo.Height(self,Y,Y1)
            if X>X1:
                lista.append((X1, Y1, width, height))
            elif Y1<Y:
                lista.append((X1, Y1, width, height))
            else:
                lista.append((X, Y, width, height))
        return lista

    def rectangulo_bg(self):
        lista=[]
        for x in range(0,len(path_bg) - 1,2):
            X = path_bg[x][0]
            Y = path_bg[x][1]
            X1 = path_bg[x + 1][0]
            Y1 = path_bg[x + 1][1]
            width =  abs(X - X1)
            height = abs(Y - Y1)
            lista.append((X, Y, width, height))
        return lista


    def Width(self, X, X1):
        if X == X1:
            width = 60
        else:
            width = abs(X - X1)
        return width

    def Height(self,Y,Y1):
        if Y == Y1 or abs(Y - Y1)<70:
            height = 70
        else:
            height = abs(Y - Y1)
        return height




    def collide(self, obs):
        if pygame.Rect(self.x,self.y,64,64).colliderect(pygame.Rect(obs)):
            return True
        else:
            return False




if __name__ == '__main__':
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(bg,(0,0))
        for x in range(len(obstaculo.rectangulo_camino(obstaculo))):
            obstaculo.draw(obstaculo,window,obstaculo.rectangulo_camino(obstaculo)[x])
        for x in range(len(obstaculo.rectangulo_bg(obstaculo))):
            obstaculo.draw(obstaculo,window,obstaculo.rectangulo_bg(obstaculo)[x])
        pygame.display.update()
        clock.tick(100)





