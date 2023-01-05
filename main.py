# pip install pygame

import pygame as pyg
import random
import math

enemyImg = pyg.image.load('img/enemy.png')
playerImg = pyg.image.load('img/space-invaders.png')
bgSpaceImg = pyg.image.load('img/bg-space.jpg')
bulletImg = pyg.image.load('img/bullett.png')
score = 0

bullet_state = 'ready'  # ready ->can't see bullet, Fire -> bullet moving


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


def isCrash(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-enemyY, 2)) +
                         (math.pow(bulletX-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


if __name__ == '__main__':
    playerX, playerY = 370, 480
    playerX_change, playerY_change = 0, 0

    enemyX, enemyY = random.randint(0, 735), random.randint(50, 150)
    enemyX_change, enemyY_change = 0.3, 30

    bulletX, bulletY = 0, 480
    bulletX_change, bulletY_change = 0, 1

    pyg.init()
    # space-invaders.png
    screen = pyg.display.set_mode((800, 600))    # creating screen

    #icon and logo
    pyg.display.set_caption("Gaurav's Game")
    logo = pyg.image.load('img/logo.png')
    pyg.display.set_icon(logo)

    # Game loop
    running = True
    while running:
        screen.fill((104, 104, 104))        # Screen color
        screen.blit(bgSpaceImg, (0, 0))
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False

            # checking for key pressed or not (left and rigth)
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:  # left arrow is pressed
                    playerX_change -= 0.5
                if event.key == pyg.K_RIGHT:  # right arrow is pressed
                    playerX_change += 0.5

                if event.key == pyg.K_SPACE:
                    if bullet_state == 'ready':
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT:
                    playerX_change = 0

        if(isCrash(bulletX, bulletY, enemyX, enemyY)):
            bullet_state = 'ready'
            bulletY = 480
            score += 1
            print(score)
            enemyX = random.randint(0, 735)
            enemyY = random.randint(50, 150)

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        enemyX += enemyX_change
        if enemyX <= 0:
            enemyX_change = 0.3
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -0.3
            enemyY += enemyY_change

        if bulletY <= 0:
            bulletY, bullet_state = 480, "ready"

        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        enemy(enemyX, enemyY)

        pyg.display.update()
