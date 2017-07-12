# создать класc Sqaure, который должен
#  - содержать размер и координаты (pygame.Rect) 
#  - содержать цвет (pygame.Color)
#  - содержать метод show(self, surface) - нарисовать себя на surface
#  - содержать метод ID(self) - строка с описанием объекта
#  создать список из 10 таких прямоугольников, задать их координаты
#  нарисовать все

import pygame
import random

def randcolor():
    col = [random.randrange(100,255), random.randrange(100,255), random.randrange(100,255)]
    random.shuffle(col)
    return pygame.Color(*col)
    
class Square:
    rect = pygame.Rect(0,0,0,0)
    color = pygame.Color(0,0,0,0)
    
    def show(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
    
    def ID(self):
        return "Square: {}/{}".format(self.rect, self.color)
    
W, H = 320, 200
pygame.init()
screen = pygame.display.set_mode((W, H))

SQS = [Square() for i in range(10)]
for s in SQS:
    s.color = randcolor()
    s.rect = pygame.Rect(random.randrange(0,W-10), random.randrange(0, H-10), 10, 10)

for s in SQS:
    s.show(screen)
    
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
