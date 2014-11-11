import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
windowsurface = pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption('Hello world!')

black =(0,0,0)
white =(225,255,225)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

basicfont = pygame.font.SysFont(None,48)

text = basicfont.render('Hello world!',True,white,blue)
textrect =text.get_rect()
textrect.centerx = windowsurface.get_rect().centerx
textrect.centery = windowsurface.get_rect().centery

windowsurface.fill(white)


pygame.draw.line(windowsurface, blue, (60,60),(120,60),4)
pygame.draw.line(windowsurface, blue, (120,60), (60,120))
pygame.draw.line(windowsurface, blue, (60,120),(120,120),4)
pygame.draw.circle(windowsurface, blue, (300,50),20,0)
pygame.draw.ellipse(windowsurface, red, (300,250,40,80),1)
pygame.draw.rect(windowsurface, red, (textrect.left -20,textrect.top -20, textrect.width +40, textrect.height +40))

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
                                      
