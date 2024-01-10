import pygame
import consts
import specfunctions
import sounds


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
    sounds.tp_sound()
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
