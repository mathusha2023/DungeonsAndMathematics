import pygame
import math
import consts
import specfunctions
from spriteGroups import all_sprites, enemies, player_group, player_bullets
import weapon


class Enemy(pygame.sprite.Sprite):
    left_st_im = specfunctions.load_image("ura/ura_left_st.png")
    left_go1_im = specfunctions.load_image("ura/ura_left_go1.png")
    left_go2_im = specfunctions.load_image("ura/ura_left_go2.png")
    right_st_im = specfunctions.load_image("ura/ura_right_st.png")
    right_go1_im = specfunctions.load_image("ura/ura_right_go1.png")
    right_go2_im = specfunctions.load_image("ura/ura_right_go2.png")

    right = 0
    left = 1

    def __init__(self, pos_x, pos_y, checkrect_size=600):
        super().__init__(enemies, all_sprites)
        self.image = Enemy.right_st_im
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.checkrect_size = checkrect_size
        self.checking_rect = pygame.Rect(
            (0, 0, self.rect.width + self.checkrect_size, self.rect.height + self.checkrect_size))
        self.update_checkrect()
        self.left_ims = [Enemy.left_go1_im, Enemy.left_go2_im]
        self.right_ims = [Enemy.right_go1_im, Enemy.right_go2_im]
        self.im = 0
        self.counter = 0
        self.state = Enemy.right
        self.weapon = None
        self.speed = 3
        self.ammo = 1000000000000000000000000000000000000
        self.hp = 10

    def update_checkrect(self):
        self.checking_rect.x = self.rect.x - self.checkrect_size // 2
        self.checking_rect.y = self.rect.y - self.checkrect_size // 2

    def check_player_shot(self):
        for bullet in pygame.sprite.spritecollide(self, player_bullets, False):
            if bullet.is_alive():
                if isinstance(bullet, weapon.Bullet):
                    bullet.kill()
                if isinstance(bullet, weapon.Fist):
                    bullet.attacked = True
                self.hp -= bullet.damage
                if self.hp <= 0:
                    self.kill()
                    if self.weapon:
                        self.weapon.kill()

    def check_player(self):
        return self.checking_rect.colliderect([i for i in player_group][0].rect)

    def update_state(self):
        if [i for i in player_group][0].rect.centerx > self.rect.centerx:
            self.state = Enemy.right
        else:
            self.state = Enemy.left

    def update(self, *args):
        self.update_checkrect()
        self.update_state()
        if self.state == Enemy.right:
            self.image = Enemy.right_st_im
        else:
            self.image = Enemy.left_st_im
        self.check_player_shot()
        if not self.check_player():
            return


class SniperEnemy(Enemy):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, checkrect_size=800)
        self.counter = 2 * consts.FPS
        self.weapon = weapon.Rifle(pos_x, pos_y, owner=self, is_players=False)

    def update(self, *args):
        super().update(*args)
        self.counter += 1
        if not self.check_player():
            return
        if not self.counter % (2 * consts.FPS):
            self.counter = 1
            self.shoot()

    def shoot(self):
        self.weapon.shoot(*[i for i in player_group][0].rect.center)


class FollowEnemy(Enemy):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, checkrect_size=800)
        self.weapon = weapon.ShotGun(pos_x, pos_y, owner=self, is_players=False)
        self.moving = False

    def shoot(self):
        self.weapon.shoot(*[i for i in player_group][0].rect.center)

    def check_distance(self):
        x1, y1 = [i for i in player_group][0].rect.topleft
        x2, y2 = self.rect.topleft
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= 300

    def update(self, *args):
        super().update(*args)
        if not self.check_player():
            return
        if self.check_distance():
            if self.weapon.is_ready():
                self.shoot()
            self.moving = False
        else:
            self.move_to_player()
            self.moving = True
        if self.moving:
            self.image = self.left_ims[self.im] if self.state == Enemy.left else self.right_ims[self.im]
            self.counter += 1
            if not self.counter % 5:
                self.im = 1 - self.im
                self.counter = 0

    def move_to_player(self):
        x1, y1 = [i for i in player_group][0].rect.topleft
        x2, y2 = self.rect.topleft
        self.rect = self.rect.move(math.copysign(self.speed, x1 - x2), math.copysign(self.speed, y1 - y2))
