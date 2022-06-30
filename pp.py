# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# Is it possible to implement gradual movement of an object to given coordinates in Pygame?
# https://stackoverflow.com/questions/60356812/is-it-possible-to-implement-gradual-movement-of-an-object-to-given-coordinates-i/60356995#60356995
#
# How to make a circle move diagonally from corner to corner in pygame
# https://stackoverflow.com/questions/65814020/how-to-make-a-circle-move-diagonally-from-corner-to-corner-in-pygame/65814431#65814431
#
# How to move the object in squared path repeatedly?
# https://stackoverflow.com/questions/71340195/how-to-move-the-object-in-squared-path-repeatedly/71340468#71340468
#
# GitHub - PyGameExamplesAndAnswers - Motion and movement - Move and rotate - Move in grid
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

corner_points = [(100, 100), (300, 300), (300, 100), (100, 300)]
poss = corner_points[:]
pos = corner_points[0]
speed = 10


def move(pos, speed, points):
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
    pygame.draw.rect(window, "gray", pygame.Rect(poss[0][0],poss[0][1],abs(poss[0][0]-poss[2][0]),abs(poss[0][1]-poss[2][1])))
    pygame.draw.circle(window, "red", pos, 20)
    pygame.display.update()
    clock.tick(100)

pygame.quit()


def point_to_line(self, tower):
    """
    returns if you can place a tower based on the distance to the path
    :param tower:
    :return: Bool
    """
    # find two closest points
    closest = []
    for point in path:
        dis = math.sqrt((tower.x - point[0]) ** 2 + (tower.y - point[1]) ** 2)
        closest.append([dis, point])

    closest.sort(key=lambda x: x[0])

    return True

    if self.moving_object.path_dis(self.point_to_line(self.moving_object)):
        not_allowed = True


    def point_to_line(self,tower):
        """
        returns if you can place a tower based on the distance to the path
        :param tower:
        :return: Bool
        """
        W = self.width
        H = self.height
        path = [(W, H / 7), (W / 3.3, H / 7), (W / 3.3, H / 2.5), (W / 1.4, H / 2.5), (W / 1.4, H / 1.45),
                (W / 13, H / 1.45), (W / 13, H / 5)]
        #find two closest points
        closest=[]
        for point in path:
            dis = math.sqrt((tower.x-point[0])**2+(tower.y - point[1])**2)
            closest.append([dis,point])

        closest.sort(key=lambda x: x[0])
        p1 = closest[0][1]
        p2 = closest[0][1]
        try:
            m = (p1[1]-p2[1])/(p1[0]-p2[0])
            n = p1[1] - m * p1[0]
            mp = -1 / m
            np = tower.y - tower.x * mp
            xc = (n - np) / (mp - m)
            yc = m * xc + n
            dis = math.sqrt((tower.x - xc) ** 2 + (tower.y - yc) ** 2)

            return dis
        except ZeroDivisionError:
            dis = tower.y - p1[1]

            return dis

    def path_dis(self, dis):
        if dis >= 10:
            return False
        else:
            return True