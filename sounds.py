import pygame
import specfunctions


def lobby_music():
    pygame.mixer.music.load("data/audio/lobby.wav")
    specfunctions.set_music_volume()
    pygame.mixer.music.play(-1)
    return


def dungeon_music():
    pygame.mixer.music.load("data/audio/dungeonmusic.wav")
    specfunctions.set_music_volume()
    pygame.mixer.music.play(-1)
    return


def boss_music():
    pygame.mixer.music.load("data/audio/bossmusic.mp3")
    specfunctions.set_music_volume()
    pygame.mixer.music.play(-1)
    return


def start_sound():
    sound = pygame.mixer.Sound("data/audio/start.ogg")
    sound.play()


def boss_right_sound():
    sound = pygame.mixer.Sound("data/audio/right.wav")
    sound.play()


def tp_sound():
    sound = pygame.mixer.Sound("data/audio/tp.wav")
    sound.play()


def shoot_sound():
    sound = pygame.mixer.Sound("data/audio/weapon.wav")
    sound.play()


def punch_sound():
    sound = pygame.mixer.Sound("data/audio/punch.wav")
    sound.play()


def death_sound():
    sound = pygame.mixer.Sound("data/audio/death.wav")
    sound.play()


def damage_sound():
    sound = pygame.mixer.Sound("data/audio/damage.wav")
    sound.play()


def fire_sound():
    sound = pygame.mixer.Sound("data/audio/fire.wav")
    sound.play()


def heal_sound():
    sound = pygame.mixer.Sound("data/audio/heal.wav")
    sound.play()


class BossPhrases:
    def __init__(self):
        self.p = []
        self.load_phrases()
        self.p = iter(self.p)

    def load_phrases(self):
        for i in range(1, 8):
            self.p.append(pygame.mixer.Sound(f"data/audio/bossphrases/phrase{i}.wav"))

    def __next__(self):
        next(self.p).play()
