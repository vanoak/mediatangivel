# parametric lines. John whitney

import pygame
from pygame.locals import *
import sys
from pygame import gfxdraw
import random
import math
from psonic import *

width, height = (1024,768)

def x1(t):
    return int(math.sin(t/10) * 100 + math.sin(t / 5) * 100 +width/2)
    
def y1(t):
    return int(math.cos(t / 10) * 100 + height/2)
    
def x2(t):
    return int(math.sin(t/10) * 200 + math.sin(t) * 2 +width/2)

def y2(t):
    return int(math.cos(t / 20) * 200 + math.cos(t/12) * 20 + height/2)
    
pygame.init()
t = 0
screen = pygame.display.set_mode((1024,768))

pygame.mouse.set_visible(False)
play(80)
while True:
    screen.fill((255,255,255))
    for i in range(20):
        drawSurface = pygame.Surface((1024,768),pygame.SRCALPHA, 32)
        pygame.gfxdraw.line(drawSurface, x1(t+i) ,y1(t+i), x2(t+i), y2(t+i),(0,0,0,255))
        screen.blit(drawSurface,(0,0))
        t = t+0.3
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            sys.exit(0)
