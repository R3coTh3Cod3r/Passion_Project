import pygame
import sys
import pygame.sprite as sprite
import os
from pygame.locals import *
def events():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
pygame.init()
width_display=1900
height_display=1100
screen = pygame.display.set_mode((width_display, height_display ))
pygame.display.set_caption('My game Now!!')
CLOCK = pygame.time.Clock()
background_Image = pygame.image.load("/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/pixelbackground.png").convert()
FPS = 120


x = 0 # x coordnate of image
 # y coordinate of image
# screen.blit(background_Image, ( x,y)) # paint to screen
pygame.display.flip() # paint screen one time

# Main Loop
while True:
    events()

    rel_x = x % background_Image.get_rect().width
    screen.blit(background_Image,(rel_x, 0))
    if rel_x < width_display:
        screen.blit(background_Image,(rel_x, 0))
        x -= 1

    pygame.display.update()
    CLOCK.tick(FPS)

#loop over, quite pygame
# pygame.quit()