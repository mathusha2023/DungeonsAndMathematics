import pygame
import math
import consts
import specfunctions
from spriteGroups import all_sprites, enemies, player_group, player_bullets, walls
from settings import settings
import weapon


class Enemy(pygame.sprite.Sprite):
    left_st_im = None
    left_go1_im = None
    left_go2_im = None
    right_st_im = None
    right_go1_im = None
    right_go2_im = None

    right = 0
    left = 1

    def __init__(self, pos_x, pos_y, checkrect_sizex=consts.WIDTH, checkrect_sizey=consts.HEIGHT):
        super().__init__(enemies, all_sprites)
        self.image = self.right_st_im
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.checkrect_sizex = checkrect_sizex
        self.checkrect_sizey = checkrect_sizey
        self.checking_rect = pygame.Rect(
            (0, 0, self.rect.width + self.checkrect_sizex, self.rect.height + self.checkrect_sizey))
        self.update_checkrect()
        self.left_ims = [self.left_go1_im, self.left_go2_im]
        self.right_ims = [self.right_go1_im, self.right_go2_im]
        self.im = 0
        self.counter = 0
        self.state = Enemy.right
        self.weapon = None
        self.speed = 3
        self.ammo = 1000000000000000000000000000000000000
        self.hp = 10

    def update_checkrect(self):
        self.checking_rect.x = self.rect.x - self.checkrect_sizex // 2
        self.checking_rect.y = self.rect.y - self.checkrect_sizey // 2

    def stop_wall_moving(self):
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x = self.prev_x
            self.rect.y = self.prev_y

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
                    [i for i in player_group][0].score += 10
                    if self.weapon:
                        self.weapon.kill()
                    return

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
            self.image = self.right_st_im
        else:
            self.image = self.left_st_im
        self.check_player_shot()
        if not self.check_player():
            return
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

    def check_distance(self):
        x1, y1 = [i for i in player_group][0].rect.topleft
        x2, y2 = self.rect.topleft
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= 300

    def move_to_player(self):
        x1, y1 = [i for i in player_group][0].rect.center
        x2, y2 = self.rect.center
        if not (x2 - self.speed < x1 < x2 + self.speed):
            self.rect.x += math.copysign(self.speed, x1 - x2)
            self.stop_wall_moving()
            self.prev_x = self.rect.x
        if not (y2 - self.speed < y1 < y2 + self.speed):
            self.rect.y += math.copysign(self.speed, y1 - y2)
            self.stop_wall_moving()


class SniperEnemy(Enemy):
    left_st_im = specfunctions.load_image("enemies/enemy1/enemy_sniper_left.png")
    right_st_im = specfunctions.load_image("enemies/enemy1/enemy_sniper_right.png")

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.counter = 2 * consts.FPS
        self.weapon = weapon.Rifle(pos_x, pos_y, owner=self, is_players=False)
        self.hp = 6

    def update(self, *args):
        super().update(*args)
        if self.counter < 2 * consts.FPS:
            self.counter += 1
        if not self.check_player():
            return
        if not self.counter % (2 * consts.FPS):
            self.counter = 1
            self.shoot()

    def shoot(self):
        self.weapon.shoot(*[i for i in player_group][0].rect.center)


class FollowEnemy(Enemy):
    left_st_im = specfunctions.load_image("enemies/enemy2/left_st_enemy.png")
    left_go1_im = specfunctions.load_image("enemies/enemy2/left_go1_enemy.png")
    left_go2_im = specfunctions.load_image("enemies/enemy2/left_go2_enemy.png")
    right_st_im = specfunctions.load_image("enemies/enemy2/right_st_enemy.png")
    right_go1_im = specfunctions.load_image("enemies/enemy2/right_go1_enemy.png")
    right_go2_im = specfunctions.load_image("enemies/enemy2/right_go2_enemy.png")

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.weapon = weapon.ShotGun(pos_x, pos_y, owner=self, is_players=False)
        self.moving = False
        self.hp = 8

    def shoot(self):
        self.weapon.shoot(*[i for i in player_group][0].rect.center)

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


