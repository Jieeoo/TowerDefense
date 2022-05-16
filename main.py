import pygame.display
import os
from Enemies.orc import Orc
from Allies.ArcherTower import ArcherTower
class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Orc()]
        self.towers = [ArcherTower(300,300),ArcherTower(300,400)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
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

        for en in self.enemys:
            en.draw(self.win)

        for tw in self.towers:
            tw.draw(self.win)
        pygame.display.update()


g = Game()
g.run()