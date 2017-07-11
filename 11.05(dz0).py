import pygame
import random

W, H = 640, 480
Vel = 1, 1
pygame.init()
display = pygame.display.set_mode((W,H))
screen = display.copy()
pygame.time.set_timer(pygame.USEREVENT + 1, 50)
BLACK = pygame.Color("black")

def CreateSquare(Size, Cords):
    SCol = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    Square = pygame.Rect(*Cords, Size, Size)
    print(Square)
    return Square, SCol

def SquareMotion(SCarry, NSquare):
    e = pygame.event.poll()
    if e.type == pygame.USEREVENT+1:
        screen.fill(BLACK)
        for i in range(Count):
            pygame.draw.rect(screen, SquareC[i], SquareS[i])
            SquareS[i] = SquareS[i].move(Vel)
    #elif e.type == pygame.QUIT or e.type == pygame.KEYUP and e.key == 27:
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
        for i in range(Count):
            if SquareS[i].collidepoint(e.pos):
                SCarry = True
                print("Понесли квадрат")
                NSquare = i
                #Понесли квадрат
    elif e.type == pygame.MOUSEBUTTONUP and e.button == 1 :
        if SCarry:
            SCarry = False
            SquareS[NSquare].center = e.pos
            #print("Перенесли в", Square.center)
    elif e.type == pygame.MOUSEMOTION and e.buttons[0]:
        if SCarry:
            SquareS[NSquare].center = e.pos
    return SCarry, NSquare


Count = int(input())
SquareS, SquareC = [], []
q = 1
SCarry = False
NSquare = 0

for i in range(Count):
    r = random.randint(0,255)
    x = CreateSquare(r, (random.randint(0,255), random.randint(0,255)))
    SquareS += [""]
    SquareC += [""]
    SquareS[i], SquareC[i] = x

while True:
    SCarry, NSquare = SquareMotion(SCarry, NSquare)
    display.blit(screen, (1, 1))
    pygame.display.flip()
