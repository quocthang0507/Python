import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
grass = pygame.image.load('data/resources/images/grass.png')
castle = pygame.image.load('data/resources/images/castle.png')
player = pygame.image.load('data/resources/images/dude.png')

while True:
    #screen.fill(BLACK)
    screen.blit(player, (100, 100))
    pygame.display.flip()
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass, (x*100, y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
