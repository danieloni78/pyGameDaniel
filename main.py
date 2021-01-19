import pygame
import pygame_menu
import myGame

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("WIP Project: pyGame by Daniel Wetzel")

firstMonst = ('Machamp', 0)
secondMonst = ('Mewtwo', 1)
lastMonst = ('Gengar', 2)


def startGame():
    myGame.new(firstMonst, secondMonst, lastMonst)


def set_firtMon(monster, number):
    global firstMonst
    firstMonst = monster


def set_secMon(monster, number):
    global secondMonst
    secondMonst = monster

def set_lastMon(monster, number):
    global lastMonst
    lastMonst = monster


menu = pygame_menu.Menu(700, 1000, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)
menu.add_selector('First Monster: ', [('Machamp (Melee)', 1), ('Mewtwo (Ranged)', 2), ('Gengar (Assassin)', 3)], onchange=set_firtMon)
menu.add_selector('Second Monster: ', [('Machamp (Melee)', 1), ('Mewtwo (Ranged)', 2), ('Gengar (Assassin)', 3)], onchange=set_secMon)
menu.add_selector('Last Monster: ', [('Machamp (Melee)', 1), ('Mewtwo (Ranged)', 2), ('Gengar (Assassin)', 3)], onchange=set_lastMon)
menu.add_button('Play', startGame)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
