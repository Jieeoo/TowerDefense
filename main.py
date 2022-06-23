import pygame.display
import os
from Enemies.orc import Orc
from Enemies.Ent import Ent
from Enemies.Troll import Troll
from Allies.ArcherTower import ArcherTower
from Allies.supportTower import DamageTower, RangeTower
from Allies.WizardTower import WizardTower
from Allies.TrebuchetteTower import TrebuchetteTower
from Menu.menu import VerticalMenu, PlayPauseButton
import Unit
import time
import random
pygame.font.init()

lives_img = pygame.image.load(os.path.join("game_assets","heart.png"))
coin_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu", "coin.png")),(40,40))
UI_background = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","menu.png")), (200,100))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","menu.png")), (100,500))

archer_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","archer_icon.png")), (75,75))
wizard_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","wizard_icon.png")), (75,75))
catapulta_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","catapulta_icon.png")), (75,75))
range_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","range_icon.png")), (75,75))
damage_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","damage_icon.png")), (75,75))

play_btn=pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","play.png")), (75,75))
pause_btn=pygame.transform.scale(pygame.image.load(os.path.join("game_assets/Menu","pausa.png")), (75,75))

attack_tower_name=["archer","wizard","catapulta"]
support_tower_name=["range","damage"]

waves = [
    [20, 0, 0],
    [50, 0, 0],
    [100,0,0],
    [50,20,0],
    [20,50, 0],
    [50, 0,20],

]


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [TrebuchetteTower(300, 150), ArcherTower(725, 400), WizardTower( 100,250), ArcherTower(725, 50)]
        self.support_towers = [RangeTower(800, 400), DamageTower(800,500)]
        self.lives = 10
        self.money = 20000
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.0.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer =time.time()
        self.life_font = pygame.font.SysFont("comicsans",30)
        self.selected_tower = None
        self.Menu = VerticalMenu(self.width - side_img.get_width()+55 , 300, side_img)
        self.Menu.add_btn(archer_icon,"buy_archer",500)
        self.Menu.add_btn(wizard_icon, "buy_wizard", 750)
        self.Menu.add_btn(catapulta_icon, "buy_catapulta", 100)
        self.Menu.add_btn(range_icon, "buy_range",750)
        self.Menu.add_btn(damage_icon, "buy_damage", 750)
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.PlayPauseButton= PlayPauseButton(play_btn,pause_btn,10,self.height-85)

    def gen_enemies(self):
        if sum(self.current_wave) == 0:
            self.wave += 1
            self.current_wave = waves[self.wave]
            self.pause = True
        else:
            wave_enemies = [Orc(), Ent(), Troll()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] !=0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] -1
                    break

    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            pygame.time.delay(100)
            clock.tick(30)
            if self.pause == False:
                if time.time() -self.timer> 2:
                    self.timer = time.time()
                    #añadir en la lista el resto de enemigos cuando esten hechos
                    self.gen_enemies()

            pos = pygame.mouse.get_pos()

            if self.moving_object:
                self.moving_object.move(pos[0],pos[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.moving_object:

                        if self.moving_object.name in attack_tower_name:
                            self.attack_towers.append(self.moving_object)
                        elif self.moving_object.name in support_tower_name:
                            self.support_towers.append(self.moving_object)
                        self.moving_object.moving = False
                        self.moving_object = None

                    else:
                        if self.PlayPauseButton.click(pos[0],pos[1]):
                            self.pause = not(self.pause)
                            self.PlayPauseButton.paused = self.pause

                        side_menu_button = self.Menu.get_clicked(pos[0],pos[1])
                        if side_menu_button:

                            cost=self.Menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.add_tower(side_menu_button)
                                self.money -= cost

                        btn_clicked=None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()

                        if not (btn_clicked):
                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False
            to_del = []
            for en in self.enemys:
                en.move()
                if en.pos[0] == 110 and en.pos[1] == 90:
                    to_del.append(en)
            for d in to_del:
                self.lives -= 1
                self.enemys.remove(d)
            for tw in self.attack_towers:
                self.money += tw.attack(self.enemys)

            for tw in self.support_towers:
                tw.support(self.attack_towers)

            if self.lives <= 0:
                print("You lose")
                run=False

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        # draw enemies
        for en in self.enemys:
            en.draw(self.win)


        #draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)
        self.Menu.draw(self.win)

        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw UI background
        UIbg = UI_background
        self.win.blit(UIbg, (self.width - 200, 0))

        self.PlayPauseButton.draw(self.win)

        #draw lifes
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = lives_img
        self.win.blit(text, (self.width-100, 10))
        self.win.blit(life, (self.width-650, -395))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = coin_img
        self.win.blit(text, (self.width - 120, 48))
        self.win.blit(money, (self.width - 175, 48))



        pygame.display.update()



    def add_tower(self, name):
        x,y= pygame.mouse.get_pos()
        name_list=["buy_archer","buy_wizard", "buy_catapulta", "buy_range", "buy_damage"]
        object_list=[ArcherTower(x,y),WizardTower(x,y),TrebuchetteTower(x,y),RangeTower(x,y),DamageTower(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True

        except Exception as e:
            print(str(e)+ "NOT VALID NAME")

g = Game()
g.run()