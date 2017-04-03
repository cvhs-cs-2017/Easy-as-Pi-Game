import pygame
import time
import random

pygame.init() 
wind_leng = 800
wind_high = 600

black = (0,0,0)
white = (255,255,255)
sky_blue = (135,206,235)

Display = pygame.display.set_mode((wind_leng,wind_high))
pygame.display.set_caption('Robot Adventures')
clock =  pygame.time.Clock()

main_robot = pygame.image.load('MainRobot.png')
treepic = pygame.image.load('Tree.png')
cloudpic = pygame.image.load('Cloud.png')

def ground():
    pygame.draw.rect(Display, (0, 123, 12), [-200,560,1000,50])

def MainRobot():
    Display.blit(main_robot,(400,500))

def Tree(x,y):
    Display.blit(treepic,(x,y))

def Cloud(cloudx,cloudy):
    Display.blit(cloudpic,(cloudx,cloudy))

def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text2, font, fsize, sec, tcolor, x, y):
    words = pygame.font.Font(font, fsize)
    TextSurf, TextRect = text_objects(text2, words, tcolor)
    TextRect.center = (x,y)
    Display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(sec)

def GameLoop():    
    treex = random.randrange(-400,0)
    tree2x = random.randrange(0,400)
    tree3x = random.randrange(400,800)
    tree4x = random.randrange(800,1000)
    tree5x = random.randrange(-600,-400)
    cloud1x = random.randrange(-400,0)
    cloud2x = random.randrange(200,250)
    cloud3x = random.randrange(750,800)
    cloud1y = random.randrange(0,50)
    cloud2y = random.randrange(-50,50)
    cloud3y = random.randrange(-50,70)
    treechangex = 0
    cloudXch = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    treechangex = 3
                    cloudXch = 1
                elif event.key == pygame.K_RIGHT:
                    treechangex = -3
                    cloudXch = -1
            if event.type == pygame. KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    treechangex = 0
                    cloudXch = 0

        treex += treechangex
        tree2x += treechangex
        tree3x += treechangex
        tree4x += treechangex
        tree5x += treechangex
        cloud1x += cloudXch
        cloud2x += cloudXch
        cloud3x += cloudXch
        
        Display.fill(sky_blue)

        ground()
        Cloud(cloud1x,cloud1y)
        Cloud(cloud2x,cloud2y)
        Cloud(cloud3x,cloud3y)
        for tree in [tree2x,tree4x,tree5x]:
            Tree(tree,150)
        MainRobot()
        Tree(tree3x,300)
        Tree(treex,400)
        
        pygame.display.update()
        clock.tick(60)

GameLoop()

pygame.quit()
quit()
