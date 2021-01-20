import pygame
import pygame_menu
import player
import enemy
import attackParticles
import sys
import random
import time






#Textures
background = pygame.image.load("textures/background.png")
backPanel = pygame.image.load("textures/panel.png")
lostImg = pygame.image.load("textures/lost.png")
wonImg = pygame.image.load("textures/win.png")
screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

#Sounds
winningSound = pygame.mixer.Sound("sounds/victory.wav")
losingSound = pygame.mixer.Sound("sounds/losing.wav")



#Variables
fps = 60
firstMonst = [("Venusaur", 15)]
secondMonst = [("Blastoise", 16)]
lastMonst = [("Charizard", 17)]

eNumber = 0

eFirstMonst = [('Bulbasaur', 0)]
eSecondMonst = [('Squirtle', 1)]
eLastMonst = [('Charmander', 2)]


#Set the amount of time the game idles after every action
waitingAmount = 120

rounds = 1


screen = pygame.display.set_mode([screen_width, screen_height])

turnOrder = []


def new(fM, sM, lM):


    global won
    global lost
    global firstMonst, secondMonst, lastMonst

    global eFirstMonst, eSecondMonst, eLastMonst


    won = False
    lost = False

    firstMonst = fM
    firstMonstNr = fM[0][1]
    eFirstMonstNr = eFirstMonst[0][1]

    secondMonst = sM
    secondMonstNr = sM[0][1]
    eSecondMonstNr = eSecondMonst[0][1]

    lastMonst = lM
    lastMonstNr = lM[0][1]
    eLastMonstNr = eLastMonst[0][1]

    player.setMonsters(firstMonstNr, secondMonstNr, lastMonstNr)
    enemy.setMonsters(eFirstMonstNr, eSecondMonstNr, eLastMonstNr)
    starten()


def printScreen():



    screen.blit(background, (0, 0))
    screen.blit(backPanel, (0, screen_backImg))

    player.printPlayerMonsters()
    enemy.printEnemyMonsters()
    for a in attackParticles.currentParticles:
        a.printAttack()

    pygame.display.update()


