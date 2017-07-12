import pygame
def spurce(surface, N, Rect, Color = pygame.Color("cyan")):
    '''Функция рисования ёлки в прямоугольнике'''
    # Opasnij bolvanka
    pygame.draw.rect(surface, Color, Rect)

s = ""
W, H = 640, 480
pygame.init()
screen = pygame.display.set_mode((W,H))
spurce(screen, 3, (10,10,100,200))


while True:
    s = input()
    pygame.display.flip()

#pygame.display.quit
