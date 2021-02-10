import pygame

#Chose System Font



def print_transparent(screen, image, coordinates, opacity):
    x_temp = coordinates[0]
    y_temp = coordinates[1]
    tempImg = pygame.Surface((image.get_width(), image.get_height())).convert()
    tempImg.blit(screen, (-x_temp, -y_temp))
    tempImg.blit(image, (0, 0))
    tempImg.set_alpha(opacity)
    screen.blit(tempImg, coordinates)

