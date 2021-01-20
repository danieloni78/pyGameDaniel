import pygame

def loadStaticPlayer(number):
    p_static = [pygame.image.load(f'textures/player/static/{number}/1.png'),
                 pygame.image.load(f'textures/player/static/{number}/2.png')]
    return p_static


def loadStaticEnemy(number):
    e_static = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
                 pygame.image.load(f'textures/enemy/static/{number}/2.png')]
    return e_static


def loadJumpPlayer(number):
    p_jump = pygame.image.load(f'textures/player/jump/{number}/1.png')
    return p_jump


def loadJumpEnemy(number):
    e_jump = pygame.image.load(f'textures/enemy/jump/{number}/1.png')
    return e_jump


def loadMovePlayer(number):
    p_move = [pygame.image.load(f'textures/player/static/{number}/1.png'),
               pygame.image.load(f'textures/player/jump/{number}/1.png'),
               pygame.image.load(f'textures/player/static/{number}/2.png'),
               pygame.image.load(f'textures/player/jump/{number}/2.png')]
    return p_move


def loadMoveEnemy(number):
    e_move = [pygame.image.load(f'textures/enemy/static/{number}/1.png'),
               pygame.image.load(f'textures/enemy/jump/{number}/1.png'),
               pygame.image.load(f'textures/enemy/static/{number}/2.png'),
               pygame.image.load(f'textures/enemy/jump/{number}/2.png')]
    return e_move