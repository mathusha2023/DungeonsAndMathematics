import pygame
import consts
import db
import specfunctions
import buttons


def records_menu():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    button = buttons.ExitButton(all_sprites, text="Назад", x=consts.WIDTH // 2, y=650, f_size=45)

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
