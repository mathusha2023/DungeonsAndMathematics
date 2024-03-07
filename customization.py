import pygame
import consts
import buttons
import specfunctions
from localisation import Localisation


class SkinsMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


def customization_menu():
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    button = buttons.EscapeButton(all_sprites, text=Localisation.back(), x=consts.WIDTH // 2, y=650, f_size=45)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            all_sprites.update(event)
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        if button.clicked:
            return
        pygame.display.flip()
        clock.tick(consts.FPS)
