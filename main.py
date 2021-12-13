import pygame
from pygame.locals import *
import time

if __name__ == "__main__":
    pygame.init()

    display_x = 800
    display_y = 800
    displayRPG = [128, 128, 128]

    surface = pygame.display.set_mode((display_x, display_y))
    surface.fill((displayRPG))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
