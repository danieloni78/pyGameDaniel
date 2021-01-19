import pygame
import player
import enemy
import attackParticles
import sys
import random






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

#Set the amount of time the game idles after every action
waitingAmount = 120


lost = False
won = False

screen = pygame.display.set_mode([screen_width, screen_height])

turnOrder = []


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
    global waitingAmount
    global turnOrder
    playerStarting = False
    counter = 0
    waitingCounter = 0

    clock = pygame.time.Clock()
    pygame.display.set_caption("WIP Project: pyGame by Daniel Wetzel")

    if random.randint(0,1) == 0:
        playerStarting = True
        turnOrder = [player.monsterList[0], enemy.monsterList[0], player.monsterList[1], enemy.monsterList[1], player.monsterList[2], enemy.monsterList[2]]

    else:
        playerStarting = False
        turnOrder = [enemy.monsterList[0], player.monsterList[0], enemy.monsterList[1], player.monsterList[1], enemy.monsterList[2], player.monsterList[2]]

    target = turnOrder[1]

    length = len(turnOrder)
    go = True

    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if  waitingCounter > waitingAmount:

            if counter >= length:
                counter = 0

            if player.isAttacking() == False:

                if enemy.isAttacking() == False:

                    #If the turning monster is dead skip to the next of the team if there still is one
                    while turnOrder[counter].isDead() and not player.isDead() and not enemy.isDead():

                        if counter == length-1:
                            counter = 1

                        elif counter == length-2:
                            counter = 0

                        else:
                            counter += 2


                    if turnOrder[counter].player:
                        target = enemy.getNextTarget()

                    else:
                        target = player.getNextTarget()

                    turnOrder[counter].attack(target)
                    counter += 1
                    waitingCounter = 0







        clock.tick(fps)

        if player.isDead():
            go = False
        if enemy.isDead():
            go = False

        attackParticles.hanldeAttacks()
        printScreen()

        waitingCounter += 1









