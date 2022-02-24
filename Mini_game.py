import pygame
import random
import math
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((1000,600))


#BACKGROUND
background = pygame.image.load("back.png")


#BACKGROUND SOUND
mixer.music.load("background.wav")
mixer.music.play(-1)

#TITLE AND ICON 
pygame.display.set_caption("Pro player 2023")
pygame.display.set_icon(pygame.image.load("player1.png"))

#PLAYER
playerimg = pygame.image.load("player.png")
playerX = 457
playerY = 190

playerX_change = 0





#Defender
defenderimg = pygame.image.load("pic50.png")
defenderX = random.randint(0,0)
defenderY = random.randint(400, 500)

defenderX_change = 0.5
defenderY_change = 0


#Football
footballimg = pygame.image.load("try.png")
footballX = 0
footballY = 190
footballX_change = 0
footballY_change = -2
football_state = "ready"



#SCORE
score_value = 0
font = pygame.font.Font("freesansbold.ttf",40)

textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf",70)


def show_score(x,y):
    score = font.render("Fails :" + str(score_value),True, (0,0,0))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (400,350))

def player(x,y):
    screen.blit(playerimg, (x, y))


def defender(x,y):
    screen.blit(defenderimg, (x, y))

def shoot_ball(x,y):
    global football_state
    football_state = "shoot"
    screen.blit(footballimg, (x + 16,y + 10))

def isCollision(defenderX,defenderY,footballX,footballY):
    distance = math.sqrt((math.pow(defenderX-footballX,2)) + (math.pow(defenderY-footballY,2)))
    if distance < 27:
        return True
    else:
        return False









#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if football_state is "ready":
                    footballX = playerX
                    shoot_ball(footballX,footballY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            

    screen.fill((0, 100, 0))
    screen.blit(background, (0,0))
    playerX += playerX_change
  #PLAYER MOVEMENT
    if playerX <= 0:
        playerX = 0
    elif playerX >= 900:
        playerX = 900


 #DEFENDER MOVEMENT

 #GAME OVER
    if score_value >= 3:
        defenderX = 2000
        defenderY = 2000
        defenderX_change = 0
        playerX_change = 0
        game_over_text()

    defenderX += defenderX_change

    if defenderX <= 300:
        defenderX_change = 1.9
    elif defenderX >= 580:
        defenderX_change = -1.9

#FOOTBALL MOVEMENT
    if footballY >= 990:
        footballY = 190
        football_state = "ready"
    if football_state is "shoot":
        shoot_ball(playerX, footballY)
        footballY-= footballY_change

    #COLLISION

    collision  = isCollision(defenderX,defenderY,footballX,footballY)
    if collision:
        footballY = 190
        football_state = "ready"
        score_value += 1








    player(playerX, playerY)
    show_score(textX,textY)
    defender(defenderX, defenderY)
    pygame.display.update()