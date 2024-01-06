import pygame
import consts
import specfunctions
from spriteGroups import bonus_group, all_sprites


class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, bonus_group)
        self.rect = self.image.get_rect()
        self.rect.x = consts.TILE_WIDTH * pos_x - self.rect.width // 2
        self.rect.y = consts.TILE_HEIGHT * pos_y - self.rect.height // 2


class Ammo(Bonus):
    image = specfunctions.load_image("ammo.png")

    def __init__(self, pos_x, pos_y):
        self.image = Ammo.image
        super().__init__(pos_x, pos_y)

    def take(self, player):
        player.ammo += 25
        self.kill()


class Heal(Bonus):
    image = specfunctions.load_image("heal.png")

    def __init__(self, pos_x, pos_y):
        self.image = Heal.image
        super().__init__(pos_x, pos_y)

    def take(self, player):
        player.hp += 3
        if player.hp > 10:
            player.hp = 10
        self.kill()
