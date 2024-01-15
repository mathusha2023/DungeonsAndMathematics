import pygame
import consts
import specfunctions
from localisation import Localisation


def escape_animation():
    surface = pygame.Surface(consts.SIZE)
    clock = pygame.time.Clock()
    surface.blit(consts.SCREEN, (0, 0))
    x = y = 0
    while y <= consts.HEIGHT // 2 and x <= consts.WIDTH // 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, consts.WIDTH, y))
        pygame.draw.rect(surface, (0, 0, 0), (0, consts.HEIGHT - y, consts.WIDTH, y))
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, x, consts.HEIGHT))
        pygame.draw.rect(surface, (0, 0, 0), (consts.WIDTH - x, 0, x, consts.HEIGHT))
        consts.SCREEN.blit(surface, (0, 0))
        pygame.display.flip()
        x += consts.WIDTH // 2 // consts.FPS
        y += consts.HEIGHT // 2 // consts.FPS
        clock.tick(consts.FPS)


def start_animation():
    surface = pygame.Surface(consts.SIZE)
    surface2 = pygame.Surface(consts.SIZE)
    clock = pygame.time.Clock()
    surface2.blit(consts.SCREEN, (0, 0))
    y = consts.HEIGHT // 2
    x = consts.WIDTH // 2
    while y >= 0 and x >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
        surface.blit(surface2, (0, 0))
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, consts.WIDTH, y))
        pygame.draw.rect(surface, (0, 0, 0), (0, consts.HEIGHT - y, consts.WIDTH, y))
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, x, consts.HEIGHT))
        pygame.draw.rect(surface, (0, 0, 0), (consts.WIDTH - x, 0, x, consts.HEIGHT))
        consts.SCREEN.blit(surface, (0, 0))
        pygame.display.flip()
        x -= consts.WIDTH // 2 // consts.FPS
        y -= consts.HEIGHT // 2 // consts.FPS
        clock.tick(consts.FPS)


def to_be_continued():
    text = pygame.font.Font(None, 50).render(Localisation.to_be_continued(), True,
                                             (255, 255, 255))
    consts.SCREEN.fill((0, 0, 0))
    consts.SCREEN.blit(text, ((consts.WIDTH - text.get_rect().width) // 2, consts.HEIGHT // 2))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN:
                return


def you_dead():
    pygame.mixer.music.stop()
    text = pygame.font.Font(None, 160).render(Localisation.you_dead(), True,
                                              (255, 0, 0))
    consts.SCREEN.blit(text, ((consts.WIDTH - text.get_rect().width) // 2, consts.HEIGHT // 4))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN:
                return
