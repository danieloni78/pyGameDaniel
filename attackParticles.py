import pygame

screen = pygame.display.set_mode([1200, 595])

spdList = [15, 7, 25]
colorList = [(225, 225, 195), (55, 0, 80), (230, 100, 0)]
radList = [30, 30, 20]
amountList = [30, 1, 30]


currentParticles = []

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

    def move(self):
        self.x += self.speed

    def printAttack(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad, 0)

def hanldeAttacks():
    for a in currentParticles:
        if a.x >= 0 and a.x <= 1200:
            a.move()
        else:
            currentParticles.remove(a)

