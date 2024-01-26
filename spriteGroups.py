import pygame


class MyGroup(pygame.sprite.Group):
    def draw(self, surface, *args):
        for sprite in self:
            sprite.draw(surface)


all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
player_group = pygame.sprite.Group()
weapons = pygame.sprite.Group()
bullets = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
bonus_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemies_bullets = pygame.sprite.Group()
boss_walls = pygame.sprite.Group()
boss_group = MyGroup()
exit_btn_group = pygame.sprite.Group()
