import pygame
import pygame_menu
import myGame

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("WIP Project: pyGame by Daniel Wetzel - Battle Simulator - Choose Game Settings...")


menu = pygame_menu.Menu(700, 1000, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)
menu.add_selector('First Monster: ',
                  [('Machamp (Melee)', 0), ('Mewtwo (Ranged)', 1), ('Gengar (Assassin)', 2)],
                  onchange=myGame.set_firtMon)

menu.add_selector('Second Monster: ',
                  [('Mewtwo (Ranged)', 1), ('Gengar (Assassin)', 2), ('Machamp (Melee)', 0)],
                  onchange=myGame.set_secMon)

menu.add_selector('Last Monster: ',
                  [('Gengar (Assassin)', 2), ('Machamp (Melee)', 0), ('Mewtwo (Ranged)', 1)],
                  onchange=myGame.set_lastMon)

menu.add_selector('Enemy: ',
                  [('Easy', 0), ('Medium', 1), ('Hard', 2)],
                  onchange=myGame.set_Enemy)

menu.add_button('Play', myGame.startGame)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
