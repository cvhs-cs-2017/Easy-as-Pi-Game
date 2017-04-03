import pygame
import time
import random

pygame.init()

wind_leng = 800
wind_high = 600

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

Display = pygame.display.set_mode((wind_leng,wind_high))
pygame.display.set_caption('The Life of a Robot')
clock =  pygame.time.Clock()

main_robot = pygame.image.load('MainRobot.png')
tree = pygame.image.load('Tree.png')

def ground():
    pygame.draw.rect(Display, (0, 123, 12), [-200,560,1000,50])

def MainRobot():
    Display.blit(main_robot,(400,480))

def Tree(x):
    Display.blit(tree,(x,150))

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
    treex = random.randrange(-200,(wind_leng-200))
    tree2x = random.randrange(-100,(wind_leng-200))
    changex = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changex = 3
                elif event.key == pygame.K_RIGHT:
                    changex = -3
            if event.type == pygame. KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changex = 0

        treex += changex
        tree2x += changex
        Display.fill(white)
        ground()
        Tree(treex)
        Tree(tree2x)
        MainRobot()
        
        pygame.display.update()
        clock.tick(60)

GameLoop()

pygame.quit()
quit()
