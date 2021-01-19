import pygame

#Chose System Font



def print_transparent(target, source, location, opacity):
    x_temp = location[0]
    y_temp = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x_temp, -y_temp))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

