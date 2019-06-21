import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((width, height))

player = pygame.image.load('data/resources/images/dude.png')

while True:
    screen.fill(BLACK)
    screen.blit(player, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
