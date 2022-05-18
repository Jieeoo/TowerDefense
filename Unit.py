import pygame
import math

class Unit:
    def __init__(self):
        self.widht = 32
        self.height = 32
        self.animation_count = 0
        self.health = 1
        self.vel = 10
        self.path = [(1187, 100), (350, 100), (350, 300), (850, 300), (850, 480), (110, 480), (110, 90)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count =0
        self.move_dis = 0
        self.dis=0
        self.imgs=[]
        self.pos=((1187, 100))
        self.flipped_1 = False
        self.flipped_2 = False
        self.max_health = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """

        self.img = self.imgs[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.pos))
        self.draw_health_bar(win)
        self.move()

    def draw_health_bar(self, win):
        """
        draw health bar above a unit
        :param win: surface
        :return: none
        """
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.pos[0]+10, self.pos[1]-15, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.pos[0]+10,self.pos[1]-15, health_bar, 10), 0)



    def collide(self, x, y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <=self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        
        """Move enemy
        :return: None


        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10,155)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis=math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.move_count += 1

        dirn = (x2-x1, y2-y1)
        if dirn[0] > 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img,True,False)


        move_x, move_y = (self.x + dirn[0] * self.move_count,self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)
        self.x = move_x
        self.y = move_y
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False


        return True
        """
        pore = self.path[0]
        dir = pygame.math.Vector2(pore) - self.pos
        if dir.length() <= self.vel:
            pos = self.path[0]
            self.path.append(pore)
            self.path.pop(0)
        else:
            dir.scale_to_length(self.vel)
            new_pos = pygame.math.Vector2(self.pos) + dir
            pos = (new_pos.x, new_pos.y)
        self.pos=pos

        if pos[0] == 350 and pos[1] >=100 and not(self.flipped_1):
            self.flipped_1 = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)
        elif pos[0] == 850 and pos[1] >=300 and not (self.flipped_2):
            self.flipped_2 = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

    def hit(self, damage):
        """
        Returns if a enemy has died and removes one health each call
        :return:Bool
        """

        self.health -= damage
        if self.health <= 0:
            return True
        return False