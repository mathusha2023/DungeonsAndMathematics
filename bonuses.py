import pygame
import consts
from spriteGroups import bonus_group, all_sprites


class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, bonus_group)
        self.rect = self.image.get_rect()
        self.rect.x = consts.TILE_WIDTH * pos_x - 15
        self.rect.y = consts.TILE_HEIGHT * pos_y - 15


class Ammo(Bonus):
    def __init__(self, pos_x, pos_y):
        self.image = pygame.Surface((30, 30))
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 30, 30))
        super().__init__(pos_x, pos_y)

    def take(self, player):
        player.ammo += 25
        self.kill()


class Heal(Bonus):
    def __init__(self, pos_x, pos_y):
        self.image = pygame.Surface((30, 30))
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, 30, 30))
        super().__init__(pos_x, pos_y)

    def take(self, player):
        player.hp += 10
        if player.hp > 50:
            player.hp = 50
        self.kill()
