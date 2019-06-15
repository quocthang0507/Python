# To deal with graphics, sound, and other features
import pygame, sys

# Many constant variables is being in the pygame.locals module without pygame.locals.
from pygame.locals import *

# Initialize pygame
pygame.init()

# Tuple (x, y) tells the set_mode() function how wide and how high in pixels
DISPLAYSURF = pygame.display.set_mode((400, 300))

# Name of the window
pygame.display.set_caption('Hello World!')

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
