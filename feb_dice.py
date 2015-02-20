##
# future tasks:
# - make boxes = side 2, side 3, etc for each die side
# - click on the screen and say which was clicked on
# - box number or empty space

import pygame
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((300,400),0,32)
pygame.display.set_caption('DICE GAME !')

blue =(0,0,255)
white = (255,255,255)
red = (255,0,0)
green =(0,255,0)
black = (0,0,0)
basicfont = pygame.font.SysFont(None,48)



windowsurface.fill(white)


pygame.draw.rect(windowsurface, blue, ((10,10),(100,100)))
pygame.draw.circle(windowsurface, black, (60,60),20)

pygame.draw.rect(windowsurface, green, ((130,10),(100,100)))
pygame.draw.circle(windowsurface, blue, (180,60),20,0)

pygame.draw.rect(windowsurface, green, ((10,130),(100,100)))
pygame.draw.circle(windowsurface, blue, (60,180),20,0)

pygame.draw.rect(windowsurface, blue, ((130,130),(100,100)))
pygame.draw.circle(windowsurface, red, (180,180),20,0)
                 
pygame.draw.rect(windowsurface, blue, ((10,250),(100,100)))
pygame.draw.circle(windowsurface, red, (60,300),20,0)
                 
pygame.draw.rect(windowsurface, green, ((130,250),(100,100)))
pygame.draw.circle(windowsurface, blue, (180,300),20,0)


pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
                              
