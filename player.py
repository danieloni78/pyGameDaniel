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

counter = 0

def setMonsters(firstMon, secMon, thirdMon):

    global monsterList
    global m1PosX, m1PosY, m2PosX, m2PosY, m3PosX, m3PosY

    monster1 = monsters.monster(firstMon, True, m1PosX, m1PosY)
    monster2 = monsters.monster(secMon, True, m2PosX, m2PosY)
    monster3 = monsters.monster(thirdMon, True, m3PosX, m3PosY)

    monsterList= [monster1, monster2, monster3]


def printPlayerMonsters():
    global counter
    while counter < 1:
        #monsterList[0].attack()
        #monsterList[1].attack()
        #monsterList[2].attack()
        counter += 1

    monsterList[0].printMonster()
    monsterList[1].printMonster()
    monsterList[2].printMonster()