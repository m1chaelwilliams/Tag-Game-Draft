import pygame as py
import random as r

py.init()
width,height = 800,800

screen = py.display.set_mode((width,height))

background = py.image.load('blackbg.png')
playerImg = py.image.load('rplayer.png')
playerImg = py.transform.scale(playerImg, (50,50))
rect = playerImg.get_rect()
rect.x = 375
rect.y = 375


vel = 10 #player moves 10 pixels for every frame of the loop
objvel = 5

#obstacle
obstacle = py.Rect(400,200,80,80) #pos x, pos y, width, height

clock = py.time.Clock()

#timer
seconds = 225
#start_ticks=py.time.get_ticks()
#assigning font and size
font = py.font.Font('ARCADECLASSIC.ttf', 100)
title_font = py.font.Font('ARCADECLASSIC.ttf', 200)
caption_font = py.font.Font('ARCADECLASSIC.ttf', 25)

wins = 0

game_status = False


def player(x,y):
    screen.blit(playerImg, rect)

def gameover():
    global game_status
    game_status = False
    screen.fill((0,0,0))
    game_over = font.render('GAME OVER', False, (255,255,255))
    screen.blit(game_over, (170,355))
    quit = caption_font.render('Press Q to Quit', False, (255,255,255))
    screen.blit(quit, (310, 450))

def start_screen():
    screen.fill((0,0,0))
    start_text = title_font.render('TAG', False, (255,255,255))
    screen.blit(start_text, (230,250))
    press_key = caption_font.render('(Press Space to Start)', False, (255,255,255))
    screen.blit(press_key, (265,460))

def gamestart():
    global game_status
    game_status = True
run = True
while run:


    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            gamestart()
    screen.fill((0,0,0))
    #seconds=(py.time.get_ticks()-start_ticks)/1000
    #text_surface = font.render(str(5-int(seconds)), False, (255,255,255))
    if game_status == True:
        seconds -= 1
    text_surface = font.render(str(int(seconds/60)), False, (255,255,255))
    screen.blit(text_surface, (375,50))


    win_count = caption_font.render(str(wins), False, (255,255,255))
    win_text = caption_font.render('Level', False, (255,255,255))
    screen.blit(win_text, (15,0))
    screen.blit(win_count, (90,0))

    userInput = py.key.get_pressed()
    if rect.x >= 25:
        if userInput[py.K_LEFT]:
            rect.x -= vel
    if rect.x <= 730:
        if userInput[py.K_RIGHT]:
            rect.x += vel
    if rect.y >= 25:
        if userInput[py.K_UP]:
            rect.y -= vel
    if rect.y <= 730:
        if userInput[py.K_DOWN]:
            rect.y += vel
    if game_status == False:
        if userInput[py.K_q]:
            py.quit()
            exit()




    #draws player
    player(rect.x, rect.y)
    #draws obstacle
    py.draw.rect(screen, (205,205,205), obstacle)

    if game_status == False:
        start_screen()

    if rect.colliderect(obstacle):
        # py.draw.rect(screen, (255, 255, 0), rect)
        rect.x = r.randint(50,730)
        rect.y = r.randint(50,730)
        obstacle.x = r.randint(50,700)
        obstacle.y = r.randint(50,700)
        wins += 1
        vel += 1
        seconds = 225
    else:
        if seconds<1:
            gameover()

    clock.tick(60)
    py.display.update()
