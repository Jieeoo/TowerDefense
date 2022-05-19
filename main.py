import pygame.display
import os
from Enemies.orc import Orc
from Enemies.Ent import Ent
from Allies.ArcherTower import ArcherTower
from Allies.supportTower import DamageTower, RangeTower
from Allies.WizardTower import WizardTower
from Allies.TrebuchetteTower import TrebuchetteTower
import Unit
import time
import random
pygame.font.init()

lives_img = pygame.image.load(os.path.join("game_assets","heart.png"))
star_imgs = pygame.image.load(os.path.join("game_assets","star.png"))
class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [TrebuchetteTower(300, 150), ArcherTower(725, 400), WizardTower( 100,250)]
        self.support_towers = [RangeTower(500, 400), DamageTower(300,600)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer =time.time()
        self.life_font = pygame.font.SysFont("comicsans",50)

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            if time.time() -self.timer> 2:
                self.timer = time.time()
                #añadir en la lista el resto de enemigos cuando esten hechos
                self.enemys.append((random.choice([Orc(), Ent()])))

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
                self.lives -= 1
                self.enemys.remove(d)

            for tw in self.attack_towers:
                tw.attack(self.enemys)

            for tw in self.support_towers:
                tw.support(self.attack_towers)

            if self.lives <= 0:
                print("You lose")

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))

        #draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        #draw lifes
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = lives_img
        self.win.blit(text, (self.width-75, 0))
        self.win.blit(life, (self.width-600, -385))


        pygame.display.update()

    def draw_menu(self):

        pass



g = Game()
g.run()