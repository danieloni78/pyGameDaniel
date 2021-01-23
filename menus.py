import pygame
import sys
import monsters
import myGame
import copy

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

skipImg = pygame.image.load("textures/skip.png")
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
exitButton = pygame.image.load("textures/exit.png")

chooseTeamMsg = pygame.image.load("textures/chooseTeamMsg.png")
selectOrderMsg = pygame.image.load("textures/selectOrder.png")
selectLeague = pygame.image.load("textures/selectLeague.png")



pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
fps = 60


placeNum = 0


startingMonsters = [[0, 1, 2, 3, 5, 6, 7, 40],
                    [37, 43, 54, 56, 58, 26, 27, 28],
                    [4, 65, 62, 50, 48, 35, 32, 29]]

monsterList = [[], [], []]
selectedMonsters = [monsters.monster(0, False, 0, 0), monsters.monster(0, False, 0, 0), monsters.monster(0, False, 0, 0)]

monstSize = 100
borderDistanceX = 50
borderDistanceY = 300
displayDistance = monstSize + borderDistanceX

dynamicTics = [0, 0, 0]
dynamicTicsSelect = [0, 0, 0]

chosen = [[False, monsters.monster(0, False, 0, 0)], [False, monsters.monster(0, False, 0, 0)], [False, monsters.monster(0, False, 0, 0)]]


def selectTeam():
    global chosen
    global monsterList

    screen = pygame.display.set_mode([screen_width + 175, screen_height])

    pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Choose your Monsters...')
    clock = pygame.time.Clock()

    count1 = 0
    mbDown = False
    while count1 < len(startingMonsters):

        count2 = 0
        while count2 < len(startingMonsters[count1]):
            monsterList[count1].append(monsters.monster(startingMonsters[count1][count2], True, 0, 0))

            count2 +=1
        count1 +=1


    go = True

    while(go):

        # show mouse
        pygame.mouse.set_visible(True)



        #Load Background
        screen.fill((255,255,230))
        screen.blit(chooseTeamMsg, (100, 100))

        #Button Press Actions
        for event in pygame.event.get():
            #Close the game
            if event.type == pygame.QUIT: sys.exit()

            #Player clicked Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mbDown = True
            else:
                mbDown = False

        # get mouse position
        mousePos = pygame.mouse.get_pos()

        line = 0
        for n in startingMonsters:

            rectSelect = pygame.Rect(borderDistanceX, borderDistanceY + (displayDistance * line), 110, 110)
            pygame.draw.rect(screen, (255, 0, 0), rectSelect, 3)

            if chosen[line][0] == True:

                    #Print Menu Image of the monster
                    chosen[line][1].printMenu(True, borderDistanceX, borderDistanceY + (displayDistance * line))

            row = 0
            for m in monsterList[line]:

                if m.rect.collidepoint(mousePos):

                    #Print Menu Image of the monster
                    m.printMenu(True, borderDistanceX + displayDistance + (displayDistance * row), borderDistanceY + (displayDistance * line))

                    # Player clicked on the Button
                    if mbDown:
                        # Player selected a monster
                        chosen[line][0] = True
                        chosen[line][1] = m
                        selectedMonsters[line] = m

                else:
                    # Print Menu Image of the monster
                    m.printMenu(False, borderDistanceX + displayDistance + (displayDistance * row), borderDistanceY + (displayDistance * line))


                row += 1
            line +=1

            # Load Buttons
            # StartButton (Shows only if all 3 monsters are selected)
            if chosen[0][0] == True and chosen[1][0] == True and chosen[2][0] == True:
                screen.blit(selectYellowImg, ((screen_width + 175) - 220, 20))
                startButton = pygame.Rect((screen_width + 175) - 220, 20, 200, 100)
            else:
                screen.blit(selectGreyImg, ((screen_width + 175) - 220, 20))
                startButton = pygame.Rect((screen_width + 175) - 220, 20, 200, 100)


            # Quit Button
            screen.blit(exitButton, ((screen_width + 175) - 220, 140))
            quitButton = pygame.Rect((screen_width + 175) - 220, 140, 200, 100)

            #Quits Game
            if quitButton.collidepoint(mousePos):

                # set cursor to a hand
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

                # Player clicked on the Button
                if mbDown:

                    # Player wants to Quit
                    sys.exit()

            #Starts game
            elif startButton.collidepoint(mousePos):
                if chosen[0][0] == True and chosen[1][0] == True and chosen[2][0] == True:
                    # set cursor to a hand
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                    # Player clicked on the Button
                    if mbDown:
                        # Player wants to Start
                        go = False
                else:
                    screen.blit(lockImg, mousePos)

            else:
                # set normal cursor
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)



        clock.tick(fps)
        pygame.display.update()


    return selectedMonsters


