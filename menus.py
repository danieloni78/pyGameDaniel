import pygame
import sys
import monsters
import myGame
import copy

#Setup screen size
screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

#load font
font = pygame.font.SysFont(None, 30)

#Load menu textures
skipImg = pygame.image.load("textures/skip.png")
startImg = pygame.image.load("textures/start.png")
selectGreyImg = pygame.image.load("textures/selectGrey.png")
selectYellowImg = pygame.image.load("textures/selectYellow.png")
startGreyImg = pygame.image.load("textures/startGrey.png")
resetImg = pygame.image.load("textures/reset.png")
lockImg = pygame.image.load("textures/locked.png")

oneImage = pygame.image.load("textures/1.png")
twoImage = pygame.image.load("textures/2.png")
threeImage = pygame.image.load("textures/3.png")


bronzeText = font.render("BRONZE", True, (0, 0, 0))
silverText = font.render("SILVER", True, (0, 0, 0))
goldText = font.render("GOLD", True, (0, 0, 0))
bronzeImg = [pygame.image.load("textures/medals/bronze/1.png"),
             pygame.image.load("textures/medals/bronze/2.png"),
             pygame.image.load("textures/medals/bronze/3.png"),
             pygame.image.load("textures/medals/bronze/4.png"),
             pygame.image.load("textures/medals/bronze/5.png"),
             pygame.image.load("textures/medals/bronze/6.png")]
bronzeTics = 0
silverImg = [pygame.image.load("textures/medals/silver/1.png"),
             pygame.image.load("textures/medals/silver/2.png"),
             pygame.image.load("textures/medals/silver/3.png"),
             pygame.image.load("textures/medals/silver/4.png"),
             pygame.image.load("textures/medals/silver/5.png"),
             pygame.image.load("textures/medals/silver/6.png")]
silverTics = 0
goldImg =   [pygame.image.load("textures/medals/gold/1.png"),
             pygame.image.load("textures/medals/gold/2.png"),
             pygame.image.load("textures/medals/gold/3.png"),
             pygame.image.load("textures/medals/gold/4.png"),
             pygame.image.load("textures/medals/gold/5.png"),
             pygame.image.load("textures/medals/gold/6.png")]
goldTics = 0

pwrUp = pygame.image.load("textures/pwrUp.png")
exitButton = pygame.image.load("textures/exit.png")

chooseTeamMsg = pygame.image.load("textures/chooseTeamMsg.png")
selectOrderMsg = pygame.image.load("textures/selectOrder.png")
selectLeague = pygame.image.load("textures/selectLeague.png")


#Initialize pygame and setup the window
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
#Setup Frames per Second
fps = 60
#Setup Selection Time in Seconds
selectionTime = 30

#List of all starting monster id's
startingMonsters = [[0, 1, 2, 3, 5, 6, 7, 40],
                    [37, 43, 54, 56, 58, 26, 27, 28],
                    [4, 65, 62, 50, 48, 35, 32, 29]]

#List of the initially selected monsters
monsterList = [[], [], []]
selectedMonsters = [monsters.monster(0, False, 0, 0), monsters.monster(37, False, 0, 0), monsters.monster(4, False, 0, 0)]

#Display values for the monsters
monstSize = 100
borderDistanceX = 50
borderDistanceY = 300
displayDistance = monstSize + borderDistanceX

#Tics for the animated sprites
dynamicTics = [0, 0, 0]
dynamicTicsSelect = [0, 0, 0]

#Set a default monster list array.
# First value of each entry states whether the monster in the order selection screen.
# Second value of each entry contains the monster object
chosen = [[False, monsters.monster(0, False, 0, 0)], [False, monsters.monster(37, False, 0, 0)], [False, monsters.monster(4, False, 0, 0)]]

#Select the initial team
def selectTeam():
    global chosen
    global monsterList

    time = selectionTime
    frames = 0

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

        #Render the Seconds
        seconds = int (frames / fps)
        secondsRender = font.render(f'{(time - seconds)} Seconds left', True, (0, 0, 0))

        #Load Background
        screen.fill((255,255,230))
        screen.blit(chooseTeamMsg, (100, 100))

        #Load Time
        screen.blit(secondsRender,(20, 20))

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

            #Draw selection Rectangle
            pygame.draw.rect(screen, (255, 0, 0), rectSelect, 3)

            if chosen[line][0] == True:

                    #Print Menu Image of the monster into rectangle
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

        #Timer Runs up
        if seconds >= time:
            go = False


        clock.tick(fps)
        pygame.display.update()
        frames +=1


    return selectedMonsters


