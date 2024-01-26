import pygame
from localisation import Localisation

pygame.init()

SIZE = WIDTH, HEIGHT = 1080, 720
SCREEN = pygame.display.set_mode(SIZE)
FPS = 60
TITLE = "Dungeons&Mathematics: " + Localisation.title()
TILE_WIDTH = TILE_HEIGHT = 60
