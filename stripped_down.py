import pygame
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((300,400),0,32)
pygame.display.set_caption('SPACE GAME !')

blue =(0,0,255)
white = (255,255,255)
red = (255,0,0)
basicfont = pygame.font.SysFont(None,48)



windowsurface.fill(white)


Alien3a = '/home/carmen/elias/Alien3a.png'

#pygame.image.load(Alien3a)

pygame.draw.rect(windowsurface, blue, ((5,5),(50,50)))
pygame.draw.circle(windowsurface, blue, (275,50),20,0)

pygame.draw.circle(windowsurface, red, (20,100),20,0)
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
            



pygame.quit()
                              
