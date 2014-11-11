import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption('Hello world!')


pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False



pygame.quit()
           
                                      
