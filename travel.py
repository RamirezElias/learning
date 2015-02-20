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
y = 25
x2 = 70
y2 = 120

windowsurface.blit(Alien3a,(x,y))
pygame.display.update()

for i in range(30):
    windowsurface.fill(black)
    y = y + 30
    windowsurface.blit(Alien3a,(x,y))
    pygame.display.update()    


running = True
# begin game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


pygame.quit()                  