#Select the order of the players team with a given monster list (mList)
def selectOrder(mList):
    global selectedMonsters
    global chosen

    time = selectionTime
    frames = 0

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

        #Render the Seconds
        seconds = int (frames / fps)
        secondsRender = font.render(f'{(time - seconds)} Seconds left', True, (0, 0, 0))

        # Load Background
        screen.fill((255, 255, 230))
        screen.blit(selectOrderMsg, (100, 100))
        screen.blit(secondsRender, (20,20))

        #Draw Selection Rectanles
        rectSelect1 = pygame.Rect(400, 400, 110, 110)
        rectSelect2 = pygame.Rect(545, 400, 110, 110)
        rectSelect3 = pygame.Rect(690, 400, 110, 110)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect1, 3)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect2, 3)
        pygame.draw.rect(screen, (255, 0, 0), rectSelect3, 3)

        screen.blit(oneImage, (405, 300))
        screen.blit(twoImage, (550, 300))
        screen.blit(threeImage, (695, 300))


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
                    #Setup the monsters
                    myGame.set_firstMon(chosen[0][1], chosen[0][1].select)
                    myGame.set_secMon(chosen[1][1], chosen[1][1].select)
                    myGame.set_lastMon(chosen[2][1], chosen[2][1].select)
                    #start the game
                    myGame.new()
                    go = False
            else:
                screen.blit(lockImg, mousePos)


        else:
            # set normal cursor
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


        if seconds >= time:
            #Reset the order if not all the monsters were selected
            if chosen[0][0] == True and chosen[1][0] == True and chosen[2][0] == True:
                # Setup the monsters
                #Player selected all monsters, but did not click start
                myGame.set_firstMon(chosen[0][1], chosen[0][1].select)
                myGame.set_secMon(chosen[1][1], chosen[1][1].select)
                myGame.set_lastMon(chosen[2][1], chosen[2][1].select)

            else:
                #Not all monsters were selected
                myGame.set_firstMon(backupMonstList[0], backupMonstList[0].select)
                myGame.set_secMon(backupMonstList[1], backupMonstList[1].select)
                myGame.set_lastMon(backupMonstList[2], backupMonstList[2].select)

            #Start Game
            myGame.new()

            go = False


        clock.tick(fps)
        pygame.display.update()
        frames += 1


#Select the enemy league
def selectEnemy():
    global bronzeTics, silverTics, goldTics

    screen = pygame.display.set_mode([screen_width, screen_height])

    time = selectionTime
    frames = 0

    pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Choose your Enemy...')
    clock = pygame.time.Clock()

    mbDown = False

    go = True

    while go:

        #reset tics if out of range
        if bronzeTics > 41:
            bronzeTics = 0
        if silverTics > 41:
            silverTics = 0
        if goldTics > 41:
            goldTics = 0

        # show mouse
        pygame.mouse.set_visible(True)

        #Render the Seconds
        seconds = int (frames / fps)
        secondsRender = font.render(f'{(time - seconds)} Seconds left', True, (0, 0, 0))

        #Load Background
        screen.fill((255,255,230))
        screen.blit(selectLeague, (200, 100))
        screen.blit(secondsRender, (20,20))

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
        rectSelect1 = pygame.Rect(150, 450, 150, 150)
        rectSelect2 = pygame.Rect(525, 450, 150, 150)
        rectSelect3 = pygame.Rect(900, 450, 150, 150)
        #pygame.draw.rect(screen, (0, 255, 50), rectSelect1, 100)
        #pygame.draw.rect(screen, (255, 255, 0), rectSelect2, 100)
        #pygame.draw.rect(screen, (255, 0, 0), rectSelect3, 100)

        screen.blit(bronzeText, (179, 700))
        screen.blit(silverText, (564, 700))
        screen.blit(goldText, (945, 700))


        if rectSelect1.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            #Print Rotating Medal
            screen.blit(bronzeImg[bronzeTics // 7], (150, 450))
            bronzeTics += 1

            #Print static medals
            screen.blit(silverImg[0], (525, 450))
            screen.blit(goldImg[0], (900, 450))
            silverTics = 0
            goldTics = 0

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(0)

                # Player wants to Start
                go = False

        elif rectSelect2.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Print Rotating Medal
            screen.blit(silverImg[silverTics // 7], (525, 450))
            silverTics += 1

            # Print static medals
            screen.blit(bronzeImg[0], (150, 450))
            screen.blit(goldImg[0], (900, 450))
            bronzeTics = 0
            goldTics = 0

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(1)

                # Player wants to Start
                go = False

        elif rectSelect3.collidepoint(mousePos):
            # set cursor to a hand
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

            # Print Rotating Medal
            screen.blit(goldImg[goldTics // 7], (900, 450))
            goldTics += 1

            # Print static medals
            screen.blit(silverImg[0], (525, 450))
            screen.blit(bronzeImg[0], (150, 450))
            bronzeTics = 0
            silverTics = 0

            # Player clicked on the Button
            if mbDown:
                # Player wants to Start
                myGame.set_Enemy(2)

                # Player wants to Start
                go = False

        else:
            # set normal cursor
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # Print static medals
            screen.blit(bronzeImg[0], (150, 450))
            screen.blit(silverImg[0], (525, 450))
            screen.blit(goldImg[0], (900, 450))
            bronzeTics = 0
            silverTics = 0
            goldTics = 0


        if seconds >= time:
            # Set Default Enemy
            myGame.set_Enemy(0)
            # End loop
            go = False


        clock.tick(fps)
        pygame.display.update()
        frames += 1

