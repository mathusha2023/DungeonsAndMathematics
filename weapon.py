import pygame
import math
import consts


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT

    def update(self, *args):
        if args:
            self.rect.x = args[0]
            self.rect.y = args[1]


class MeleeWeapon(Weapon):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(pos_x, pos_y, *groups)


class RangedWeapon(Weapon):
    def __init__(self, pos_x, pos_y, bullets_group, weapons_group, *groups):
        self.image = pygame.Surface((25, 20))
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 25, 20))
        super().__init__(pos_x, pos_y, weapons_group, *groups)
        self.groups = list(groups) + [bullets_group]

    def shoot(self, x, y):
        Bullet(self.rect.x, self.rect.y, x, y, 200, *self.groups)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, target_x, target_y, brange, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((12, 12))
        pygame.draw.circle(self.image, (255, 0, 0), (6, 6), 6)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.target_x = target_x
        self.target_y = target_y
        self.brange = brange
        self.speed = 25
        self.vx, self.vy = self.get_speeds()

    def get_speeds(self):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        d = math.sqrt(dx ** 2 + dy ** 2)
        frames = math.ceil(d / self.speed)
        return dx / frames, dy / frames

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)
