import pygame
import attackParticles
import random
import printFunctions

screen_width = 1200
screen_backImg = 600
screen_panel = 225
screen_height = screen_backImg + screen_panel

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])

#Sounds
shootingSound = pygame.mixer.Sound("sounds/laser1.wav")
jumpingSound = pygame.mixer.Sound("sounds/jump.wav")
punchSound = pygame.mixer.Sound("sounds/punch.wav")

#Font for Monster Stats
font = pygame.font.SysFont(None, 30)
deadRender = font.render("DEAD", True, (255, 255, 255))

#Monster List
monstName = ["Machamp", "Mewtwo", "Gengar"]
# 0 = Melee, 1 = Ranged, 2 = Assassin
monstType = [0, 1, 2]
monstHp = [12, 10, 8]
monstDmg = [2, 3, 4]
attType = [0, 1, 2]
effectiveList = [[2], [0], [1]]

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
        global font

        self.select = select
        self.player = player
        self.name = monstName[select]
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
        self.maxHp = monstHp[select]
        self.dmg = monstDmg[select]
        self.posX = posX
        self.posY = posY
        self.basePosX = posX
        self.basePosY = posY
        self.width = 150
        self.height = 150
        self.staticTics = 0
        self.steps = 0
        self.inJump = False
        self.jumpVar = -15
        self.action = 0
        self.rangedAttType = attType[select]
        self.particleCounter = 0
        self.rect = pygame.Rect(self.posX+35, self.posY+30, self.width-70, self.height-30)


        self.effectiveAgainst = effectiveList[select]

        self.nameRender = font.render(self.name, True, (255, 255, 255))
        self.hpRendeer = font.render(f'HP: {self.hp*10} / {self.maxHp*10}', True, (255, 255 ,255))

        self.target = self


    def printMonster(self):

        global counter
        global counter2
        global deadRender

        # 4 // 2 = 2 <- Out of Range
        if self.staticTics >= 19:
            self.staticTics = 0
        # 16 // 4 = 4 <- Out of Range
        if self.steps >= 15:
            self.steps = 0

        self.rect = pygame.Rect(self.posX+20, self.posY+30, self.width-40, self.height-30)

        #Check Hitbox Rectangle
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 7)


        # MonsterName
        screen.blit(self.nameRender, (self.basePosX + 25, self.basePosY + self.height + 100))

        #Draw Healthbar
        self.drawHealthBar()

        #If monster is dead
        if self.isDead():
            screen.blit(deadRender, (self.basePosX + 30, self.basePosY + self.height + 200))

        #If monster is not dead
        else:
            screen.blit(self.hpRendeer, (self.basePosX + 10, self.basePosY + self.height + 200))
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
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 128)
                    if self.steps % 4 == 1 or self.steps % 4 == 2:
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 180)
                    else:
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 150)

                else:
                    screen.blit(self.movement[self.steps // 4], (self.posX, self.posY))


                self.posX += self.speed
                self.steps += 1
                counter += 1

                #Target was hit
                if self.rect.colliderect(self.target.rect):
                    self.posX = self.basePosX
                    self.posY = self.basePosY
                    self.action = 0
                    counter = 0

                    #Damage the target
                    self.calcDamage()
                    #Hitting Sound
                    pygame.mixer.Sound.play(punchSound)


                #If monster missed the target
                elif counter >= 200:
                    self.action = 0
                    counter = 0

                    #Damage the target
                    self.calcDamage()
                    #Hitting Sound
                    pygame.mixer.Sound.play(punchSound)


            #jumping
            if self.action == 2:
                #Makes Assassin transparent
                if self.select == 2:
                    printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 120)
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


                #firstParticle = len(attackParticles.currentParticles) - 1
                a = attackParticles.currentParticles[0]
                attRect = pygame.Rect(a.x - a.rad, a.y - a.rad, a.rad*2, a.rad*2)

                if self.target.rect.colliderect(attRect):
                    attackParticles.currentParticles.clear()
                    self.particleCounter = 0
                    self.action = 0

                    #Damage the target
                    self.calcDamage()

                    #Hitting Sound
                    pygame.mixer.Sound.play(punchSound)



    #Chose the Attack Type
    def attack(self, target):

        self.posX = self.basePosX
        self.posY = self.basePosY
        self.target.posX = self.target.basePosX
        self.target.posY = self.target.basePosY

        if not self.isDead():

            self.target = target

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


    def drawHealthBar(self):

        #Calculate the HP Ratio
        hpRatio = self.hp / self.maxHp

        #Draw a Red Line with max HP
        pygame.draw.rect(screen, (255, 0, 0), (self.basePosX, self.basePosY + self.height + 150, 150, 30))

        #Draw a Green line based on the HP ratio over the red Line
        pygame.draw.rect(screen, (0, 255, 0), (self.basePosX, self.basePosY + self.height + 150, round(150 * hpRatio), 30))


    #Calculate the damage against target HP
    def calcDamage(self):

        #set default Attack Multiplicator
        multiplicator = 1

        for aType in self.effectiveAgainst:

            #Is the monster effective against the target
            if aType == self.target.type:
                multiplicator = 2

        for targetaType in self.target.effectiveAgainst:

            #Is the target effective against the monster
            if targetaType == self.type:
                multiplicator = 0.5

        self.target.hp = self.target.hp - (self.dmg * multiplicator)


    #Monster is dead
    def isDead(self):

        if self.hp <= 0:
            return True
        else:
            return False