import pygame


pygame.init()

display_width = 800
display_length = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



gameDisplay = pygame.display.set_mode((display_width,display_length))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('screen.png')

def Bk_ground(x,y):
    gameDisplay.blit(backgroundImg,(x,y))

x = (display_width * 0.45)
y = (display_length * 0.8)




crashed = False


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    Bk_ground(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()