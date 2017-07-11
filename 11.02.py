import random
import pygame
W, H = 640, 480
pygame.init()
screen = pygame.display.set_mode((W,H))
while 1:
    e = pygame.event.wait()
    if e.type == pygame.QUIT or e.type == pygame.KEYUP and e.key == 27:
        break
    elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
        pygame.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), e.pos, random.randrange(3,4))
    else:
        print(e)
    pygame.display.flip()





















