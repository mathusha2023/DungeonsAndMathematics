import pygame
import webbrowser
import consts
import buttons
import specfunctions
import game
import records
import settingsMenu
import sounds
from localisation import Localisation
import db

db.create_base()
pygame.display.set_caption(consts.TITLE)
pygame.display.set_icon(specfunctions.load_image("logo.png"))
sounds.lobby_music()

all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()


class Title(pygame.sprite.Sprite):
    image = specfunctions.load_image("title.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Title.image
        self.rect = self.image.get_rect()
        self.rect.center = (consts.WIDTH // 2, 200)


Title()
play_btn = buttons.Button(all_sprites, text=Localisation.play(), x=consts.WIDTH // 2, y=375, f_size=45,
                          press_event=game.start_game)
rec_btn = buttons.Button(all_sprites, text=Localisation.records(), x=consts.WIDTH // 2, y=450, f_size=45,
                         press_event=records.records_menu)
sett_btn = buttons.Button(all_sprites, text=Localisation.settings(), x=consts.WIDTH // 2, y=525, f_size=45,
                          press_event=settingsMenu.settings_menu)
exit_btn = buttons.Button(all_sprites, text=Localisation.exit(), x=consts.WIDTH // 2, y=600, f_size=45,
                          press_event=specfunctions.terminate)
support_btn = buttons.RightButton(all_sprites, text=Localisation.support(), x=consts.WIDTH - 25,
                                  y=consts.HEIGHT - 10,
                                  press_event=lambda: webbrowser.open(
                                      "https://www.sberbank.com/sms/pbpn?requisiteNumber=79303042212"),
                                  f_active_color=(0, 255, 0))


def update_text():
    play_btn.set_text(Localisation.play())
    rec_btn.set_text(Localisation.records())
    sett_btn.set_text(Localisation.settings())
    exit_btn.set_text(Localisation.exit())
    support_btn.set_text(Localisation.support())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            specfunctions.terminate()
        all_sprites.update(event)
    update_text()
    consts.SCREEN.fill((0, 0, 0))
    all_sprites.draw(consts.SCREEN)
    pygame.display.flip()
    clock.tick(consts.FPS)
