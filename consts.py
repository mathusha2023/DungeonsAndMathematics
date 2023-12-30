import pygame
import random

pygame.init()

SIZE = WIDTH, HEIGHT = 1080, 720
SCREEN = pygame.display.set_mode(SIZE)
FPS = 60
TITLE = "Dungeons&Mathematics: " + random.choice(("2 + 2 = 5",
                                                  "физика лучше!",
                                                  "история о бесполезной науке",
                                                  "убей их всех!",
                                                  "попробуй Soul Knight!"))
TILE_WIDTH = TILE_HEIGHT = 60
