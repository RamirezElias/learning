import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption('SPACE GAME !')

blue =(0,0,255)
white = (255,255,255)

basicfont = pygame.font.SysFont(None,48)



windowsurface.fill(white)


Alien3a = '/home/carmen/elias/Alien3a.png'

pygame.image.load(Alien3a)


pygame.display.update()

pygame.draw.circle(windowsurface, blue, (300,50),20,0)



running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            



pygame.quit()
                              
