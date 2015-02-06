import pygame
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((300,400),0,32)
pygame.display.set_caption('SPACE GAME !')

blue =(0,0,255)
white = (255,255,255)
red = (255,0,0)
green =(0,255,0)
black = (0,0,0)
basicfont = pygame.font.SysFont(None,48)



windowsurface.fill(black)



Alien3a = pygame.image.load("Alien3a.png")

x = 150
y = 200
x2 = 70
y2 = 120

running = True

# begin game loop
while running == True:
    windowsurface.blit(Alien3a,(x,y))
    #windowsurface.blit(Alien3a,(x2,y2))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == 273:
                print 'up'
                y = y - 1
            if event.key == 274:
                print 'down'
                y = y + 1
            if event.key == 275:
                print 'right'
                x = x + 1
            if event.key == 276:
                print 'left'
                x = x -1


            # end loop

pygame.quit()                  
