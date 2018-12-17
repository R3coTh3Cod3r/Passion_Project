import pygame,sys
from pygame.locals import *


pygame.init()
display_width = 800
display_height = 600

DisplaySurface = pygame.display.set_mode((display_width,display_height))
screenImgage = pygame.image.load("/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/screen.png").convert()

x = 20;
y= 30;
DisplaySurface.blit(screenImgage,(x,y))
pygame.display.flip()

pygame.display.set_caption("My Game Now!")
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
#

pygame.quit()