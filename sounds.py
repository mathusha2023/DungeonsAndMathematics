import pygame


def lobby_music():
    pygame.mixer.music.load("data/audio/lobby.wav")
    pygame.mixer.music.play(-1)
    return


def dungeon_music():
    # pygame.mixer.music.load("data/audio/dungeonmusic.mp3")
    # pygame.mixer.music.play(-1)
    return


def boss_music():
    pygame.mixer.music.load("data/audio/bossmusic.mp3")
    pygame.mixer.music.play(-1)
    return


def tp_sound():
    sound = pygame.mixer.Sound("data/audio/tp.wav")
    sound.play()


def shoot_sound():
    sound = pygame.mixer.Sound("data/audio/weapon.wav")
    sound.play()


def punch_sound():
    # sound = pygame.mixer.Sound("data/audio/weapon.mp3")
    # sound.play()
    return


def death_sound():
    sound = pygame.mixer.Sound("data/audio/death.wav")
    sound.play()
