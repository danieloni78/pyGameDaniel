import pygame
import player
import enemy
import sys





#Textures
background = pygame.image.load("textures/background.png")


#Variables
fps = 60
firstMonst = ('Machamp', 1)
firstMonstNr = 0
secondMonst = ('Mewtwo', 2)
secondMonstNr = 1
lastMonst = ('Gengar', 3)
lastMonstNr = 2

lost = False
won = False

screen = pygame.display.set_mode([1200, 595])


def new(fM, sM, lM):
    global won
    global lost
    global firstMonst, secondMonst, lastMonst
    global firstMonstNr, secondMonstNr, lastMonstNr

    won = False
    lost = False

    firstMonst = fM
    firstMonstNr = fM[1]
    secondMonst = sM
    secondMonstNr = sM[1]
    lastMonst = lM
    lastMonstNr = lM[1]

    player.setMonsters(firstMonstNr, secondMonstNr, lastMonstNr)
    enemy.setMonsters(firstMonstNr, secondMonstNr, lastMonstNr)
    starten()


def printScreen():

    screen.blit(background, (0, 0))

    player.printPlayerMonsters()
    enemy.printEnemyMonsters()

    pygame.display.update()


def starten():


    clock = pygame.time.Clock()
    pygame.display.set_caption("WIP Project: pyGame by Daniel Wetzel")


    go = True

    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        clock.tick(fps)

        printScreen()







