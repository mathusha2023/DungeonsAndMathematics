import pygame
import math
import specfunctions
from spriteGroups import bullets, weapons, all_sprites, walls


class Weapon(pygame.sprite.Sprite):
    image_left = None
    image_right = None
    right = 0
    left = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(weapons, all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.state = Weapon.right

    def update(self, *args):
        if args:
            self.rect.x = args[0]
            self.rect.y = args[1]
            self.state = args[2]
        # self.image = self.image_left if self.state == Weapon.left else self.image_right
        if self.state == Weapon.left:
            self.image = self.image_left
            self.rect.right = self.rect.x
        else:
            self.image = self.image_right
            self.rect.x = self.rect.right


class MeleeWeapon(Weapon):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)


class RangedWeapon(Weapon):
    def __init__(self, pos_x, pos_y):
        # self.image = pygame.Surface((35, 10))
        # pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 25, 20))
        super().__init__(pos_x, pos_y)

    def shoot(self, x, y):
        Bullet(self.rect.x, self.rect.y, x, y)


class ShotGun(RangedWeapon):
    image_left = specfunctions.load_image("weapons/weaponranged1_left.png")
    image_right = specfunctions.load_image("weapons/weaponranged1_right.png")

    def __init__(self, pos_x, pos_y):
        self.image = ShotGun.image_left
        super().__init__(pos_x, pos_y)


class Bullet(pygame.sprite.Sprite):
    image = specfunctions.load_image("bullet.png")

    def __init__(self, pos_x, pos_y, target_x, target_y):
        super().__init__(bullets, all_sprites)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.target_x = target_x
        self.target_y = target_y
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
        if pygame.sprite.spritecollideany(self, walls):
            self.kill()
