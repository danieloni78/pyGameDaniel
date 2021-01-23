import pygame
import attackParticles
import random
import printFunctions
import loadTextures

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

#MoveTypes: 0 - Normal, 1 - Special, 2 - Assassin

#Most/Atk Types: 0 - Normal, 1 - Water, 2 - Fire, 3 - Grass, 4 - Electric ,5 - Psychic, 6 - Rock, 7 - Flying, 8 - Fighting,  9 - Dragon


#           [ID,     Name, MoveType,HP,    DMG,  MonstType  Evolves Into
monstData = [[0, "Bulbasaur", 0,    6,      1,      3,          9],
             [1, "Squirtle",  0,    6,      1,      1,          10],
             [2, "Charmander",0,    5,      2,      2,          11],
             [3, "Pikachu",   2,    5,      3,      4,          8],
             [4, "Gastly",    2,    4,      3,      5,          12],
             [5, "Machop",    0,    7,      2,      8,          13],
             [6, "Dratini",   0,    6,      2,      9,          14],
             [7, "Eevee",     2,    6,      2,      0,          -2],
             [8, "Raichu",    2,    12,     4,      4,          -1],
             [9, "Venusaur",  0,    12,      3,      3,          15],
             [10, "Wartortle", 0,   12,      3,      1,          16],
             [11, "Charmeleon", 0,  8,      4,      2,          17],
             [12, "Haunter",    2,  7,      5,      5,          18],
             [13, "Machoke",    0,  9,      4,      8,          19],
             [14, "Dragonair",  0,  7,      5,      9,          20],
             [15, "Ivysaur",    0,  20,     7,      3,          -1],
             [16, "Blastoise",  0,  19,     7,      1,          -1],
             [17, "Charizard",  2,  18,     8,      2,          -1],
             [18, "Gengar",     2,  15,     10,     5,          -1],
             [19, "Machamp",    0,  21,     7,      8,          -1],
             [20, "Dragonite",  0,  27,     11,     9,          -1],
             [21, "Snorlax",    0,  26,     7,      0,          -1],
             [22, "Mewtwo",     2,  30,     12,     5,          -1],
             [23, "Vaporeon",   0,  12,     4,      1,          -1],
             [24, "Jolteon",    0,  10,     5,      4,          -1],
             [25, "Flareon",    0,  11,     5,      2,          -1],
             [26, "Aerodactyl", 0,  9,      3,      7,          -1],
             [27, "Electabuzz", 0,  9,      3,      4,          -1],
             [28, "Magmar",     0,  9,      3,      2,          -1],
             [29, "Abra",       2,  4,      2,      5,          30],
             [30, "Kadabra",    2,  8,      6,      5,          31],
             [31, "Alakazam",   2,  14,     10,     5,          -1],
             [32, "Weedle",     0,  4,      2,      3,          33],
             [33, "Kakuna",     0,  8,      2,      3,          34],
             [34, "Beedrill",   2,  18,     7,      3,          -1],
             [35, "Magikarp",   0,  5,      0,      1,          36],
             [36, "Gyarados",   0,  25,     10,     1,          -1],
             [37, "Geodude",    0,  6,      1,      6,          38],
             [38, "Graveler",   0,  10,     4,      6,          39],
             [39, "Golem",      0,  25,     7,      6,          -1],
             [40, "Nidoran",    0,  5,      2,      9,          41],
             [41, "Nidorino",   0,  9,      4,      9,          42],
             [42, "Nidoking",   0,  25,     10,     9,          -1],
             [43, "Bellsprout", 0,  5,      1,      3,          44],
             [44, "Weepinbell", 0,  8,      3,      3,          45],
             [45, "Victreebel", 0,  15,     7,      3,          -1],
             [46, "Scyther",    2,  14,     8,      3,          -1],
             [47, "Lapras",     0,  18,     7,      1,          -1],
             [48, "Grimer",     0,  6,      1,      5,          49],
             [49, "Muk",        0,  12,     4,      5,          -1],
             [50, "Rattata",    2,  4,      2,      0,          51],
             [51, "Raticate",   2,  12,     5,      0,          -1],
             [52, "Mr. Mime",   2,  12,     6,      5,          -1],
             [53, "Rhydon",     0,  18,     7,      6,          -1],
             [54, "Growlithe",  2,  6,      2,      2,          55],
             [55, "Arcanine",   2,  12,     6,      2,          -1],
             [56, "Magnemite",  0,  6,      1,      4,          57],
             [57, "Magneton",   0,  14,     6,      4,          -1],
             [58, "Poliwag",    0,  5,      2,      1,          59],
             [59, "Poliwhirl",  0,  9,      5,      1,          60],
             [60, "Poliwrath",  0,  16,     8,      1,          -1],
             [61, "Chansey",    0,  31,     4,      0,          -1],
             [62, "Caterpie",   0,  4,      2,      3,          63],
             [63, "Metapod",    0,  8,      2,      3,          64],
             [64, "Butterfree", 0,  19,     6,      3,          -1],
             [65, "Pidgey",     2,  6,      1,      7,          66],
             [66, "Pidgeotto",  2,  9,      5,      7,          67],
             [67, "Pidgeot",    2,  16,     8,      7,          -1],
             [68, "Articuno",   0,  28,     11,     1,          -1],
             [69, "Moltres",    0,  28,     11,     2,          -1],
             [70, "Zapdos",     0,  28,     11,     4,          -1],
             [71, "Mew",        0,  27,     10,     5,          -1]

             ]

