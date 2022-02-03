import pygame
from pygame.locals import *

pygame.init()

size = width, height = 1152 , 965
display_surface = pygame.display.set_mode((1152, 965))
pygame.display.set_caption('Diplomacy')
diplomacyboard = pygame.image.load("diplomacyboard.png")

white = (255,255,255)


while True:
    display_surface.fill(white)

    display_surface.blit(diplomacyboard, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        
        pygame.display.update()





