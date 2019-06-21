import pygame
from pygame.locals import *

pygame.init()

width, height = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
keys = [False, False, False, False]
playerpos = [100, 100]

screen = pygame.display.set_mode((width, height))
grass = pygame.image.load('data/resources/images/grass.png')
castle = pygame.image.load('data/resources/images/castle.png')
player = pygame.image.load('data/resources/images/dude.png')


def background():
    # screen.fill(BLACK)
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass, (x*100, y*100))
    screen.blit(player, playerpos)
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    pygame.display.flip()


def move():
    global playerpos
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
    background()


def main():
    global keys, playerpos
    background()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    keys[0] = True
                elif event.key == K_LEFT:
                    keys[1] = True
                elif event.key == K_DOWN:
                    keys[2] = True
                elif event.key == K_RIGHT:
                    keys[3] = True
                move()
            elif event.type == pygame.KEYUP:
                if event.key == K_UP:
                    keys[0] = False
                elif event.key == K_LEFT:
                    keys[1] = False
                elif event.key == K_DOWN:
                    keys[2] = False
                elif event.key == K_RIGHT:
                    keys[3] = False
                move()
            elif event.type == QUIT:
                pygame.quit()
                exit(0)


if __name__ == '__main__':
    main()
