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
                  [("Venusaur", 15), ('Bulbasaur (Melee)', 0), ('Squirtle (Melee)', 1), ('Charmander (Ranged)', 2),
                   ("Pikachu (Assassin)",3), ("Gastly (Assassin)", 4),("Machop (Melee)",5),
                   ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                   ("Haunter", 12),("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                   ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                   ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                  onchange=myGame.set_firtMon)

menu.add_selector('Second Monster: ',
                  [("Blastoise", 16), ('Squirtle (Melee)', 1), ('Bulbasaur (Melee)', 0), ('Charmander (Ranged)', 2),
                   ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                   ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                   ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                   ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                   ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                  onchange=myGame.set_secMon)

menu.add_selector('Last Monster: ',
                  [("Charizard", 17), ('Charmander (Ranged)', 2),('Bulbasaur (Melee)', 0), ('Squirtle (Melee)', 1),
                   ("Pikachu (Assassin)", 3), ("Gastly (Assassin)", 4), ("Machop (Melee)", 5),
                   ("Dratini", 6), ("Ivysaur", 9), ("Wartortle", 10), ("Charmeleon", 11),
                   ("Haunter", 12), ("Machoke", 13), ("Dragonair", 14), ("Venusaur", 15),
                   ("Blastoise", 16), ("Charizard", 17), ("Gengar", 18), ("Machamp", 19),
                   ("Dragonite", 20), ("Snorlax", 21), ("Mewtwo", 22)],
                  onchange=myGame.set_lastMon)

menu.add_selector('Enemy: ',
                  [('Easy', 0), ('Medium', 1), ('Hard', 2)],
                  onchange=myGame.init_Enemy)

menu.add_button('Play', myGame.startGame)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
