import pygame
pygame.init()


displaySurface = pygame.display.set_mode((500,480))
pygame.display.set_caption('My Game')
# animation for walking (INCLUDE ANIMATION SPRITES)
walkRight = [pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R1.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R2.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R3.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R4.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R5.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R6.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R7.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R8.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R9.png')]
walkLeft = [pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L1.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L2.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L3.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L4.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L5.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L6.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L7.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L8.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L9.png')]

backGround = pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passionate_Project/screen.png')
Character = pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/standing.png')

clock = pygame.time.Clock()


x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def rePlayWindow():
    global walkCount
    displaySurface.blit(backGround, (0,0))

    if walkCount + 1 >= 20:
        walkCount = 0

    if left:
        displaySurface.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        displaySurface.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        displaySurface.blit(Character, (x,y))

    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    rePlayWindow()

pygame.quit()
