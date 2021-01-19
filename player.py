import pygame
import monsters


screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

screen = pygame.display.set_mode([screen_width, screen_height])

monsterList = []

m1PosX = 375
m1PosY = 380
m2PosX = 200
m2PosY = 380
m3PosX = 25
m3PosY = 380


def setMonsters(firstMon, secMon, thirdMon):

    global monsterList
    global m1PosX, m1PosY, m2PosX, m2PosY, m3PosX, m3PosY

    monster1 = monsters.monster(firstMon, True, m1PosX, m1PosY)
    monster2 = monsters.monster(secMon, True, m2PosX, m2PosY)
    monster3 = monsters.monster(thirdMon, True, m3PosX, m3PosY)

    monsterList= [monster1, monster2, monster3]


def printPlayerMonsters():


    monsterList[0].printMonster()
    monsterList[1].printMonster()
    monsterList[2].printMonster()

def isDead():
    deadCounter = 0
    dead = False
    global monsterList

    for m in monsterList:
        if m.hp <= 0:
            deadCounter += 1

    if deadCounter >= 3:
        dead = True

    return dead


def isAttacking():

    attacking = False

    for m in monsterList:
        if m.action != 0:
            attacking = True

    return attacking


def getNextTarget():

    global monsterList

    target = monsterList[0]

    if monsterList[0].hp <= 0 and monsterList[1].hp > 0:
        target = monsterList[1]

    elif monsterList[1].hp <= 0:
        target = monsterList[2]

    return target