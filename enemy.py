import pygame
import monsters


screen = pygame.display.set_mode([1200, 595])

monsterList = []

e1PosX = 675
e1PosY = 380
e2PosX = 850
e2PosY = 380
e3PosX = 1025
e3PosY = 380


def setMonsters(firstMon, secMon, thirdMon):

    global monsterList
    global e1PosX, e1PosY, e2PosX, e2PosY, e3PosX, e3PosY

    monster1 = monsters.monster(firstMon, False, e1PosX, e1PosY)
    monster2 = monsters.monster(secMon, False, e2PosX, e2PosY)
    monster3 = monsters.monster(thirdMon, False, e3PosX, e3PosY)

    monsterList= [monster1, monster2, monster3]


def printEnemyMonsters():

    monsterList[0].attack()
    monsterList[0].printMonster()
    monsterList[1].printMonster()
    monsterList[2].printMonster()