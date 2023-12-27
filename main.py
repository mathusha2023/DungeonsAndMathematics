import pygame
import consts
import buttons
import specfunctions
import game

pygame.display.set_caption(consts.TITLE)
pygame.display.set_icon(specfunctions.load_image("logo.png"))

all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()


class Title(pygame.sprite.Sprite):
    image = specfunctions.load_image("title.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Title.image
        self.rect = self.image.get_rect()
        self.rect.center = (consts.WIDTH // 2, 150)


Title()
buttons.Button(all_sprites, text="Играть!", x=consts.WIDTH // 2, y=300, f_size=40,
               press_event=lambda: game.start_game(clock))
buttons.Button(all_sprites, text="Рекорды", x=consts.WIDTH // 2, y=350, f_size=40,
               press_event=lambda: print("RECORDS!"))
buttons.Button(all_sprites, text="Настройки", x=consts.WIDTH // 2, y=400, f_size=40,
               press_event=lambda: print("SETTINGS!"))
buttons.Button(all_sprites, text="Выход", x=consts.WIDTH // 2, y=450, f_size=40,
               press_event=specfunctions.terminate)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            specfunctions.terminate()
        all_sprites.update(event)
    consts.SCREEN.fill((0, 0, 0))
    all_sprites.draw(consts.SCREEN)
    pygame.display.flip()
    clock.tick(consts.FPS)
