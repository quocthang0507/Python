import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

text = 'Hello World!'

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render(text, True, GREEN, BLUE) # surface with the text on it, the second parameter is Anti-Aliasing
textRectObj = textSurfaceObj.get_rect() # get the rectangle cover the text
textRectObj.center = (200, 150) # set the position of the Rect object

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) # Put the object on the screen
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
