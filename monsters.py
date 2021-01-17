import pygame
import attackParticles
import random

pygame.init()
screen = pygame.display.set_mode([1200, 595])

#Sounds
shootingSound = pygame.mixer.Sound("sounds/laser1.wav")
jumpingSound = pygame.mixer.Sound("sounds/jump.wav")


#Monster List
monstName = ["Machamp", "Mewtwo", "Gengar"]
# 0 = Melee, 1 = Ranged, 2 = Assassin
monstType = [0, 1, 2]
monstHp = [10, 8, 8]
monstDmg = [2, 3, 3]
attType = [0, 1, 2]

#static image of the monster
p_static = [[pygame.image.load("textures/machamp/player1.png"),
             pygame.image.load("textures/machamp/player2.png")],

            [pygame.image.load("textures/mewtwo/player1.png"),
             pygame.image.load("textures/mewtwo/player2.png")],

            [pygame.image.load("textures/gengar/player1.png"),
             pygame.image.load("textures/gengar/player2.png")]]

e_static = [[pygame.image.load("textures/machamp/enemy1.png"),
             pygame.image.load("textures/machamp/enemy2.png")],

            [pygame.image.load("textures/mewtwo/enemy1.png"),
             pygame.image.load("textures/mewtwo/enemy2.png")],

            [pygame.image.load("textures/gengar/enemy1.png"),
             pygame.image.load("textures/gengar/enemy2.png")]]

p_jump = [pygame.image.load("textures/machamp/playerjump1.png"),
          pygame.image.load("textures/mewtwo/playerjump1.png"),
          pygame.image.load("textures/gengar/playerjump1.png")]

e_jump = [pygame.image.load("textures/machamp/enemyjump1.png"),
          pygame.image.load("textures/mewtwo/enemyjump1.png"),
          pygame.image.load("textures/gengar/enemyjump1.png")]

p_move = [[pygame.image.load("textures/machamp/player1.png"),
           pygame.image.load("textures/machamp/playerjump1.png"),
           pygame.image.load("textures/machamp/playerjump2.png"),
           pygame.image.load("textures/machamp/player2.png")],

          [pygame.image.load("textures/mewtwo/player2.png"),
           pygame.image.load("textures/mewtwo/playerjump1.png"),
           pygame.image.load("textures/mewtwo/playerjump2.png"),
           pygame.image.load("textures/mewtwo/player2.png")],

          [pygame.image.load("textures/gengar/player2.png"),
           pygame.image.load("textures/gengar/playerjump1.png"),
           pygame.image.load("textures/gengar/playerjump2.png"),
           pygame.image.load("textures/gengar/player2.png")]
          ]

e_move = [[pygame.image.load("textures/machamp/enemy1.png"),
           pygame.image.load("textures/machamp/enemyjump1.png"),
           pygame.image.load("textures/machamp/enemyjump2.png"),
           pygame.image.load("textures/machamp/enemy2.png")],

          [pygame.image.load("textures/mewtwo/enemy2.png"),
           pygame.image.load("textures/mewtwo/enemyjump1.png"),
           pygame.image.load("textures/mewtwo/enemyjump2.png"),
           pygame.image.load("textures/mewtwo/enemy2.png")],

          [pygame.image.load("textures/gengar/enemy2.png"),
           pygame.image.load("textures/gengar/enemyjump1.png"),
           pygame.image.load("textures/gengar/enemyjump2.png"),
           pygame.image.load("textures/gengar/enemy2.png")]
          ]


counter = 0
counter2 = 0

class monster:
    def __init__(self, select, player, posX, posY):
        self.select = select
        self.player = player
        if player:
            self.static = p_static[select]
            self.jump = p_jump[select]
            self.movement = p_move[select]
            self.speed = 5
            if self.select == 2:
                self.speed += 5
        else:
            self.static = e_static[select]
            self.jump = e_jump[select]
            self.movement = e_move[select]
            self.speed = -5
            if self.select == 2:
                self.speed -= 5
        self.type = monstType[select]
        self.hp = monstHp[select]
        self.dmg = monstDmg[select]
        self.posX = posX
        self.posY = posY
        self.basePosX = posX
        self.basePosY = posY
        self.staticTics = 0
        self.steps = 0
        self.inJump = False
        self.jumpVar = -15
        self.action = 0
        self.rangedAttType = attType[select]
        self.particleCounter = 0

    def printMonster(self):

        global counter
        global counter2

        # 4 // 2 = 2 <- Out of Range
        if self.staticTics >= 19:
            self.staticTics = 0
        # 16 // 4 = 4 <- Out of Range
        if self.steps >= 15:
            self.steps = 0

        #static
        if self.action == 0:
            self.posX = self.basePosX
            self.posY = self.basePosY
            screen.blit(self.static[self.staticTics // 10], (self.posX, self.posY))
            self.staticTics += 1

        #walking/melee attacking
        if self.action == 1:

            # Makes Assassin transparent
            if self.select == 2:
                if self.steps % 4 == 0:
                    blit_alpha(screen, self.movement[self.steps // 4],(self.posX, self.posY), 128)
                if self.steps % 4 == 1 or self.steps % 4 == 2:
                    blit_alpha(screen, self.movement[self.steps // 4],(self.posX, self.posY), 180)
                else:
                    blit_alpha(screen, self.movement[self.steps // 4],(self.posX, self.posY), 150)

            else:
                screen.blit(self.movement[self.steps // 4], (self.posX, self.posY))


            self.posX += self.speed
            self.steps += 1
            counter += 1

            if counter >= 200:
                self.action = 0


        #jumping
        if self.action == 2:
            #Makes Assassin transparent
            if self.select == 2:
                blit_alpha(screen, self.movement[self.steps // 4], (self.posX, self.posY), 120)
            else:
                screen.blit(self.jump, (self.posX, self.posY))
            if self.jumpvar >= -14:
                n = 1
                if self.jumpvar < 0:
                    n = -1
                self.posY -= (self.jumpvar ** 2) * 0.25 * n
                self.posX += self.speed
                self.jumpvar -= 1
            else:
                self.inJump = False
                self.action = 1


        #shooting
        if self.action == 3:
            self.posX = self.basePosX
            self.posY = self.basePosY
            screen.blit(self.static[0], (self.posX, self.posY))

            if self.particleCounter < attackParticles.amountList[self.rangedAttType]:
                attackParticles.currentParticles.append(attackParticles.rangedAttack(round(self.posX),
                                                                                     round(self.posY),
                                                                                     self.rangedAttType,
                                                                                     self.player))
                self.particleCounter +=1
            else:
                self.particleCounter = 0
                self.action = 0



    #Chose the Attack Type
    def attack(self):
        if self.type == 0:
            self.meleeAtt()

        if self.type == 1:
            self.rangedAtt()

        if self.type == 2:
            self.assassinAttack()



    def meleeAtt(self):
        self.action = 1


    def rangedAtt(self):
        self.action = 3
        pygame.mixer.Sound.play(shootingSound)


    def assassinAttack(self):
        if random.randint(0, 1) != 0:
            self.jumping()
        else:
            self.meleeAtt()


    def jumping(self):
        self.inJump = True
        self.jumpvar = 14
        self.action = 2
        pygame.mixer.Sound.play(jumpingSound)


def blit_alpha(target, source, location, opacity):
    x_temp = location[0]
    y_temp = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x_temp, -y_temp))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)