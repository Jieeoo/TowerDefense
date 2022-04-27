import pygame

pygame.init()
window = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

class Prueba:

    def __init__(self):

        self.path = [(1187, 146), (400, 141), (394, 325), (882, 341), (878, 537), (160, 517), (132, 155)]
        self.path_ini= self.path[0]
        self.speed= 5

    def move(self, pos):
        pore = self.path[0]
        dir = pygame.math.Vector2(self.path[0]) - pos
        if dir.length() <= self.speed:
            pos = self.path[0]
            self.path.append(self.path[0])
            self.path.pop(0)
        else:
            dir.scale_to_length(self.speed)
            new_pos = pygame.math.Vector2(pos) + dir
            pos = (new_pos.x, new_pos.y)
        return pos
    def ataque(self):
        if pos == self.path[-1]:

        else:
            pass

if __name__ == '__main__':
    run = True
    P = Prueba()
    pos=(1187, 146)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = P.move(pos)

        window.fill(0)
        pygame.draw.circle(window, "red", pos, 20)
        pygame.display.update()
        clock.tick(100)

    pygame.quit()