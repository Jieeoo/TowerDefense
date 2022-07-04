import Settings
from pygame.locals import *
import pygame
import os


pygame.init()


restart_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/win_game", "restart.png")),(185,185))
you_lose = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/win_game","you_win.png")),(800,200))


class WinGame:
    def __init__(self):
        self.width = Settings.width
        self.height = Settings.height
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.re_btn = (self.width / 2 - restart_btn.get_width() / 2, self.height / 2 - restart_btn.get_height() / 2,
                       restart_btn.get_width(), restart_btn.get_height())



    def run(self):
        pygame.mixer.music.load(os.path.join("game_assets/win_game", "win_music.mp3"))
        pygame.mixer.music.play(loops = -1)
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join("game_assets/main_menu", "Title_music.mp3"))
                    pygame.mixer.music.play(loops=-1)
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    #check if start button is clicked
                    x, y = pygame.mouse.get_pos()
                    if self.re_btn[0] <= x <= self.re_btn[0] + self.re_btn[2]:
                        if self.re_btn[1] <= y <= self.re_btn[1] + self.re_btn[3]:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(os.path.join("game_assets/main_menu", "Title_music.mp3"))
                            pygame.mixer.music.play(loops=-1)
                            run = False



            self.draw()



    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(restart_btn, (self.re_btn[0], self.re_btn[1]+50))
        self.win.blit(you_lose, (self.width / 2 - you_lose.get_width() / 2, self.height / 2 - you_lose.get_height() / 2 - self.height/5))

        pygame.display.update()
