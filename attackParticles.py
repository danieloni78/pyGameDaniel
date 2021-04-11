# This class creates and manages the special attack particles

import pygame

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

screen = pygame.display.set_mode([screen_width, screen_height])

# Size, form and color of the particles for each type
# Most/Atk Types: 0 - Normal,     1 - Water,         2 - Fire,           3 - Grass,          4 - Electric ,      5 - Psychic,    6 - Rock,           7 - Flying,         8 - Fighting,       9 - Dragon
spdList = [20, 25, 25, 35, 25, 15, 15, 25, 15, 25]
colorList = [(225, 225, 195), (50, 175, 255), (230, 100, 0), (5, 85, 15), (240, 250, 40), (55, 0, 80), (85, 65, 40),
             (175, 245, 240), (120, 60, 10), (130, 45, 255)]
radList = [30, 20, 30, 28, 25, 30, 50, 30, 70, 35]
amountList = [50, 50, 50, 50, 50, 1, 1, 50, 1, 50]
form = [0, 0, 0, 2, 3, 0, 1, 0, 1, 2]

# List of current particles
currentParticles = []


# Special Attack
class rangedAttack:
    def __init__(self, pX, pY, type, player):
        self.x = pX
        self.y = pY
        if player:
            self.x += 145
            self.speed = spdList[type]
        else:
            self.x += 5
            self.speed = -1 * spdList[type]
        self.y += 84
        self.rad = radList[type]
        self.color = colorList[type]
        self.form = form[type]

    # Move the attack
    def move(self):
        self.x += self.speed

    # Print the attack
    def printAttack(self):

        if self.form == 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad)

        elif self.form == 1:
            pygame.draw.rect(screen, self.color, [self.x, self.y, self.rad, self.rad / 2])

        elif self.form == 2:
            pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.rad, self.rad * 0.65])

        elif self.form == 3:
            pygame.draw.polygon(screen, self.color,
                                [[self.x, self.y], [self.x, self.y + self.rad], [self.x + self.rad, self.y]])


# Handle the attack particles
def hanldeAttacks():
    for a in currentParticles:
        if a.x >= 0 and a.x <= 1200:
            a.move()
        else:
            currentParticles.remove(a)
