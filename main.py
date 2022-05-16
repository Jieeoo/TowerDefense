import pygame.display
import os
from Enemies.orc import Orc
from Allies.ArcherTower import ArcherTower
import Unit
import time
import random

lives_img = pygame.image.load(os.path.join("game_assets","heart.png"))
star_imgs = pygame.image.load(os.path.join("game_assets","star.png"))
class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Orc()]
        self.towers = [ArcherTower(300,300), ArcherTower(700,600)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer =time.time()

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            if time.time() -self.timer> 2:
                self.timer = time.time()
                #añadir en la lista el resto de enemigos cuando esten hechos
                self.enemys.append((random.choice([Orc()])))

            pygame.time.delay(100)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
            to_del = []
            for en in self.enemys:
                if en.pos[0] == 110 and en.pos[1] == 90:
                    to_del.append(en)
            for d in to_del:
                self.enemys.remove(d)

            for tw in self.towers:
                tw.attack(self.enemys)

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))

        #draw towers
        for tw in self.towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        #draw lives
        live = lives_img
        start_x = self.width - live.get_width() - 5
        live = lives_img
        for x in range(self.lives):
            self.win.blit(live, (start_x - live.get_width()*x + 5, 10))


        pygame.display.update()


g = Game()
g.run()