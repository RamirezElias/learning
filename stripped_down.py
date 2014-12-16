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


Alien3a = '/home/carmen/elias/Alien3a.png'

#pygame.image.load(Alien3a)

pygame.draw.rect(windowsurface, blue, ((10,10),(100,100)))

pygame.draw.circle(windowsurface, red, (60,60),20)

pygame.draw.rect(windowsurface, blue, ((130,130),(100,100)))

#rect 3                 
pygame.draw.rect(windowsurface, green, ((130,10),(100,100)))
#rect 2

pygame.draw.rect(windowsurface, green, ((10,130),(100,100)))
pygame.draw.circle(windowsurface, blue, (150,90),20,0)
                 
pygame.draw.rect(windowsurface, blue, ((10,250),(100,100)))
                 
pygame.draw.rect(windowsurface, green, ((130,250),(100,100)))
#rect 6
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
            



pygame.quit()
                              
