import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption('Hello world!')

black =(0,0,0)
lightgreen =(225,255,225)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

basicfont = pygame.font.SysFont(None,48)

text = basicfont.render('Hello world!',True,lightgreen,blue)
textrect =text.get_rect()
textrect.centerx = windowsurface.get_rect().centerx
textrect.centery = windowsurface.get_rect().centery

windowsurface.fill(lightgreen)



pygame.draw.rect(windowsurface, red, (textrect.left -20,textrect.top -20, textrect.width +40, textrect.height +40))

eg. asurf = pygame.image.load('elias', 'Alien3a.png')


pixArray = pygame.PixelArray(windowsurface)
pixArray[480][380] =black
del pixArray

windowsurface.blit(text, textrect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                                      