#Most/Atk Types: 0 - Normal, 1 - Water, 2 - Fire, 3 - Grass, 4 - Electric ,5 - Psychic, 6 - Rock, 7 - Flying, 8 - Fighting,  9 - Dragon
effectiveList = [[-1],            [2, 6],     [3],    [1, 6],     [1, 7],        [5, 8],    [2, 7],   [3, 8],     [0, 6],         [9]]


counter = 0
counter2 = 0

class monster:
    def __init__(self, select, player, posX, posY):
        global font

        self.select = select
        self.player = player
        self.name = monstData[self.select][1]
        self.moveType = monstData[self.select][2]
        if player:
            self.static = loadTextures.loadStaticPlayer(self.select)
            self.jump = loadTextures.loadJumpPlayer(self.select)
            self.movement = loadTextures.loadMovePlayer(self.select)
            self.special = loadTextures.loadSpecialPlayer(self.select)
            self.speed = 8
            if self.moveType == 2:
                self.speed += 5
        else:
            self.static = loadTextures.loadStaticEnemy(self.select)
            self.jump = loadTextures.loadJumpEnemy(self.select)
            self.movement = loadTextures.loadMoveEnemy(self.select)
            self.special = loadTextures.loadSpecialEnemy(self.select)
            self.speed = -5
            if self.moveType == 2:
                self.speed -= 5
        self.menuStatic = loadTextures.loadMenuStatic(self.select)
        self.menuMoving = loadTextures.loadMenuMoving(self.select)
        self.hp = monstData[self.select][3]
        self.maxHp = monstData[self.select][3]
        self.dmg = monstData[self.select][4]
        self.monstType = monstData[self.select][5]
        self.evolvesTo = monstData[self.select][6]
        self.posX = posX
        self.posY = posY
        self.basePosX = posX
        self.basePosY = posY
        self.width = 150
        self.height = 150
        self.staticTics = 0
        self.steps = 0
        self.specialTics = 0
        self.menuTics = 0
        self.inJump = False
        self.jumpVar = -15
        self.action = 0
        self.particleCounter = 0
        self.rect = pygame.Rect(self.posX+35, self.posY+30, self.width-70, self.height-30)

        self.effectiveAgainst = effectiveList[self.monstType]

        self.nameRender = font.render(self.name, True, (255, 255, 255))
        self.hpRendeer = font.render(f'HP: {self.hp*10} / {self.maxHp*10}', True, (255, 255 ,255))

        self.target = self


    def printMonster(self):

        global counter
        global counter2
        global deadRender


        # 40 // 10 = 4 <- Out of Range
        if self.staticTics >= 39:
            self.staticTics = 0
        # 16 // 4 = 4 <- Out of Range
        if self.steps >= 15:
            self.steps = 0
        # 16 // 4 = 4 <- Out of Range
        if self.specialTics >= 31:
            self.specialTics = 0

        self.rect = pygame.Rect(self.posX+20, self.posY+30, self.width-40, self.height-30)

        #Check Hitbox Rectangle
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 7)


        # MonsterName
        screen.blit(self.nameRender, (self.basePosX + 25, self.basePosY + self.height + 100))

        #Draw Healthbar
        self.drawHealthBar()

        #If monster is dead
        if self.isDead():
            #Render dead status
            screen.blit(deadRender, (self.basePosX + 30, self.basePosY + self.height + 200))

        #If monster is not dead
        else:
            #Render Hp Status
            screen.blit(self.hpRendeer, (self.basePosX + 10, self.basePosY + self.height + 200))


            #static
            if self.action == 0:
                #Reset Position
                self.posX = self.basePosX
                self.posY = self.basePosY

                #Reset Steps
                self.steps= 0
                self.specialTics = 0

                #Print The monster
                screen.blit(self.static[self.staticTics // 10], (self.posX, self.posY))
                self.staticTics += 1

            #walking/melee attacking
            if self.action == 1:

                # Makes Assassin transparent
                if self.moveType == 2:
                    #Print the monster transparent
                    if self.steps % 4 == 0:
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 128)
                    if self.steps % 4 == 1 or self.steps % 4 == 2:
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 180)
                    else:
                        printFunctions.print_transparent(screen, self.movement[self.steps // 4], (self.posX, self.posY), 150)

                else:
                    #Print the monster
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
                if self.moveType == 2:
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

                # Print the monster
                screen.blit(self.special[self.specialTics // 8], (self.posX, self.posY))
                self.specialTics += 1

                if self.particleCounter < attackParticles.amountList[self.monstType]:
                    attackParticles.currentParticles.append(attackParticles.rangedAttack(round(self.posX),
                                                                                         round(self.posY),
                                                                                         self.monstType,
                                                                                         self.player))
                    self.particleCounter +=1



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

            if self.moveType == 0:
                self.meleeAtt()

            elif self.moveType == 1:
                self.rangedAtt()

            elif self.moveType == 2:
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
        if self.moveType == 1:
            multiplicator = 1.5
        else:
            multiplicator = 1

        for aType in self.effectiveAgainst:

            #Is the monster effective against the target
            if aType == self.target.monstType:
                multiplicator *= 2

        for targetaType in self.target.effectiveAgainst:

            #Is the target effective against the monster
            if targetaType == self.monstType:
                multiplicator *= 0.5

        self.target.hp = self.target.hp - (self.dmg * multiplicator)
        self.target.hpRendeer = font.render(f'HP: {int(self.target.hp*10)} / {int(self.target.maxHp*10)}', True, (255, 255 ,255))


    #Monster is dead
    def isDead(self):

        if self.hp <= 0:
            return True
        else:
            return False


    def evolve(self):

        success = False

        #Monster cannot evolve
        if self.evolvesTo == -1:
            success = False

        #Monster has more than one evolution
        elif self.evolvesTo == -2:

            ran = random.randint(0,2)

            if  ran == 0:

                self.__init__(23, self.player, self.basePosX, self.basePosY)

            elif ran == 1:

                self.__init__(24, self.player, self.basePosX, self.basePosY)

            else:

                self.__init__(25, self.player, self.basePosX, self.basePosY)

            success = True

        #Monser has one evolution
        else:

            self.__init__(self.evolvesTo, self.player, self.basePosX, self.basePosY)
            success = True

        return success


    def printMenu(self, moving, x, y):

        self.width = 100
        self.height = 100

        # 40 // 10 = 4 <- Out of Range
        if self.menuTics >= 39:
            self.menuTics = 0

        self.rect = pygame.Rect(x+20, y+30, self.width-40, self.height-30)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 7)


        if moving:
            # Print The monster
            screen.blit(self.menuMoving[self.menuTics // 10], (x, y))
            self.menuTics += 1



        else:
            # Print The monster
            screen.blit(self.menuStatic, (x, y))


    def turnSpecialAttacker(self):
        self.moveType = 1
        if self.dmg == 0:
            self.dmg = 0.5


    def switchRandom(self, rounds):

        success = False

        if rounds == 5:
            ran = random.randint(0,100)

            if  ran < 20:

                self.__init__(46, self.player, self.basePosX, self.basePosY)
                success = True

            elif 20 <= ran < 40:

                self.__init__(52, self.player, self.basePosX, self.basePosY)
                success = True

            elif 40 <= ran < 50:

                self.__init__(47, self.player, self.basePosX, self.basePosY)
                success = True

            elif 50 <= ran < 60:

                self.__init__(57, self.player, self.basePosX, self.basePosY)
                success = True

            elif 60 <= ran < 65:

                self.__init__(61, self.player, self.basePosX, self.basePosY)
                success = True

            elif 65 <= ran < 70:

                self.__init__(60, self.player, self.basePosX, self.basePosY)
                success = True

            elif 70 <= ran < 75:

                self.__init__(49, self.player, self.basePosX, self.basePosY)
                success = True

            elif 75 <= ran < 80:

                self.__init__(21, self.player, self.basePosX, self.basePosY)
                success = True

            elif 80 <= ran < 85:

                self.__init__(18, self.player, self.basePosX, self.basePosY)
                success = True

            elif 85 <= ran < 90:

                self.__init__(34, self.player, self.basePosX, self.basePosY)
                success = True

            elif 90 <= ran < 95:

                self.__init__(64, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 95:

                self.__init__(68, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 96:

                self.__init__(69, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 97:

                self.__init__(70, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 98:

                self.__init__(71, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 99:

                self.__init__(22, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 100:

                self.__init__(35, self.player, self.basePosX, self.basePosY)
                success = True

        elif rounds == 7:
            ran = random.randint(0, 100)

            if ran < 20:

                self.__init__(61, self.player, self.basePosX, self.basePosY)
                success = True

            elif 20 <= ran < 40:

                self.__init__(21, self.player, self.basePosX, self.basePosY)
                success = True

            elif 40 <= ran < 50:

                self.__init__(47, self.player, self.basePosX, self.basePosY)
                success = True

            elif 50 <= ran < 60:

                self.__init__(42, self.player, self.basePosX, self.basePosY)
                success = True

            elif 60 <= ran < 65:

                self.__init__(46, self.player, self.basePosX, self.basePosY)
                success = True

            elif 65 <= ran < 70:

                self.__init__(60, self.player, self.basePosX, self.basePosY)
                success = True

            elif 70 <= ran < 75:

                self.__init__(49, self.player, self.basePosX, self.basePosY)
                success = True

            elif 75 <= ran < 80:

                self.__init__(52, self.player, self.basePosX, self.basePosY)
                success = True

            elif 80 <= ran < 85:

                self.__init__(18, self.player, self.basePosX, self.basePosY)
                success = True

            elif 85 <= ran < 90:

                self.__init__(34, self.player, self.basePosX, self.basePosY)
                success = True

            elif 90 <= ran < 95:

                self.__init__(64, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 95:

                self.__init__(68, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 96:

                self.__init__(69, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 97:

                self.__init__(70, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 98:

                self.__init__(71, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 99:

                self.__init__(22, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 100:

                self.__init__(35, self.player, self.basePosX, self.basePosY)
                success = True

        elif rounds > 7:
            ran = random.randint(0, 100)

            if ran < 10:

                self.__init__(61, self.player, self.basePosX, self.basePosY)
                success = True

            elif 10 <= ran < 20:

                self.__init__(21, self.player, self.basePosX, self.basePosY)
                success = True

            elif 20 <= ran < 30:

                self.__init__(47, self.player, self.basePosX, self.basePosY)
                success = True

            elif 30 <= ran < 40:

                self.__init__(42, self.player, self.basePosX, self.basePosY)
                success = True

            elif 40 <= ran < 50:

                self.__init__(68, self.player, self.basePosX, self.basePosY)
                success = True

            elif 50 <= ran < 60:

                self.__init__(69, self.player, self.basePosX, self.basePosY)
                success = True

            elif 60 <= ran < 70:

                self.__init__(70, self.player, self.basePosX, self.basePosY)
                success = True

            elif 70 <= ran < 75:

                self.__init__(71, self.player, self.basePosX, self.basePosY)
                success = True

            elif 75 <= ran < 80:

                self.__init__(22, self.player, self.basePosX, self.basePosY)
                success = True

            elif 80 <= ran < 90:

                self.__init__(39, self.player, self.basePosX, self.basePosY)
                success = True

            elif 90 <= ran < 100:

                self.__init__(36, self.player, self.basePosX, self.basePosY)
                success = True

            elif ran == 100:

                self.__init__(35, self.player, self.basePosX, self.basePosY)
                success = True


        return success