import pygame

def loadStaticPlayer(number):

    if number == 26 or number == 34 or number == 46 or number == 64 or number >= 67:
        p_static = [pygame.image.load(f'textures/player/static/{number}/1.png'),
                   pygame.image.load(f'textures/player/jump/{number}/1.png'),
                   pygame.image.load(f'textures/player/static/{number}/2.png'),
                   pygame.image.load(f'textures/player/jump/{number}/2.png')]

    else:
        p_static = [pygame.image.load(f'textures/player/static/{number}/1.png'),
                     pygame.image.load(f'textures/player/static/{number}/2.png'),
                    pygame.image.load(f'textures/player/static/{number}/1.png'),
                    pygame.image.load(f'textures/player/static/{number}/2.png')
                    ]
    return p_static


def loadStaticEnemy(number):

    if number == 26 or number == 34 or number == 46 or number == 64 or number >= 67:
        e_static = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/static/{number}/2.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/2.png')]

    else:
        e_static = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
                     pygame.image.load(f'textures/enemy/static/{number}/2.png'),
                    pygame.image.load(f'textures/enemy/static/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/static/{number}/2.png')
                    ]
    return e_static


def loadJumpPlayer(number):
    p_jump = pygame.image.load(f'textures/player/jump/{number}/1.png')
    return p_jump


def loadJumpEnemy(number):
    e_jump = pygame.image.load(f'textures/enemy/jump/{number}/1.png')
    return e_jump


def loadMovePlayer(number):

    if number == 7:
        p_move = [pygame.image.load(f'textures/player/jump/{number}/1.png'),
                   pygame.image.load(f'textures/player/jump/{number}/2.png'),
                   pygame.image.load(f'textures/player/jump/{number}/3.png'),
                   pygame.image.load(f'textures/player/jump/{number}/2.png')]

    else:
        p_move = [pygame.image.load(f'textures/player/static/{number}/1.png'),
                   pygame.image.load(f'textures/player/jump/{number}/1.png'),
                   pygame.image.load(f'textures/player/static/{number}/2.png'),
                   pygame.image.load(f'textures/player/jump/{number}/2.png')]
    return p_move


def loadMoveEnemy(number):

    if number == 7:
        e_move = [pygame.image.load(f'textures/enemy/jump/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/2.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/3.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/2.png')]

    else:
        e_move = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/1.png'),
                    pygame.image.load(f'textures/enemy/static/{number}/2.png'),
                    pygame.image.load(f'textures/enemy/jump/{number}/2.png')]
    return e_move


def loadSpecialPlayer(number):

    if number < 4 or number == 7:
        p_special = [pygame.image.load(f'textures/player/special/{number}/1.png'),
                   pygame.image.load(f'textures/player/special/{number}/2.png'),
                   pygame.image.load(f'textures/player/special/{number}/3.png'),
                   pygame.image.load(f'textures/player/special/{number}/4.png')]

    elif number == 17 or number == 22:
        p_special = [pygame.image.load(f'textures/player/special/{number}/1.png'),
                     pygame.image.load(f'textures/player/special/{number}/1.png'),
                     pygame.image.load(f'textures/player/special/{number}/1.png'),
                     pygame.image.load(f'textures/player/special/{number}/1.png')]

    else:
        p_special = [pygame.image.load(f'textures/player/static/{number}/1.png'),
               pygame.image.load(f'textures/player/jump/{number}/1.png'),
               pygame.image.load(f'textures/player/static/{number}/2.png'),
               pygame.image.load(f'textures/player/jump/{number}/2.png')]


    return p_special


def loadSpecialEnemy(number):

    if number < 4 or number == 7:
        e_special = [pygame.image.load(f'textures/enemy/special/{number}/1.png'),
                   pygame.image.load(f'textures/enemy/special/{number}/2.png'),
                   pygame.image.load(f'textures/enemy/special/{number}/3.png'),
                   pygame.image.load(f'textures/enemy/special/{number}/4.png')]

    elif number == 17 or number == 22:
        e_special = [pygame.image.load(f'textures/enemy/special/{number}/1.png'),
                     pygame.image.load(f'textures/enemy/special/{number}/1.png'),
                     pygame.image.load(f'textures/enemy/special/{number}/1.png'),
                     pygame.image.load(f'textures/enemy/special/{number}/1.png')]

    else:
        e_special = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
               pygame.image.load(f'textures/enemy/jump/{number}/1.png'),
               pygame.image.load(f'textures/enemy/static/{number}/2.png'),
               pygame.image.load(f'textures/enemy/jump/{number}/2.png')]

    return e_special