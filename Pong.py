import pygame
import time
import random
pygame.init()
windleng = 600
windhigh  = 600
black = (0,0,0)
white = (255,255,255)
gray = (100,100,100)
Display = pygame.display.set_mode((windleng,windhigh))
pygame.display.set_caption('Pong')
clock =  pygame.time.Clock()
xball = 292.5

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,icol,acol,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Display,acol,(x,y,w,h))
        message_display(msg,"freesansbold.ttf",25,icol,(x+(w/2)),(y+(h/2)))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(Display,icol,(x,y,w,h))
        message_display(msg,"freesansbold.ttf",25,acol,(x+(w/2)),(y+(h/2)))

def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def message_display(text2, font, fsize, tcolor, x, y):
    words = pygame.font.Font(font, fsize)
    TextSurf, TextRect = text_objects(text2, words, tcolor)
    TextRect.center = ((x),(y))
    Display.blit(TextSurf, TextRect)

def player1rect(y1):
    pygame.draw.rect(Display, white, [15,y1,17,80])
def player2rect(y2):
    pygame.draw.rect(Display, white, [575,y2,17,80])
def ball(ballx,bally):
    pygame.draw.rect(Display, white, [ballx,bally,15,15])

def instructions():
    instruc = True
    while instruc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Display.fill(black)
        message_display("In 2 player mode:", "freesansbold.ttf", 30, white, 300, 20)
        message_display("Player 1 (left): use w and s to move paddle up and down.", "freesansbold.ttf", 20, white, 300, 45)
        message_display("Player 2 (right): use up arrow and down arrow to move paddle", "freesansbold.ttf", 20, white, 300, 70)
        message_display("up and down.", "freesansbold.ttf", 20, white, 300, 88)
        message_display("In 1 player mode:", "freesansbold.ttf", 30, white, 300, 150)
        message_display("You are the left paddle.", "freesansbold.ttf", 20, white, 300, 175)
        message_display("Use up arrow and down arrow to move paddle up and down.","freesansbold.ttf", 20, white, 300, 200)
        button("2 PLAYER",150,250,300,50,white,gray,counter)
        button("1 PLAYER",150,320,300,50,white,gray,counterAI)
        button("QUIT",150,390,300,50,white,gray,quitgame)
        pygame.display.update()
        clock.tick(15)

def intro():
    intr = True
    while intr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Display.fill(black)
        message_display("PONG","PongFont.ttf",100,white,300,200)
        button("2 PLAYERS",150,310,300,50,white,gray,counter)
        button("1 PLAYER",150,380,300,50,white,gray,counterAI)
        button("INSTRUCTIONS",150,450,300,50,white,gray,instructions)
        button("QUIT",150,520,300,50,white,gray,quitgame)
        pygame.display.update()
        clock.tick(15)

