import pygame

pygame.init()


displaySurface = pygame.display.set_mode((1014,658))
pygame.display.set_caption('My Game')
# animation for walking (INCLUDE ANIMATION SPRITES)
walkRight = [pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R1.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R2.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R3.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R4.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R5.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R6.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R7.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R8.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/R9.png')]
walkLeft = [pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L1.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L2.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L3.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L4.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L5.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L6.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L7.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L8.png'), pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/L9.png')]

backGround = pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/pixelbackground_small.png')
Character = pygame.image.load('/home/student/CodeSchool/IdeaProjects/Passion_Project/Pyton_Game_files/images/standing.png')

clock = pygame.time.Clock()



class player(object):
    def __init__(self,x,y,width,height):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.vel = 5
       self.isJump = False
       self.left = False
       self.right = False
       self.walkCount = 0
       self.jumpCount = 10


    def draw(self,displaySurface):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            displaySurface.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            displaySurface.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount +=1
        else:
            displaySurface.blit(Character, (self.x, self.y))







def rePlayWindow():
    pygame.font.init() # you have to call this at the start,

    #This will initialize the text
    myfont = pygame.font.SysFont('Comic Sans MS', 120)


    textsurface = myfont.render('Quest Hunter', False, (0, 0, 0))

    displaySurface.blit(backGround, (0,0))

    # This will display the text on the screen
    displaySurface.blit(textsurface, (300,100))

    warrior.draw(displaySurface)
    pygame.transform.scale(displaySurface, (0, 0))
    pygame.display.update()


#mainloop
warrior = player(500, 500, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and warrior.x > warrior.vel:
        warrior.x -= warrior.vel
        warrior.left = True
        warrior.right = False
    elif keys[pygame.K_RIGHT] and warrior.x < 1800 - warrior.width - warrior.vel:
        warrior.x += warrior.vel
        warrior.right = True
        warrior.left = False
    else:
        warrior.right = False
        warrior.left = False
        warrior.walkCount = 0

    if not(warrior.isJump):
        if keys[pygame.K_SPACE]:
            warrior.isJump = True
            warrior.right = False
            warrior.left = False
            warrior.walkCount = 0
    else:
        if warrior.jumpCount >= -10:
            neg = 1
            if warrior.jumpCount < 0:
                neg = -1
            warrior.y -= (warrior.jumpCount ** 2) * 0.5 * neg
            warrior.jumpCount -= 1
        else:
            warrior.isJump = False
            warrior.jumpCount = 10

    rePlayWindow()

pygame.quit()
