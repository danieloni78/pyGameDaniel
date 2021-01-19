import pygame
import player
import enemy
import attackParticles
import sys
import printFunctions





#Textures
background = pygame.image.load("textures/background.png")
backPanel = pygame.image.load("textures/panel.png")
screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel



#Chose System Font
#font = pygame.font.SysFont('Arial', 26)


#Variables
fps = 60
firstMonst = ('Machamp', 1)
firstMonstNr = 0
secondMonst = ('Mewtwo', 2)
secondMonstNr = 1
lastMonst = ('Gengar', 3)
lastMonstNr = 2

startingCounter = 120

lost = False
won = False

screen = pygame.display.set_mode([screen_width, screen_height])




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
    screen.blit(backPanel, (0, screen_backImg))

    player.printPlayerMonsters()
    enemy.printEnemyMonsters()
    for a in attackParticles.currentParticles:
        a.printAttack()

    pygame.display.update()


def starten():
    #global font
    global startingCounter
    counter = 0
    counter2 = 0

    clock = pygame.time.Clock()
    pygame.display.set_caption("WIP Project: pyGame by Daniel Wetzel")


    go = True

    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        if counter > startingCounter:
            while counter2 < 1:
                player.monsterList[0].attack()
                player.monsterList[1].attack()
                player.monsterList[2].attack()
                counter2 += 1

        counter +=1


        clock.tick(fps)
        attackParticles.hanldeAttacks()
        printScreen()







