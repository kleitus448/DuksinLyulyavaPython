import pygame
import random

W, H = 640, 480
pygame.init()
display = pygame.display.set_mode((W,H))
screen = display.copy()
pygame.time.set_timer(pygame.USEREVENT + 1, 50)
BLACK = pygame.Color("black")

def CreateSquare(Size, Cords, Vel):
    SCol = pygame.Color(random.randint(100,255),random.randint(100,255),random.randint(100,255))
    Square = pygame.Rect(*Cords, Size, Size)
    return Square, SCol, Vel

def SquareMotion(SCarry, NSquare):
    e = pygame.event.poll()
    if e.type == pygame.USEREVENT+1:
        screen.fill(BLACK)
        for i in range(Count):
            pygame.draw.rect(screen, SquareC[i], SquareR[i])
            SquareR[i] = SquareR[i].move(SquareS[i])
            if SquareR[i].left < 0 or SquareR[i].right > W:
                SquareS[i] = -SquareS[i][0], SquareS[i][1]
            if SquareR[i].top < 0 or SquareR[i].bottom > H:
            	SquareS[i] = SquareS[i][0], -SquareS[i][1]
            for k in range(Count):
                if i == k: continue
                if SquareR[k].colliderect(SquareR[i]):
                    SquareS[i] = -SquareS[i][0], -SquareS[i][1]
                    SquareS[k] = -SquareS[k][0], -SquareS[k][1]
    elif e.type == pygame.QUIT or e.type == pygame.KEYUP and e.key == 27:
        return SCarry, -1
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 :
        for i in range(Count):
            if SquareR[i].collidepoint(e.pos):
                SCarry = True
                print("Понесли квадрат")
                NSquare = i
                #Понесли квадрат
    elif e.type == pygame.MOUSEBUTTONUP and e.button == 1 :
        if SCarry:
            SCarry = False
            SquareR[NSquare].center = e.pos
            #print("Перенесли в", Square.center)
    elif e.type == pygame.MOUSEMOTION and e.buttons[0]:
        if SCarry:
            SquareR[NSquare].center = e.pos
    return SCarry, NSquare

Count = int(input())
SquareR, SquareC, SquareS = [], [], []
SCarry = False
NSquare = 0

for i in range(Count):
    r = random.randint(5,20)
    x = CreateSquare(r, (random.randint(0,255), random.randint(0,255)), \
                    (random.randrange(-5,5), 0))
    SquareR += [""]
    SquareC += [""]
    SquareS += [""]
    SquareR[i], SquareC[i], SquareS[i] = x
    print(i, SquareR[i])

while NSquare != -1:
    SCarry, NSquare = SquareMotion(SCarry, NSquare)
    display.blit(screen, (1, 1))
    pygame.display.flip()
