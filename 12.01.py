import pygame 
from math import *

def scale(x,a,b,A,B):
    return (x-a)*(B-A)/(b-a)+A

W, H = 320,200
N = 100
pygame.init()
Grect = pygame.Rect(10, 5, W-20, H-10)

screen = pygame.display.set_mode((W,H))
A, B = -3,4
X = [scale(i,0,N-1,A,B) for i in range(N)]
Dots = [(x, sin(x)) for x in X]
Graph = [(scale(x,A,B,Grect.left,Grect.right), scale(y,-1,1,Grect.top,Grect.bottom)) for x,y in Dots]
pygame.draw.lines(screen, (255,255,0,255),False,Graph)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

