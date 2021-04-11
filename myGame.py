# This class is used to control the game:
# It contains functions to:
# 1. Initialize a Round
# 2. Print the game content to the screen
# 3. Run the game
# 4. Setup Monsters and enemy

# Background from: https://OpenGamersArt.org
# Pokemon Textures from TheSpritersResource: https://www.spriters-resource.com

import random
import sys
import time

import pygame

import attackParticles
import enemy
import enemyList
import menus
import player

# load font
font = pygame.font.SysFont(None, 30)

# Textures
background = [pygame.image.load("textures/backgrounds/1.png"),
              pygame.image.load("textures/backgrounds/2.png"),
              pygame.image.load("textures/backgrounds/3.png"),
              pygame.image.load("textures/backgrounds/4.png"),
              pygame.image.load("textures/backgrounds/5.png"),
              pygame.image.load("textures/backgrounds/6.png"), ]
backgroundNr = 0

backPanel = pygame.image.load("textures/panel.png")
lostImg = pygame.image.load("textures/lost.png")
wonImg = pygame.image.load("textures/win.png")
lvlUp = pygame.image.load("textures/lvlUp.png")
skipImg = pygame.image.load("textures/skip.png")
evolveImg = pygame.image.load("textures/evolveMessage.png")
startImg = pygame.image.load("textures/start.png")
selectGreyImg = pygame.image.load("textures/selectGrey.png")
selectYellowImg = pygame.image.load("textures/selectYellow.png")
startGreyImg = pygame.image.load("textures/startGrey.png")
resetImg = pygame.image.load("textures/reset.png")
lockImg = pygame.image.load("textures/locked.png")
num1img = pygame.image.load("textures/1.png")
num2img = pygame.image.load("textures/2.png")
num3img = pygame.image.load("textures/3.png")
pwrUp = pygame.image.load("textures/pwrUp.png")
tradeImg = pygame.image.load("textures/trade.png")
exitButton = pygame.image.load("textures/exit.png")
tradeInMessage = pygame.image.load("textures/tradeInMsg.png")
powerUpMsg = pygame.image.load("textures/powerUpMsg.png")

# Screen Size
screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

# Sounds
winningSound = pygame.mixer.Sound("sounds/victory.wav")
losingSound = pygame.mixer.Sound("sounds/losing.wav")

# Variables
fps = 60
selectionTime = 20

# Player's Monster Selection
firstMonstNr = 0
secondMonstNr = 0
lastMonstNr = 0

difficulty = 0

# Enemy's monster selection
eFirstMonstNr = 0
eSecondMonstNr = 0
eLastMonstNr = 0

# Set the amount of time the game idles after every action
waitingAmount = 120

rounds = 1

gameStage = 0

screen = pygame.display.set_mode([screen_width, screen_height])

turnOrder = []


# Initialize a new Round
def newRound():
    global gameStage
    global firstMonstNr, secondMonstNr, lastMonstNr

    global eFirstMonstNr, eSecondMonstNr, eLastMonstNr

    global backgroundNr

    # select random background img
    if rounds <= 6:
        backgroundNr = rounds - 1
    else:
        backgroundNr = random.randint(0, 5)

    # Set the Monsters
    player.setMonsters(firstMonstNr, secondMonstNr, lastMonstNr)
    enemy.setMonsters(eFirstMonstNr, eSecondMonstNr, eLastMonstNr)

    # Power-Up Stage - First Phase of the game round
    gameStage = 1

    # Run the game
    run()


# Function to display the content onto the screen
def printScreen():
    screen.blit(background[backgroundNr], (0, 0))
    screen.blit(backPanel, (0, screen_backImg))

    # Evolve Stage
    if gameStage == 0:
        screen.blit(evolveImg, (200, 100))
        screen.blit(skipImg, (screen_width - 220, 20))

    # PowerUp Stage
    elif gameStage == 1:
        screen.blit(powerUpMsg, (200, 100))

    # Trading Stage
    elif gameStage == 3:
        screen.blit(tradeInMessage, (200, 100))
        screen.blit(skipImg, (screen_width - 220, 20))

    player.printMonsters()
    enemy.printMonsters()
    for a in attackParticles.currentParticles:
        a.printAttack()


