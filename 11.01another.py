import pygame
import random
def spurce(surface, N, Rect, Color = pygame.Color("cyan")):
    '''Функция рисования ёлки в прямоугольнике'''
    print(Rect)
    print(Color)
    # Opasnij bolvanka
    #pygame.draw.rect(surface, Color, Rect)
    for i in range(N):
        points = (  (Rect.x + Rect.w//2, Rect.y + i*Rect.h//N),
                    (Rect.x + Rect.w - 1, Rect.y + (i+1)*Rect.h//N-1),
                    (Rect.x, Rect.y + (i+1)*Rect.h//N - 1),
                 )
        pygame.draw.polygon(surface,Color,points)
        pygame.draw.polygon(surface,Color//pygame.Color(3,2,1,1),points,2)
    
s = 1
W, H = 640, 480
pygame.init()
screen = pygame.display.set_mode((W,H))
spurce(screen, 3, pygame.Rect(10,10,100,200))
while s:
    spurce(screen, 3, pygame.Rect(random.randint(100, 500),random.randint(100, 500),100,200))
    pygame.display.flip()
    
#pygame.display.quit
