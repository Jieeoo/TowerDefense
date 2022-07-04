import Settings
from main import Game
import pygame
from pygame.locals import *
import os
pygame.init()


start_btn = pygame.image.load(os.path.join("game_assets/main_menu","start.png"))
Title = pygame.image.load(os.path.join("game_assets/main_menu","Title.png"))
Title2 = pygame.image.load(os.path.join("game_assets/main_menu","Title2.png"))


class MainMenu:
    def __init__(self):
        self.width = Settings.width
        self.height = Settings.height
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.btn = (self.width/2 - start_btn.get_width()/2, self.height/2 - start_btn.get_height()/2, start_btn.get_width(), start_btn.get_height())

    def run(self):
        pygame.mixer.music.load(os.path.join("game_assets/main_menu", "Title_music.mp3"))
        pygame.mixer.music.play(loops = -1)
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    #check if start button is clicked
                    x, y = pygame.mouse.get_pos()
                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.run()
                            del game



            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(start_btn,(self.btn[0],self.btn[1]))
        self.win.blit(Title, (self.width/2-Title.get_width()/2, self.height/2-Title.get_height()/2-250))
        self.win.blit(Title2, (self.width / 2 - Title2.get_width() / 2, self.height / 2 - Title2.get_height() / 2 - 150))
        #pygame.draw.circle(self.win,(255,0,0),(140,150), 10)
        pygame.display.update()
