import pygame 
from math import *

def scale(x,a,b,A,B):
    return (x-a)*(B-A)/(b-a)+A
    
def fun(x):
    return x**3 - 5*x**2+x+1  

W, H = 320,200
N = 100
pygame.init()
Grect = pygame.Rect(10, 5, W-20, H-10)

screen = pygame.display.set_mode((W,H))
A, B = eval(input())

X = [scale(i,0,N-1,A,B) for i in range(N)]
Y = [fun(x) for x in X]
Max,Min = max(Y),min(Y)
Graph = [(scale(x,A,B,Grect.left,Grect.right), scale(y,Min,Max,Grect.bottom,Grect.top)) for x,y in zip(X,Y)]
pygame.draw.lines(screen, (255,255,0,255),False,Graph)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
