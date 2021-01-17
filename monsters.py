import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 595])

#Monster List
monstName = ["Machamp", "Mewtwo", "Gengar"]
# 0 = Melee, 1 = Ranged, 2 = Assassin
monstType = [0, 1, 2]
monstHp = [10, 8, 8]
monstDmg = [2, 3, 3]

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



class monster:
    def __init__(self, select, player, posX, posY):
        self.select = select
        self.player = player
        if player:
            self.static = p_static[select]
            self.jump = p_jump[select]
            self.movement = p_move[select]
            self.speed = 5
        else:
            self.static = e_static[select]
            self.jump = e_jump[select]
            self.movement = e_move[select]
            self.speed = -5
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

    def printMonster(self):
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
            screen.blit(self.movement[self.steps // 4], (self.posX, self.posY))

        #jumping
        if self.action == 2:
            screen.blit(self.jump, (self.posX, self.posY))

        #shooting
        if self.action == 3:
            self.posX = self.basePosX
            self.posY = self.basePosY
            screen.blit(self.static[0], self.posX, self.posY)

    #Chose the Attack Type
    def attack(self):
        if self.type == 0:
            self.meleeAtt()

        #self.action = 0;


    def meleeAtt(self):
        self.action = 1
        self.posX += self.speed
        self.steps +=1


