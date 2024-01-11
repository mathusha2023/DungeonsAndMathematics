import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.dropdown import Dropdown
import consts
import specfunctions
import buttons


class Settings:

    @staticmethod
    def config():
        with open("data/db/settings.txt") as file:
            return list(map(float, file.readlines()))

    @staticmethod
    def write():
        with open("data/db/settings.txt", "w") as file:
            file.write("\n".join(map(str, [Settings.vol_music, Settings.vol_sound, Settings.language])))

    eng = 0
    rus = 1
    langs = {0: "english", 1: "русский"}
    start_settings = config()

    vol_music = start_settings[0]
    vol_sound = start_settings[1]
    language = start_settings[2]


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
    def __init__(self, y, text, *groups):
        super().__init__(*groups)
        self.image = pygame.font.Font(None, 45).render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = consts.WIDTH // 2 - 320
        self.rect.y = y


def update_settings(music, sound, lang):
    Settings.vol_music = music
    Settings.vol_sound = sound
    if lang is not None:
        Settings.language = lang
    specfunctions.set_music_volume()


def settings_menu():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    button = buttons.EscapeButton(all_sprites, text="Назад", x=consts.WIDTH // 2, y=650, f_size=45)

    music_slider = Slider(consts.SCREEN, consts.WIDTH // 2 - 100, 100, 400, 20,
                          min=0, max=100, step=1, colour=(120, 120, 120),
                          handleColour=(200, 200, 200), initial=Settings.vol_music * 100)

    sound_slider = Slider(consts.SCREEN, consts.WIDTH // 2 - 100, 250, 400, 20,
                          min=0, max=100, step=1, colour=(120, 120, 120),
                          handleColour=(200, 200, 200), initial=Settings.vol_sound * 100)

    SliderText(consts.WIDTH // 2 + 100, 140, music_slider, all_sprites)
    SliderText(consts.WIDTH // 2 + 100, 290, sound_slider, all_sprites)

    dropdown = Dropdown(consts.SCREEN, consts.WIDTH // 2 - 100, 400, 400, 40,
                        name=Settings.langs[int(Settings.language)],
                        choices=Settings.langs.values(),
                        values=[Settings.eng, Settings.rus],
                        textColour=(255, 255, 255), fontSize=38, inactiveColour=(0, 0, 0), hoverColour=(120, 120, 120),
                        pressedColour=(120, 120, 120))

    Text(100, "Музыка:", all_sprites)
    Text(250, "Звуки:", all_sprites)
    Text(405, "Язык:", all_sprites)

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
        if button.clicked:
            music_slider.hide()
            sound_slider.hide()
            return
        pygame.display.flip()
        clock.tick(consts.FPS)
