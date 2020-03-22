debug = False

import cv2
import numpy as np
import sys
from omxplayer.player import OMXPlayer  
from pathlib import Path

import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
screen = pygame.display.set_mode((1024,768))

camera = cv2.VideoCapture(0)

# define the list of boundaries
azul = [([230, 0, 0], [255, 200, 200]),]

VIDEO_PATH = "/home/pi/Documents/joao/london.mp4"
player = OMXPlayer(VIDEO_PATH, args =['--no-osd','--loop'])
player.pause()

blue_pixels = 0 

while True:
    ret, frame = camera.read()
    for (lower, upper) in azul:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask = mask)
        output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        (thresh, output) = cv2.threshold(output, 127, 255, cv2.THRESH_BINARY)
        blue_pixels = cv2.countNonZero(output)
        textsurface = myfont.render(str(blue_pixels), False, (0, 255, 0))
        
    if debug:
        screen.fill([0,0,0])
        output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        output = np.rot90(output)
        output = pygame.surfarray.make_surface(output)
        screen.blit(output, (0,0))
        screen.blit(textsurface,(120,120))

        pygame.display.update()

    else:
        if blue_pixels > 1000:
            if not player.is_playing():
                player.play()
        else:
            player.pause()
            
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pygame.quit()
            cv2.destroyAllWindows()
            sys.exit(0)
            
