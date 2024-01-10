import pygame
import os
import sys
import db
from settings import Settings


def load_image(name, colorkey=None):
    fullname = os.path.join(r"data\images", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    db.connection.close()
    Settings.write()
    sys.exit()
