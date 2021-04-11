# This game was created by Daniel Wetzel
# It is inspired by the Pokemon Games from Nintendo
# as welll as by the following tutorials:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/project/5492/7939
# https://www.youtube.com/playlist?list=PLjuHXsDGkbTSpTMJ4MXTiQXN4AeOzpu1w

import menus

menus.startScreen()
selection = menus.selectTeam()
menus.selectEnemy()
menus.selectOrder(selection)
