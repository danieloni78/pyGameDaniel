import pygame
import monsters

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

screen = pygame.display.set_mode([screen_width, screen_height])

monsterList = []

e1PosX = 675
e1PosY = 380
e2PosX = 850
e2PosY = 380
e3PosX = 1025
e3PosY = 380

currentlyAttacking = 0

doubleAttacker = 2
doubleAttacking = False


def setMonsters(firstMon, secMon, thirdMon):

    global monsterList
    global e1PosX, e1PosY, e2PosX, e2PosY, e3PosX, e3PosY
    global  currentlyAttacking, doubleAttacking, doubleAttacker

    currentlyAttacking = 0
    doubleAttacker = 2
    doubleAttacking = False

    monster1 = monsters.monster(firstMon, False, e1PosX, e1PosY)
    monster2 = monsters.monster(secMon, False, e2PosX, e2PosY)
    monster3 = monsters.monster(thirdMon, False, e3PosX, e3PosY)

    monsterList= [monster1, monster2, monster3]


def printEnemyMonsters():

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


def attack(target):
    global monsterList
    global currentlyAttacking

    if doubleAttacking:
        if currentlyAttacking >= 4:
            currentlyAttacking = 0
    else:
        if currentlyAttacking >= 3:
            currentlyAttacking = 0

    # Normal attacks
    if currentlyAttacking < 3:
        if monsterList[0].hp <= 0 and currentlyAttacking == 0:
            if monsterList[1].hp > 0:
                currentlyAttacking = 1
            else:
                currentlyAttacking = 2

        elif monsterList[0].hp <= 0 and monsterList[1].hp <= 0 and currentlyAttacking == 1:
            currentlyAttacking = 2

        monsterList[currentlyAttacking].attack(target)

    # Special Attack turn
    elif currentlyAttacking == 3:
        monsterList[doubleAttacker].attack(target)

    currentlyAttacking += 1


def restore():
    for m in monsterList:
        m.hp = m.maxHp

def setDoubleAttacker(number):
    global doubleAttacker, doubleAttacking
    doubleAttacker = number
    doubleAttacking = True