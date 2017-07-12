import pygame
import random
W, H = 640, 480
SW, SH = 30, 30
pygame.init()
display = pygame.display.set_mode((W,H))
screen = display.copy()
SCol = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
Square = pygame.Rect(W//2-SW//2,H//2-SH//2,SW,SH)
BLACK = pygame.Color("black")
SCarry = False
while 1:
    e = pygame.event.wait()
    if e.type == pygame.QUIT or e.type == pygame.KEYUP and e.key == 27:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
        if Square.collidepoint(e.pos):
            SCarry = True
            print("Понесли квадрат")
        #Понесли квадрат
        print()
    elif e.type == pygame.MOUSEBUTTONUP and e.button == 1 :
        if SCarry:
            SCarry = False
            Square.center = e.pos
            print("Перенесли в", Square.center)
        #Понесли квадрат
        print()
    elif e.type == pygame.MOUSEMOTION and e.buttons[0]:
        if SCarry:
            Square.center = e.pos
    else:
        print(e)
    screen.fill(BLACK)
    pygame.draw.rect(screen, SCol, Square) 
    display.blit(screen, (0, 0))
    pygame.display.flip()

