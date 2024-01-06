import pygame


def lobby_music():
    pygame.mixer.music.load("data/audio/lobby.wav")
    pygame.mixer.music.play(-1)


def dungeon_music():
    pygame.mixer.music.load("data/audio/dungeonmusic.mp3")
    pygame.mixer.music.play(-1)