def selectOrder(mList):
    global selectedMonsters
    global chosen

    mbDown = False

    selectedMonsters = mList

    #Make a Backup of the list to Reset the method
    backupMonstList = copy.copy(mList)

    chosen[0][0] = False
    chosen[1][0] = False
    chosen[2][0] = False

    screen = pygame.display.set_mode([screen_width, screen_height])

    pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Select the fighting order...')
    clock = pygame.time.Clock()

    monPosition = 0

    go = True

    while (go):

        # show mouse
        pygame.mouse.set_visible(True)

        # Load Background
        screen.fill((255, 255, 230))
        screen.blit(selectOrderMsg, (100, 100))

        #Draw Selection Rectanles
        rectSelect1 = pygame.Rect(400, 400, 110, 110)
        rectSelect2 = pygame.Rect(545, 400, 110, 110)
        rectSelect3 = pygame.Rect(690, 400, 110, 110)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect1, 3)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect2, 3)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect3, 3)

        screen.blit(num1img, (405, 300))
        screen.blit(num2img, (550, 300))
        screen.blit(num3img, (695, 300))


        #Display Chosen Monsters
        if chosen[0][0] == True:
            # Print Menu Image of the first monster
            chosen[0][1].printMenu(True, 400, 400)
        if chosen[1][0] == True:
            # Print Menu Image of the second monster
            chosen[1][1].printMenu(True, 545, 400)
        if chosen[2][0] == True:
            # Print Menu Image of the second monster
            chosen[2][1].printMenu(True, 690, 400)


        # Button Press Actions
        for event in pygame.event.get():
            # Close the game
            if event.type == pygame.QUIT: sys.exit()

            # Player clicked Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mbDown = True
            else:
                mbDown = False

        # get mouse position
        mousePos = pygame.mouse.get_pos()

        count = 0
        for m in selectedMonsters:

            if m.rect.collidepoint(mousePos):

                # Print Menu Image of the monster
                m.printMenu(True, 400 + (displayDistance * count), 600)

                # Player clicked on the Button
                if mbDown:
                    # Player selected a monster
                    chosen[monPosition][0] = True
                    chosen[monPosition][1] = m
                    selectedMonsters.remove(m)
                    monPosition += 1

                # set cursor to a hand
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            else:
                # set normal cursor
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                # Print Menu Image of the monster
                m.printMenu(False, 400 + (displayDistance * count), 600)

            count +=1


        # Load Buttons
        # StartButton (Shows only if all 3 monsters are selected)
        if chosen[0][0] == True and chosen[1][0] == True and chosen[2][0] == True:
            screen.blit(startImg, (screen_width - 220, 20))
            startButton = pygame.Rect(screen_width - 220, 20, 200, 100)
        else:
            screen.blit(startGreyImg, (screen_width - 220, 20))
            startButton = pygame.Rect(screen_width - 220, 20, 200, 100)

        # Reset Button
        screen.blit(resetImg, (screen_width - 220, 140))
        resetButton = pygame.Rect(screen_width - 220, 140, 200, 100)

        # Quit Button
        screen.blit(exitButton, (screen_width - 220, 260))
        quitButton = pygame.Rect(screen_width - 220, 260, 200, 100)

        # Quits Game
        if quitButton.collidepoint(mousePos):

            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Player clicked on the Button
            if mbDown:
                # Player wants to Quit
                sys.exit()

        #Resets Order
        elif resetButton.collidepoint(mousePos):

            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Player clicked on the Button
            if mbDown:
                # Player wants to Reset
                selectOrder(backupMonstList)


        # Starts game
        elif startButton.collidepoint(mousePos):

            if chosen[0][0] == True and chosen[1][0] == True and chosen[2][0] == True:
                # set cursor to a hand
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

                # Player clicked on the Button
                if mbDown:
                    # Player wants to Start
                    myGame.set_firstMon(chosen[0][1], chosen[0][1].select)
                    myGame.set_secMon(chosen[1][1], chosen[1][1].select)
                    myGame.set_lastMon(chosen[2][1], chosen[2][1].select)
                    myGame.new()
                    go = False
            else:
                screen.blit(lockImg, mousePos)


        else:
            # set normal cursor
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


        clock.tick(fps)
        pygame.display.update()


def selectEnemy():

    screen = pygame.display.set_mode([screen_width, screen_height])

    pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Choose your Enemy...')
    clock = pygame.time.Clock()

    mbDown = False

    go = True

    while go:

        # show mouse
        pygame.mouse.set_visible(True)

        #Load Background
        screen.fill((255,255,230))
        screen.blit(selectLeague, (200, 100))

        #Button Press Actions
        for event in pygame.event.get():
            #Close the game
            if event.type == pygame.QUIT: sys.exit()

            #Player clicked Mouse Button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mbDown = True
            else:
                mbDown = False

        # get mouse position
        mousePos = pygame.mouse.get_pos()

        #Draw Selection Rectanles
        rectSelect1 = pygame.Rect(200, 450, 110, 110)
        rectSelect2 = pygame.Rect(545, 450, 110, 110)
        rectSelect3 = pygame.Rect(890, 450, 110, 110)
        pygame.draw.rect(screen, (0, 255, 50), rectSelect1, 100)
        pygame.draw.rect(screen, (255, 255, 0), rectSelect2, 100)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect3, 100)

        screen.blit(num1img, (205, 300))
        screen.blit(num2img, (550, 300))
        screen.blit(num3img, (895, 300))


        if rectSelect1.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(0)

                # Player wants to Start
                go = False

        elif rectSelect2.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(1)

                # Player wants to Start
                go = False

        elif rectSelect3.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(2)

                # Player wants to Start
                go = False

        else:
            # set normal cursor
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

        clock.tick(fps)
        pygame.display.update()

