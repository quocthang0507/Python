import pygame
import sys
from pygame.locals import *

# set up width and height in pixels
width = 500
height = 400

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Global point variables
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Drawing')


def init_global_points():
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    x1 = 146
    x2 = 291
    x3 = 236
    x4 = 56
    x5 = 0
    y1 = 0
    y2 = 106
    y3 = 277
    y4 = 277
    y5 = 106


def move_down():
    global y1, y2, y3, y4, y5
    y1 = y1+1
    y2 = y2+1
    y3 = y3+1
    y4 = y4+1
    y5 = y5+1


def update_points():
    global p1, p2, p3, p4, p5
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    p5 = (x5, y5)


def refresh_drawing():
    DISPLAYSURF.fill(WHITE)
    # draw on the surface object
    pygame.draw.polygon(DISPLAYSURF, GREEN, (p1, p2, p3, p4, p5))


def main():
    refresh_drawing()
    # the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # form closing
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # key pressing
                if event.key == pygame.K_DOWN:  # right arrow key
                    move_down()
                    update_points()
                    refresh_drawing()
            pygame.display.update()


init_global_points()
update_points()
main()
