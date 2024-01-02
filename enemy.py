import pygame
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

    def __init__(self, pos_x, pos_y):
        super().__init__(enemies, all_sprites)
        self.image = Enemy.right_st_im
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.checking_rect = pygame.Rect((0, 0, self.rect.width + 600, self.rect.height + 600))
        self.update_checkrect()
        self.left_ims = [Enemy.left_go1_im, Enemy.left_go2_im]
        self.right_ims = [Enemy.right_go1_im, Enemy.right_go2_im]
        self.im = 0
        self.counter = 0
        self.state = Enemy.right
        self.weapon = None
        self.speed = 5
        self.ammo = 1000000000000000000000000000000000000
        self.hp = 10

    def update_checkrect(self):
        self.checking_rect.x = self.rect.x - 300
        self.checking_rect.y = self.rect.y - 300

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
                    self.weapon.kill()

    def check_player(self):
        return self.checking_rect.colliderect([i for i in player_group][0].rect)

    def update(self, *args):
        self.update_checkrect()
        self.check_player_shot()
        if not self.check_player():
            return

    def shoot(self):
        self.weapon.shoot(*[i for i in player_group][0].rect.center)


class SniperEnemy(Enemy):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
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
