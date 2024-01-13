import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
import consts
import specfunctions
import buttons
from settings import settings
from localisation import Localisation


class SliderText(pygame.sprite.Sprite):
    def __init__(self, x, y, slider, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.slider = slider
        self.font = pygame.font.Font(None, 45)
        self.update()

    def update(self, *args):
        self.image = self.font.render(str(self.slider.getValue()), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.y = self.y


class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, fsize, text, *groups):
        super().__init__(*groups)
        self.font = pygame.font.Font(None, fsize)
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_text(self, text):
        self.image = self.font.render(text, True, (255, 255, 255))


def update_settings(music, sound, lang=None):
    settings.vol_music = music
    settings.vol_sound = sound
    if lang is not None:
        settings.language = lang
    specfunctions.set_music_volume()


def update_text(button, t1, t2, t3):
    button.set_text(Localisation.back())
    button.update()
    t1.set_text(Localisation.music())
    t2.set_text(Localisation.sound())
    t3.set_text(Localisation.language())


def settings_menu():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    button = buttons.EscapeButton(all_sprites, text=Localisation.back(), x=consts.WIDTH // 2, y=650, f_size=45)

    music_slider = Slider(consts.SCREEN, consts.WIDTH // 2 - 100, 100, 400, 20,
                          min=0, max=100, step=1, colour=(120, 120, 120),
                          handleColour=(200, 200, 200), initial=settings.vol_music * 100)

    sound_slider = Slider(consts.SCREEN, consts.WIDTH // 2 - 100, 250, 400, 20,
                          min=0, max=100, step=1, colour=(120, 120, 120),
                          handleColour=(200, 200, 200), initial=settings.vol_sound * 100)

    SliderText(consts.WIDTH // 2 + 100, 140, music_slider, all_sprites)
    SliderText(consts.WIDTH // 2 + 100, 290, sound_slider, all_sprites)

    dropdown = Dropdown(consts.SCREEN, consts.WIDTH // 2 - 100, 400, 400, 40,
                        name=settings.langs[int(settings.language)],
                        choices=settings.langs.values(),
                        values=[settings.eng, settings.rus],
                        textColour=(255, 255, 255), fontSize=38, inactiveColour=(0, 0, 0), hoverColour=(120, 120, 120),
                        pressedColour=(120, 120, 120))

    t1 = Text(consts.WIDTH // 2 - 320, 100, 45, Localisation.music(), all_sprites)
    t2 = Text(consts.WIDTH // 2 - 320, 250, 45, Localisation.sound(), all_sprites)
    t3 = Text(consts.WIDTH // 2 - 320, 405, 45, Localisation.language(), all_sprites)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            all_sprites.update(event)
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        pygame_widgets.update(events)
        update_settings(music_slider.getValue() / 100, sound_slider.getValue() / 100, dropdown.getSelected())
        update_text(button, t1, t2, t3)
        if button.clicked:
            music_slider.hide()
            sound_slider.hide()
            dropdown.hide()
            return
        pygame.display.flip()
        clock.tick(consts.FPS)


def ingame_settings_menu():
    pygame.mixer.pause()
    surface = pygame.Surface(consts.SIZE)
    surface.blit(consts.SCREEN, (0, 0))
    s = pygame.Surface((consts.WIDTH // 2, consts.HEIGHT // 2), pygame.SRCALPHA)
    s.fill((0, 0, 0, 128))
    surface.blit(s, (consts.WIDTH // 4, consts.HEIGHT // 4))

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    music_slider = Slider(consts.SCREEN, consts.WIDTH // 2, consts.HEIGHT // 4 + 50, 200, 10,
                          min=0, max=100, step=1, colour=(100, 100, 100),
                          handleColour=(180, 180, 180), initial=settings.vol_music * 100)

    sound_slider = Slider(consts.SCREEN, consts.WIDTH // 2, consts.HEIGHT // 4 + 150, 200, 10,
                          min=0, max=100, step=1, colour=(100, 100, 100),
                          handleColour=(180, 180, 180), initial=settings.vol_sound * 100)

    SliderText(consts.WIDTH // 2 + 100, consts.HEIGHT // 4 + 70, music_slider, all_sprites)
    SliderText(consts.WIDTH // 2 + 100, consts.HEIGHT // 4 + 170, sound_slider, all_sprites)

    Text(consts.WIDTH // 2 - 200, consts.HEIGHT // 4 + 50, 34, Localisation.music(), all_sprites)
    Text(consts.WIDTH // 2 - 200, consts.HEIGHT // 4 + 150, 34, Localisation.sound(), all_sprites)

    return_button = buttons.EscapeButton(all_sprites, text=Localisation.back(), x=consts.WIDTH // 2,
                                         y=consts.HEIGHT // 4 + 250, f_size=42)

    escape_button = buttons.EscapeButton(all_sprites, text=Localisation.exit(), x=consts.WIDTH // 2,
                                         y=consts.HEIGHT // 4 + 310, f_size=42, f_active_color=(255, 0, 0))

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            all_sprites.update(event)
        consts.SCREEN.blit(surface, (0, 0))
        all_sprites.draw(consts.SCREEN)
        pygame_widgets.update(events)
        update_settings(music_slider.getValue() / 100, sound_slider.getValue() / 100)
        if escape_button.clicked or return_button.clicked:
            music_slider.hide()
            sound_slider.hide()
            if return_button.clicked:
                pygame.mixer.unpause()
            return escape_button.clicked
        pygame.display.flip()
        clock.tick(consts.FPS)
