# the following will import pygame library

import pygame
import images
import arcade
import os
from pygame.locals import *


pygame.init()

window_width = 600

window_length = 600



size = (window_width,window_length)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hello World")

ded= False

clock = pygame.time.Clock()
background_image = pygame.image.load("screen.png")
while(ded==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ded = True

        screen.blit(background_image,[0,0])





pygame.display.flip()
# clock.tick(clock_tick_rate)
pygame.quit()
quit()