def counter():
    Display.fill(black)
    message_display("3","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("2","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("1","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("GO!","PongFont.ttf",270,white,300,300)
    pygame.display.update()
    time.sleep(1)
    gameloop()

def counterAI():
    Display.fill(black)
    message_display("3","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("2","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("1","PongFont.ttf",300,white,300,300)
    pygame.display.update()
    time.sleep(1)
    Display.fill(black)
    message_display("GO!","PongFont.ttf",270,white,300,300)
    pygame.display.update()
    time.sleep(1)
    gameloopAI()

def winAI():
    if xball < 0:
        compwin = True
        while compwin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            Display.fill(black)
            message_display("You lost","freesansbold.ttf",100,white,300,250)
            button("RESTART",150,330,300,50,white,gray,counterAI)
            button("2 PLAYERS",150,400,300,50,white,gray,counter)
            button("QUIT",150,470,300,50,white,gray,quitgame)
            pygame.display.update()
            clock.tick(15)
    elif xball+15 > 600:
        player = True
        while player:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            Display.fill(black)
            message_display("You won","freesansbold.ttf",100,white,300,250)
            button("RESTART",150,330,300,50,white,gray,counterAI)
            button("2 PLAYERS",150,400,300,50,white,gray,counter)
            button("QUIT",150,470,300,50,white,gray,quitgame)
            pygame.display.update()
            clock.tick(15)


def win():
    if xball < 0:
        p2win = True
        while p2win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            Display.fill(black)
            message_display("Player 2 wins!","freesansbold.ttf",60,white,300,250)
            button("RESTART",150,330,300,50,white,gray,counter)
            button("1 PLAYER",150,400,300,50,white,gray,counterAI)
            button("QUIT",150,470,300,50,white,gray,quitgame)
            pygame.display.update()
            clock.tick(15)
    elif xball+15 > 600:
        p1win = True
        while p1win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            Display.fill(black)
            message_display("Player 1 wins!","freesansbold.ttf",60,white,300,250)
            button("RESTART",150,330,300,50,white,gray,counter)
            button("1 PLAYER",150,400,300,50,white,gray,counterAI)
            button("QUIT",150,470,300,50,white,gray,quitgame)
            pygame.display.update()
            clock.tick(15)

def gameloopAI():
    global xball
    xball = 292.5
    hits = 0
    target = 5
    player1y = 300-(75/2)
    computery = 300-(75/2)
    yball = 292.5
    xballchange = -3
    yballchange = random.randrange(-1,1)
    player1change = 0
    computerchange = 0
    Exit = False
    while not Exit:
        if xball < 0 or (xball+15) > 600:
            Exit = True
            winAI()
        if yball < 0 or yball > 585:
            yballchange *= -1
        if xballchange < 0 or computery < -25 or computery > 500:
            computerchange = 0
        if xballchange > 0:
            if player1y <= computery:
                hitspot = random.randrange(40,88)
                if (yball+7.5) > (computery+hitspot):
                    computerchange = 3
                if (yball+7.5) < (computery+hitspot):
                    computerchange = -3
                if (yball+7.5) == (computery+hitspot):
                    if yballchange > 0:
                        computerchanage = 3
                    if yballchange < 0:
                        computerchange = -3
                    else:
                        computerchange = 0
            elif player1y > computery:
                hitspot = random.randrange(-8,40)
                if (yball+7.5) > (computery+hitspot):
                    computerchange = 3
                if (yball+7.5) < (computery+hitspot):
                    computerchange = -3
                if (yball+7.5) == (computery+hitspot):
                    if yballchange > 0:
                        computerchanage = 3
                    if yballchange < 0:
                        computerchange = -3
                    else:
                        computerchange = 0
            
        if (xball < 30 and ((player1y-10) < yball < (player1y+9.375))) or (xball > 560 and ((computery-10) < yball < (computery+9.375))):
            xballchange *= -1
            yballchange = -3
            hits += 1
        if (xball < 30 and ((player1y+9.3751) < yball < (player1y+18.75))) or (xball > 560 and ((computery+9.2751) < yball < (computery+18.75))):
            xballchange *= -1
            yballchange = -2.5
            hits += 1
        if (xball < 30 and ((player1y+18.751) < yball < (player1y+28.125))) or (xball > 560 and ((computery+18.751) < yball < (computery+28.125))):
            xballchange *= -1
            yballchange = -2
            hits += 1
        if (xball < 30 and ((player1y+28.1251) < yball < (player1y+37.5))) or (xball > 560 and ((computery+28.1251) < yball < (computery+37.5))):
            xballchange *= -1
            yballchange = -1
            hits += 1
        if (xball < 30 and ((player1y+37.501) < yball < (player1y+42.5))) or (xball > 560 and ((computery+37.501) < yball < (computery+42.5))):
            xballchange *= -1
            yballchange = 0
            hits += 1
        if (xball < 30 and ((player1y+42.501) < yball < (player1y+51.875))) or (xball > 560 and ((computery+42.501) < yball < (computery+51.875))):
            xballchange *= -1
            yballchange = 1
            hits += 1
        if (xball < 30 and ((player1y+51.876) < yball < (player1y+61.25))) or (xball > 560 and ((computery+51.876) < yball < (computery+61.25))):
            xballchange *= -1
            yballchange = 2
            hits += 1
        if (xball < 30 and ((player1y+61.251) < yball < (player1y+70.625))) or (xball > 560 and ((computery+61.251) < yball < (computery+70.625))):
            xballchange *= -1
            yballchange = 2.5
            hits += 1
        if (xball < 30 and ((player1y+70.626) < yball < (player1y+90))) or (xball > 560 and ((computery+70.626) < yball < (computery+90))):
            xballchange *= -1
            yballchange = 3
            hits += 1
        if hits == target:
            if xballchange >= 0:
                xballchange += .25
            else:
                xballchange -= .25
            target *=2
        if player1y < 0 or player1y > 525:
            player1change = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1change = -3
                if event.key == pygame.K_DOWN:
                    player1change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player1change = 0
                if event.key == pygame.K_DOWN:
                    player1change = 0
        Display.fill(black)
        yball += yballchange
        xball += xballchange
        computery += computerchange
        player1y += player1change
        player1rect(player1y)
        player2rect(computery)
        ball(xball,yball)
        pygame.display.update()
        clock.tick(100)
    
def gameloop():
    global xball
    xball = 292.5
    hits = 0
    target = 5
    player1y = 300-(75/2)
    player2y = 300-(75/2)
    yball = 292.5
    choosedir = random.randrange(0,1000)
    if choosedir % 2 == 0:
        xballchange = -3
    else:
        xballchange = 3
    yballchange = random.randrange(-2,2)
    player1change = 0
    player2change = 0
    Exit = False
    
    while not Exit:
        if xball < 0 or (xball+15) > 600:
            Exit = True
            win()
        if hits == target:
            if xballchange >= 0:
                xballchange += .25
            else:
                xballchange -= .25
            target += 5
        if yballchange > 4 or yballchange < -4:
            yballchange = random.randrange(-4,4)
        if yball < 0 or yball > 585:
            yballchange *= -1
        if (xball < 30 and ((player1y-5) < yball < (player1y+9.375))) or (xball > 560 and ((player2y-5) < yball < (player2y+9.375))):
            xballchange *= -1
            yballchange = -3.5
            hits += 1
        if (xball < 30 and ((player1y+9.3751) < yball < (player1y+18.75))) or (xball > 560 and ((player2y+9.2751) < yball < (player2y+18.75))):
            xballchange *= -1
            yballchange = -3
            hits += 1
        if (xball < 30 and ((player1y+18.751) < yball < (player1y+28.125))) or (xball > 560 and ((player2y+18.751) < yball < (player2y+28.125))):
            xballchange *= -1
            yballchange = -2
            hits += 1
        if (xball < 30 and ((player1y+28.1251) < yball < (player1y+37.5))) or (xball > 560 and ((player2y+28.1251) < yball < (player2y+37.5))):
            xballchange *= -1
            yballchange = -1
            hits += 1
        if (xball < 30 and ((player1y+37.501) < yball < (player1y+42.5))) or (xball > 560 and ((player2y+37.501) < yball < (player2y+42.5))):
            xballchange *= -1
            yballchange = 0
            hits += 1
        if (xball < 30 and ((player1y+42.501) < yball < (player1y+51.875))) or (xball > 560 and ((player2y+42.501) < yball < (player2y+51.875))):
            xballchange *= -1
            yballchange = 1
            hits += 1
        if (xball < 30 and ((player1y+51.876) < yball < (player1y+61.25))) or (xball > 560 and ((player2y+51.876) < yball < (player2y+61.25))):
            xballchange *= -1
            yballchange = 2
            hits += 1
        if (xball < 30 and ((player1y+61.251) < yball < (player1y+70.625))) or (xball > 560 and ((player2y+61.251) < yball < (player2y+70.625))):
            xballchange *= -1
            yballchange = 3
            hits += 1
        if (xball < 30 and ((player1y+70.626) < yball < (player1y+85))) or (xball > 560 and ((player2y+70.626) < yball < (player2y+85))):
            xballchange *= -1
            yballchange = 3.5
            hits += 1
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
                    player1change = -3
                if event.key == pygame.K_s:
                    player1change = 3
                if event.key == pygame.K_UP:
                    player2change = -3
                if event.key == pygame.K_DOWN:
                    player2change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1change = 0
                if event.key == pygame.K_s:
                    player1change = 0
                if event.key == pygame.K_UP:
                    player2change = 0
                if event.key == pygame.K_DOWN:
                    player2change = 0
        xball += xballchange
        yball += yballchange
        player1y += player1change
        player2y += player2change
        Display.fill(black)
        player1rect(player1y)
        player2rect(player2y)
        ball(xball,yball)
        pygame.display.update()
        clock.tick(100)

intro()