# Function that runs the game
def run():
    global waitingAmount
    global turnOrder
    global rounds
    global gameStage

    selTime = selectionTime
    frames = 0

    mbDown = False

    gameStage = 1

    waitingCounter = 0

    clock = pygame.time.Clock()

    # Set the monsters for player and enemy
    player.setMonsters(firstMonstNr, secondMonstNr, lastMonstNr)
    enemy.setMonsters(eFirstMonstNr, eSecondMonstNr, eLastMonstNr)

    # Choose who starts the round (Coin Flip)
    if random.randint(0, 1) == 0:
        playerTurn = 0
    else:
        playerTurn = 1

    go = True

    # Game Loop
    while go:

        pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Pokemon Battle Simulator - Round: {rounds}')

        # Get system events relevant to the game
        for event in pygame.event.get():
            # Close the game
            if event.type == pygame.QUIT: sys.exit()

            # Player clicked Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mbDown = True
            else:
                mbDown = False

        # Call the Output to the screen
        attackParticles.hanldeAttacks()
        printScreen()

        # 0 = Enemies Turn; 1 = Players Turn
        if playerTurn > 1:
            playerTurn = 0

        # If the player is dead
        if player.isDead():
            screen.fill((100, 100, 100))
            screen.blit(lostImg, (350, 165))
            pygame.display.update()
            pygame.mixer.Sound.play(losingSound)
            time.sleep(3)
            menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

        # If the enemy is dead
        elif enemy.isDead():
            screen.fill((200, 200, 200))
            screen.blit(wonImg, (350, 165))
            pygame.display.update()
            pygame.mixer.Sound.play(winningSound)
            time.sleep(3)
            rounds += 1
            gameStage = 3
            frames = 0
            set_Enemy(difficulty)
            player.restore()
            enemy.restore()

        # Switch Monster (random)
        if gameStage == 3:

            # Only alow trade in after round 5 and after that in every 2nd round
            if rounds >= 5 and rounds % 2 != 0:
                # Render the Seconds
                seconds = int(frames / fps)
                secondsRender = font.render(f'{(selTime - seconds)} Seconds left', True, (0, 0, 0))

                # Show Seconds
                screen.blit(secondsRender, (20, 20))

                sButton = pygame.Rect(screen_width - 220, 20, 200, 100)

                # show mouse
                pygame.mouse.set_visible(True)

                # get mouse position
                mousePos = pygame.mouse.get_pos()

                # if mouse is on one of the players monsters
                for pMonst in player.monsterList:

                    if pMonst.rect.collidepoint(mousePos):

                        # hide normal mouse
                        pygame.mouse.set_visible(False)

                        # Show LVL Up symbol
                        screen.blit(tradeImg, mousePos)

                        # Player clicked on the monster
                        if mbDown:

                            # Try to evolve the monster
                            selectedMonst = pMonst.switchRandom(rounds)

                            # Monster could be evolved
                            if selectedMonst:
                                gameStage = 1
                                menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

                if sButton.collidepoint(mousePos):

                    # set cursor to a hand
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

                    # Player clicked on the Button
                    if mbDown:
                        # Player wants to skip
                        gameStage = 1
                        menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

                else:
                    # set normal cursor
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if seconds >= selTime:
                    # Players time runs up
                    gameStage = 1
                    menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

            else:
                gameStage = 0

        # Battle Phase
        elif gameStage == 2:

            # hide normal mouse
            pygame.mouse.set_visible(False)

            if waitingCounter > waitingAmount:

                if player.isAttacking() == False:

                    if enemy.isAttacking() == False:

                        if playerTurn == 0:
                            target = enemy.getNextTarget()
                            player.attack(target)
                        elif playerTurn == 1:
                            target = player.getNextTarget()
                            enemy.attack(target)

                        playerTurn += 1
                        waitingCounter = 0

            waitingCounter += 1

        # Choose special Attacker
        elif gameStage == 1:
            # Render the Seconds
            seconds = int(frames / fps)
            secondsRender = font.render(f'{(selTime - seconds)} Seconds left', True, (0, 0, 0))

            # Show Seconds
            screen.blit(secondsRender, (20, 20))

            # show mouse
            pygame.mouse.set_visible(True)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # get mouse position
            mousePos = pygame.mouse.get_pos()

            # if mouse is on one of the players monsters
            for pMonst in player.monsterList:

                if pMonst.rect.collidepoint(mousePos):

                    # hide normal mouse
                    pygame.mouse.set_visible(False)

                    # Show LVL Up symbol
                    screen.blit(pwrUp, mousePos)

                    # Player clicked on the monster
                    if mbDown:
                        pMonst.turnSpecialAttacker()
                        enemy.monsterList[2].turnSpecialAttacker()
                        gameStage = 2

            if seconds >= selTime:
                # The player gets punished for not selecting in time.
                # Remove "#" to give him power up after the time is up

                # player.monsterList[2].turnSpecialAttacker()
                enemy.monsterList[2].turnSpecialAttacker()
                gameStage = 2

        # Evolve Monster
        elif gameStage == 0:
            # Render the Seconds
            seconds = int(frames / fps)
            secondsRender = font.render(f'{(selTime - seconds)} Seconds left', True, (0, 0, 0))

            # Show Seconds
            screen.blit(secondsRender, (20, 20))

            skipButton = pygame.Rect(screen_width - 220, 20, 200, 100)

            # show mouse
            pygame.mouse.set_visible(True)

            # get mouse position
            mousePos = pygame.mouse.get_pos()

            # if mouse is on one of the players monsters
            for pMonst in player.monsterList:

                if pMonst.evolvesTo != -1:

                    if pMonst.rect.collidepoint(mousePos):

                        # hide normal mouse
                        pygame.mouse.set_visible(False)

                        # Show LVL Up symbol
                        screen.blit(lvlUp, mousePos)

                        # Player clicked on the monster
                        if mbDown:

                            # Try to evolve the monster
                            selectedMonst = pMonst.evolve()

                            # Monster could be evolved
                            if selectedMonst:
                                gameStage = 1
                                menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

            if skipButton.collidepoint(mousePos):

                # set cursor to a hand
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

                # Player clicked on the Button
                if mbDown:
                    # Player wants to skip
                    gameStage = 1
                    menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

            else:
                # set normal cursor
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if seconds >= selTime:
                # Players time runs up
                gameStage = 1
                menus.selectOrder([player.monsterList[0], player.monsterList[1], player.monsterList[2]])

        clock.tick(fps)
        pygame.display.update()
        frames += 1


def set_firstMon(monster, number):
    global firstMonstNr
    firstMonstNr = number

    # Delete obsolete Instance
    del monster


def set_secMon(monster, number):
    global secondMonstNr
    secondMonstNr = number

    # Delete obsolete Instance
    del monster


def set_lastMon(monster, number):
    global lastMonstNr
    lastMonstNr = number

    # Delet Obsolete Instance
    del monster


def set_Enemy(number):
    global eFirstMonstNr, eSecondMonstNr, eLastMonstNr
    global difficulty
    global rounds

    difficulty = number

    eRounds = rounds - 1

    enemySelection = enemyList.loadEnemy(difficulty, eRounds)

    eFirstMonstNr = enemySelection[0]
    eSecondMonstNr = enemySelection[1]
    eLastMonstNr = enemySelection[2]
