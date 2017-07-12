import pygame 
from math import *

W, H = 320,200
N = 100

pygame.init()
screen = pygame.display.set_mode((W,H))
A, B = -3,4
X = [A+(B-A)*i/(N-1) for i in range(N)]
Dots = [(x, sin(x)) for x in X]
Graph = [ ((x-A)*W/(B-A), (y+1)*H/2) for x,y in Dots]
pygame.draw.lines(screen, (255,255,0,255),False,Graph)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

