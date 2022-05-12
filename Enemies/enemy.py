import Unit
import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

class Enemy:

    def __init__(self):
        self.path = [(1187, 146), (400, 141), (394, 325), (882, 341), (878, 537), (160, 517), (132, 155)]
        self.pos = self.path[0]
        self.speed = 1

    def move(self, pos, speed, points):
        circle_dir = pygame.math.Vector2(points[0]) - pos
        if circle_dir.length() <= speed:
            pos = points[0]
            points.append(points[0])
            points.pop(0)
        else:
            circle_dir.scale_to_length(speed)
            new_pos = pygame.math.Vector2(pos) + circle_dir
            pos = (new_pos.x, new_pos.y)
        return pos
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pos = move(pos, speed, corner_points)

            window.fill(0)
            pygame.draw.lines(window, "gray", True, path)
            pygame.draw.circle(window, "red", pos, 20)
            pygame.display.update()
            clock.tick(100)

        pygame.quit()