class RamEnemy(Enemy):
    left_st_im = specfunctions.load_image("enemies/enemy3/enemy3_left1.png")
    right_st_im = specfunctions.load_image("enemies/enemy3/enemy3_right1.png")

    def __init__(self, pos_x, pos_y):
        if settings.spiders:
            super().__init__(pos_x, pos_y, checkrect_sizex=2160, checkrect_sizey=1440)
        else:
            super().__init__(pos_x, pos_y)
        self.dash_left = []
        self.dash_right = []
        self.add_frames()
        self.damage_counter = consts.FPS
        self.ram_counter = 1 * consts.FPS
        self.damage = 2
        self.path = 0
        self.ramming = False
        self.ram_speed_x = None
        self.ram_speed_y = None
        self.ram_x = None
        self.ram_y = None

    def add_frames(self):
        self.left_ims = []
        self.right_ims = []
        for i in range(1, 8):
            self.left_ims.append(specfunctions.load_image(f"enemies/enemy3/enemy3_left{i}.png"))
            self.right_ims.append(specfunctions.load_image(f"enemies/enemy3/enemy3_right{i}.png"))
            self.dash_left.append(specfunctions.load_image(f"enemies/enemy3/enemy3_left{i}_dash.png"))
            self.dash_right.append(specfunctions.load_image(f"enemies/enemy3/enemy3_right{i}_dash.png"))

    def update(self, *args):
        super().update(*args)
        if self.damage_counter < consts.FPS:
            self.damage_counter += 1
        if self.ram_counter < 6 * consts.FPS and not self.ramming:
            self.ram_counter += 1
        if not (self.check_player() or self.ramming):
            return
        self.collide_player()
        if (self.check_distance() and not self.ram_counter % (1 * consts.FPS)) or self.ramming:
            if not self.ramming:
                self.ram(*[i for i in player_group][0].rect.center)
            else:
                self.ram()
        else:
            self.move_to_player()
        if self.ramming:
            self.image = self.dash_left[self.im] if self.state == Enemy.left else self.dash_right[self.im]
        else:
            self.image = self.left_ims[self.im] if self.state == Enemy.left else self.right_ims[self.im]
        self.counter += 1
        if not self.counter % 2:
            self.im = (self.im + 1) % len(self.left_ims)
            self.counter = 0

    def collide_player(self):
        player = [i for i in player_group][0]
        if pygame.sprite.collide_rect(self, player):
            if not self.damage_counter % consts.FPS:
                if self.ramming:
                    player.get_damage(self.damage * 2)
                else:
                    player.get_damage(self.damage)
                self.damage_counter = 1

    def ram(self, x=None, y=None):
        if x:
            if not self.get_ram_speed(x, y):
                return
            self.ram_x = x
            self.ram_y = y
            self.path = 0
            self.ramming = True
            self.ram_counter = 1
            self.damage_counter = consts.FPS
        self.rect.x += self.ram_speed_x
        self.stop_wall_moving()
        self.prev_x = self.rect.x
        self.rect.y += self.ram_speed_y
        self.check_ram_range()
        self.stop_wall_moving()

    def check_ram_range(self):
        self.path += math.sqrt(self.ram_speed_x ** 2 + self.ram_speed_y ** 2)
        if self.path > 1000:
            self.ramming = False

    def get_ram_speed(self, x, y):
        dx = x - self.rect.centerx
        dy = y - self.rect.centery
        d = math.sqrt(dx ** 2 + dy ** 2)
        frames = math.ceil(d / (self.speed * 3))
        if frames > 2:
            vx, vy = dx / frames, dy / frames
            self.ram_speed_x = vx
            self.ram_speed_y = vy
            return True
        return False

    def stop_wall_moving(self):
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x = self.prev_x
            self.rect.y = self.prev_y
            self.ramming = False

    def update_state(self):
        if not self.ramming:
            super().update_state()