def inGameMenu(won):



    if won:
        pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Round: {rounds}')
        setEnemy(eNumber)
        gameMenu = pygame_menu.Menu(700, 1000, 'You have won.', theme=pygame_menu.themes.THEME_BLUE)
        gameMenu.add_selector('First Monster: ',
                              [("Venusaur", 15), ('Bulbasaur (Melee)', 0), ('Squirtle (Melee)', 1), ('Charmander (Ranged)', 2),
                               ("Pikachu (Assassin)",3), ("Gastly (Assassin)", 4),("Machop (Melee)",5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12),("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_firtMon)

        gameMenu.add_selector('Second Monster: ',
                              [("Blastoise", 16), ('Squirtle (Melee)', 1), ('Bulbasaur (Melee)', 0),
                               ('Charmander (Ranged)', 2),
                               ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_secMon)

        gameMenu.add_selector('Last Monster: ',
                              [("Charizard", 17), ('Charmander (Ranged)', 2), ('Bulbasaur (Melee)', 0),
                               ('Squirtle (Melee)', 1),
                               ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_lastMon)

        gameMenu.add_button('Next Enemy', startGame)
        gameMenu.add_button('Quit', pygame_menu.events.EXIT)

        gameMenu.mainloop(screen)

    else:
        init_Enemy(None, eNumber)
        gameMenu = pygame_menu.Menu(700, 1000, 'You have lost.', theme=pygame_menu.themes.THEME_BLUE)
        gameMenu.add_selector('First Monster: ',
                              [("Venusaur", 15), ('Bulbasaur (Melee)', 0), ('Squirtle (Melee)', 1),
                               ('Charmander (Ranged)', 2),
                               ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_firtMon)

        gameMenu.add_selector('Second Monster: ',
                              [("Blastoise", 16), ('Squirtle (Melee)', 1), ('Bulbasaur (Melee)', 0),
                               ('Charmander (Ranged)', 2),
                               ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_secMon)

        gameMenu.add_selector('Last Monster: ',
                              [("Charizard", 17), ('Charmander (Ranged)', 2), ('Bulbasaur (Melee)', 0),
                               ('Squirtle (Melee)', 1),
                               ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                               ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                               ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                               ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                               ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                              onchange=set_lastMon)
        gameMenu.add_button('Try Again', startGame)
        gameMenu.add_button('Quit', pygame_menu.events.EXIT)

        gameMenu.mainloop(screen)


def starten():
    global waitingAmount
    global turnOrder
    global rounds
    counter = 0
    waitingCounter = 0

    pygame.display.set_caption(f'WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Round: {rounds}')
    clock = pygame.time.Clock()

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


                        elif turnOrder[0].isDead() and turnOrder[1].isDead() and turnOrder[3].isDead() and counter == 0:
                            i = 0
                            if i == 1:
                                counter = length-2
                            else:
                                counter = 2


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
            screen.fill((100,100,100))
            screen.blit(lostImg, (350, 165))
            pygame.display.update()
            pygame.mixer.Sound.play(losingSound)
            time.sleep(3)
            rounds = 0
            inGameMenu(False)


        if enemy.isDead():
            go = False
            screen.fill((200,200,200))
            screen.blit(wonImg, (350, 165))
            pygame.display.update()
            pygame.mixer.Sound.play(winningSound)
            time.sleep(3)
            rounds += 1
            inGameMenu(True)

        attackParticles.hanldeAttacks()
        printScreen()

        waitingCounter += 1





def set_firtMon(monster, number):
    global firstMonst
    firstMonst = monster


def set_secMon(monster, number):
    global secondMonst
    secondMonst = monster


def set_lastMon(monster, number):
    global lastMonst
    lastMonst = monster


def startGame():
    new(firstMonst, secondMonst, lastMonst)


def init_Enemy(enemy, number):
    global eNumber
    eNumber = number
    setEnemy(number)


def setEnemy(number):

    global eFirstMonst, eSecondMonst, eLastMonst



    eRounds = rounds-1
    if rounds > 3:
        eRounds = random.randint(0, 2)


    #easy
    if number == 0:

        #Enemy in the first round
        if eRounds == 0:
            eFirstMonst = [('Bulbasaur', 0)]
            eSecondMonst = [('Squirtle', 1)]
            eLastMonst = [('Charmander', 2)]

        #Enemy in the second Round
        if eRounds == 1:
            eFirstMonst = [("Ivysaur", 9)]
            eSecondMonst = [("Wartortle", 10)]
            eLastMonst = [("Charmeleon", 11)]

        #Enemy in the last Round
        if eRounds == 2:
            eFirstMonst = [("Venusaur", 15)]
            eSecondMonst = [("Blastoise", 16)]
            eLastMonst = [("Charizard", 17)]

    # Medium
    if number == 1:

        # Enemy in the first round
        if eRounds == 0:
            eFirstMonst = [("Machop", 5)]
            eSecondMonst = [("Pikachu", 3)]
            eLastMonst = [("Gastly", 4)]

        # Enemy in the second Round
        if eRounds == 1:
            eFirstMonst = [("Snorlax", 21)]
            eSecondMonst = [("Machoke", 13)]
            eLastMonst = [("Haunter", 12)]

        # Enemy in the last Round
        if eRounds == 2:
            eFirstMonst = [("Snorlax", 21)]
            eSecondMonst = [("Machamp", 19)]
            eLastMonst = [("Gengar", 18)]

    # Hard
    if number == 2:

        # Enemy in the first round
        if eRounds == 0:
            eFirstMonst = [("Snorlax", 21)]
            eSecondMonst = [("Dragonite", 20)]
            eLastMonst = [("Mewtwo", 22)]

        # Enemy in the second Round
        if eRounds == 1:
            eFirstMonst = [("Dragonite", 20)]
            eSecondMonst = [("Gengar", 18)]
            eLastMonst = [("Mewtwo", 22)]

        # Enemy in the last Round
        if eRounds == 2:
            eFirstMonst = [("Mewtwo", 22)]
            eSecondMonst = [("Dragonite", 20)]
            eLastMonst = [("Mewtwo", 22)]
