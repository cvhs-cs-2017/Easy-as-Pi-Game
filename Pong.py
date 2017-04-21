import pygame
import time
import random
pygame.init()
windleng = 600
windhigh  = 600
black = (0,0,0)
white = (255,255,255)
Display = pygame.display.set_mode((windleng,windhigh))
pygame.display.set_caption('Pong')
clock =  pygame.time.Clock()
def player1rect(y1):
    pygame.draw.rect(Display, white, [15,y1,17,75])
def player2rect(y2):
    pygame.draw.rect(Display, white, [575,y2,17,75])
def ball(ballx,bally):
    pygame.draw.rect(Display, white, [ballx-(15/2),bally-(15/2),15,15])

def gameloop():
    player1y = 225
    player2y = 225
    player1change = 0
    player2change = 0
    Exit = False
    while not Exit:
        if player1y < 0 or player1y > 525:
            player1change = 0
        if player2y < 0 or player2y > 525:
            player2change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1change = -5
                if event.key == pygame.K_s:
                    player1change = 5
                if event.key == pygame.K_UP:
                    player2change = -5
                if event.key == pygame.K_DOWN:
                    player2change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1change = 0
                if event.key == pygame.K_s:
                    player1change = 0
                if event.key == pygame.K_UP:
                    player2change = 0
                if event.key == pygame.K_DOWN:
                    player2change = 0
        player1y += player1change
        player2y += player2change
        Display.fill(black)
        player1rect(player1y)
        player2rect(player2y)
        ball(300,300)
        pygame.display.update()
        clock.tick(100)

gameloop()
