import pygame
import time
import random

pygame.init()
wind_leng = 800
wind_high = 600

black = (0,0,0)
white = (255,255,255)
sky_blue = (135,206,235)
dark_button = (128,128,128)
button_gray = (200,200,200)

Display = pygame.display.set_mode((wind_leng,wind_high))
pygame.display.set_caption('Robot Adventures')
clock =  pygame.time.Clock()

main_robot = pygame.image.load('MainRobot.png')
treepic = pygame.image.load('Tree.png')
cloudpic = pygame.image.load('Cloud.png')
sunpic = pygame.image.load('Sun.png')

def ground():
    pygame.draw.rect(Display, (0, 123, 12), [-200,560,1000,50])

def MainRobot(robx,roby):
    Display.blit(main_robot,(robx,roby))

def Tree(x,y):
    Display.blit(treepic,(x,y))

def Cloud(cloudx,cloudy):
    Display.blit(cloudpic,(cloudx,cloudy))

def Sun(sunx):
    Display.blit(sunpic,(sunx,40))

def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def timed_message_display(text2, font, fsize, sec, tcolor, x, y):
    words = pygame.font.Font(font, fsize)
    TextSurf, TextRect = text_objects(text2, words, tcolor)
    TextRect.center = ((x),(y))
    Display.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(sec)

def message_display(text2, font, fsize, tcolor, x, y):
    words = pygame.font.Font(font, fsize)
    TextSurf, TextRect = text_objects(text2, words, tcolor)
    TextRect.center = ((x),(y))
    Display.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,icol,acol,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Display,acol,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                GameLoop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(Display,icol,(x,y,w,h))
            
    message_display(msg,"freesansbold.ttf",20,black,(x+(w/2)),(y+(h/2)))

def game_intro():
    intro = True
    w,h = main_robot.get_size()
    bigw = w*3
    bigh = h*3
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Display.fill(white)
        bigMainRobot = pygame.transform.scale(main_robot,(bigw,bigh))
        Display.blit(bigMainRobot,[250,0])
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf,TextRect = text_objects('A Robot\'s Purpose',largeText,black)
        TextRect.center = ((wind_leng/2),(wind_high/2))
        Display.blit(TextSurf,TextRect)

        button("Start",250,350,300,50,button_gray,dark_button,"play")

        button("Exit",250,420,300,50,button_gray,dark_button,"quit")

        pygame.display.update()
        clock.tick(15)

def GameLoop():
    treex = random.randrange(-400,0)
    tree2x = random.randrange(0,400)
    tree3x = random.randrange(400,800)
    tree4x = random.randrange(800,1000)
    tree5x = random.randrange(-600,-400)
    tree6x = random.randrange(-900,-600)
    tree7x = random.randrange(1000, 1400)
    cloud1x = random.randrange(-400,0)
    cloud2x = random.randrange(200,250)
    cloud3x = random.randrange(750,800)
    cloud1y = random.randrange(0,50)
    cloud2y = random.randrange(-50,50)
    cloud3y = random.randrange(-50,70)
    sunx = random.randrange(0,50)
    treechangex = 0
    cloudXch = 0
    sunXch = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    treechangex = 3
                    cloudXch = 0.5
                    sunXch = 0.1
                elif event.key == pygame.K_RIGHT:
                    treechangex = -3
                    cloudXch = -0.5
                    sunXch = -0.1
            if event.type == pygame. KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    treechangex = 0
                    cloudXch = 0
                    sunXch = 0
        
        treex += treechangex
        tree2x += treechangex
        tree3x += treechangex
        tree4x += treechangex
        tree5x += treechangex
        tree6x += treechangex
        tree7x += treechangex
        cloud1x += cloudXch
        cloud2x += cloudXch
        cloud3x += cloudXch
        sunx += sunXch

        Display.fill(sky_blue)

        ground()
        Sun(sunx)
        Cloud(cloud1x,cloud1y)
        Cloud(cloud2x,cloud2y)
        Cloud(cloud3x,cloud3y)
        for tree in [tree2x,tree4x,tree5x,tree6x]:
            Tree(tree,150)
        MainRobot(400,500)
        Tree(tree3x,300)
        Tree(treex,400)
        Tree(tree7x,350)


        pygame.display.update()
        clock.tick(100)

game_intro()
GameLoop()

pygame.quit()
quit()

