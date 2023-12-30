import pygame
import math
import consts
import specfunctions
from spriteGroups import bullets, weapons, all_sprites, walls


class Weapon(pygame.sprite.Sprite):
    image_left = None
    image_right = None
    right = 0
    left = 1

    def __init__(self, pos_x, pos_y, owner=None):
        super().__init__(weapons, all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.state = Weapon.right
        self.owner = owner

    def update(self, *args):
        if self.owner is None:
            return
        if self.state == Weapon.left:
            self.image = self.image_left
            self.rect.right = self.owner.rect.centerx + 15
        else:
            self.image = self.image_right
            self.rect.x = self.owner.rect.centerx - 15
        self.rect.y = self.owner.rect.centery
        self.state = self.owner.state

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        Bullet(start_x, self.rect.centery, x, y)


class Rifle(Weapon):
    image_left = specfunctions.load_image("weapons/weapon1_left.png")
    image_right = specfunctions.load_image("weapons/weapon1_right.png")

    def __init__(self, pos_x, pos_y, owner=None):
        self.image = Rifle.image_right
        super().__init__(pos_x, pos_y, owner)
        self.counter = consts.FPS // 1.5

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        Bullet(start_x, self.rect.centery, x, y, speed=35)
        self.counter = 1

    def update(self, *args):
        super().update(*args)
        if self.counter < consts.FPS // 1.5:
            self.counter += 1


class ShotGun(Weapon):
    image_left = specfunctions.load_image("weapons/weapon2_left.png")
    image_right = specfunctions.load_image("weapons/weapon2_right.png")

    def __init__(self, pos_x, pos_y, owner=None):
        self.image = ShotGun.image_right
        super().__init__(pos_x, pos_y, owner)
        self.counter = consts.FPS

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        Bullet(start_x, self.rect.centery, x, y)
        Bullet(start_x, self.rect.centery, x - 20, y - 20)
        Bullet(start_x, self.rect.centery, x + 20, y - 20)
        Bullet(start_x, self.rect.centery, x - 40, y - 40)
        Bullet(start_x, self.rect.centery, x + 40, y - 40)
        self.counter = 1

    def update(self, *args):
        super().update(*args)
        if self.counter < consts.FPS:
            self.counter += 1


class Bullet(pygame.sprite.Sprite):
    image = specfunctions.load_image("bullet.png")

    def __init__(self, pos_x, pos_y, target_x, target_y, speed=25):
        super().__init__(bullets, all_sprites)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed
        self.vx, self.vy = self.get_speeds()

    def get_speeds(self):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        d = math.sqrt(dx ** 2 + dy ** 2)
        frames = math.ceil(d / self.speed)
        if frames:
            vx, vy = dx / frames, dy / frames
        else:
            vx, vy = dx, dy
        return vx, vy

    def update(self, *args):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, walls):
            self.kill()


weapons_list = [Rifle, ShotGun]
