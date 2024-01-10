import pygame
import math
import consts
import specfunctions
import sounds
from spriteGroups import bullets, weapons, all_sprites, walls, player_bullets, enemies_bullets


class Weapon(pygame.sprite.Sprite):
    image_left = None
    image_right = None
    right = 0
    left = 1

    def __init__(self, pos_x, pos_y, owner=None, counter=1, is_players=True):
        super().__init__(weapons, all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.state = Weapon.right
        self.owner = owner
        self.counter = counter
        self.max_counter = counter
        self.is_players = is_players

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
        if self.counter < self.max_counter:
            self.counter += 1

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        Bullet(start_x, self.rect.centery, x, y, self.is_players)
        self.counter = 1
        self.owner.ammo -= 1

    def is_ready(self):
        return self.counter == self.max_counter


class Rifle(Weapon):
    image_left = specfunctions.load_image("weapons/weapon1_left.png")
    image_right = specfunctions.load_image("weapons/weapon1_right.png")

    def __init__(self, pos_x, pos_y, owner=None, is_players=True):
        self.image = Rifle.image_right
        super().__init__(pos_x, pos_y, owner, counter=consts.FPS // 1.5, is_players=is_players)

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        speed = 35 if self.is_players else 30
        Bullet(start_x, self.rect.centery, x, y, self.is_players, speed=speed, damage=3, brange=1200)
        self.counter = 1
        self.owner.ammo -= 1


class ShotGun(Weapon):
    image_left = specfunctions.load_image("weapons/weapon2_left.png")
    image_right = specfunctions.load_image("weapons/weapon2_right.png")

    def __init__(self, pos_x, pos_y, owner=None, is_players=True):
        self.image = ShotGun.image_right
        super().__init__(pos_x, pos_y, owner, counter=consts.FPS, is_players=is_players)

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        brange = 450 if self.is_players else 300
        Bullet(start_x, self.rect.centery, x, y, self.is_players, damage=1, brange=brange)
        Bullet(start_x, self.rect.centery, x - 20, y - 20, self.is_players, damage=1, brange=brange)
        Bullet(start_x, self.rect.centery, x + 20, y - 20, self.is_players, damage=1, brange=brange)
        Bullet(start_x, self.rect.centery, x - 40, y - 40, self.is_players, damage=1, brange=brange)
        Bullet(start_x, self.rect.centery, x + 40, y - 40, self.is_players, damage=1, brange=brange)
        self.counter = 1
        self.owner.ammo -= 1


class AK47(Weapon):
    image_left = specfunctions.load_image("weapons/weapon3_left.png")
    image_right = specfunctions.load_image("weapons/weapon3_right.png")

    def __init__(self, pos_x, pos_y, owner=None, is_players=True):
        self.image = AK47.image_right
        super().__init__(pos_x, pos_y, owner, counter=consts.FPS // 3, is_players=is_players)

    def shoot(self, x, y):
        start_x = self.rect.x if self.state == Weapon.left else self.rect.right
        start_y = self.rect.y + (self.rect.centery - self.rect.y) // 2
        Bullet(start_x, start_y, x, y, self.is_players, speed=20, damage=1)
        Bullet(start_x, start_y, x, y, self.is_players, speed=25)
        Bullet(start_x, start_y, x, y, self.is_players, speed=30, damage=1)
        self.counter = 1
        self.owner.ammo -= 1


class Bullet(pygame.sprite.Sprite):
    image_player = specfunctions.load_image("weapons/bullet.png")
    image_enemy = specfunctions.load_image("weapons/bullet_enemy.png")
    yaderka = specfunctions.load_image("weapons/babah.png")

    def __init__(self, pos_x, pos_y, target_x, target_y, is_players, speed=20, damage=2, brange=600):
        if is_players:
            group = player_bullets
            self.image = Bullet.image_player
        else:
            group = enemies_bullets
            self.image = Bullet.image_enemy
        super().__init__(bullets, all_sprites, group)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed
        self.damage = damage
        self.path = 0
        self.range = brange
        self.vx, self.vy = self.get_speeds()
        self.alive_counter = 0

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
        if self.alive_counter:
            self.alive_counter -= 1
            if not self.alive_counter:
                self.kill()
            return
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, walls):
            self.alive_counter = 2
            self.image = Bullet.yaderka
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        self.check_range()

    def is_alive(self):
        return self.image != Bullet.yaderka

    def check_range(self):
        self.path += math.sqrt(self.vx ** 2 + self.vy ** 2)
        if self.path > self.range:
            self.kill()


class Fist(pygame.sprite.Sprite):
    right = 0
    left = 1

    def __init__(self, pos_x, pos_y, state):
        super().__init__(all_sprites, bullets, player_bullets)
        self.sprites = []
        self.load_sprites(state)
        self.im = 0
        self.counter = 0
        self.image = self.sprites[self.im]
        self.rect = self.image.get_rect()
        if state == Fist.left:
            self.rect.x = pos_x - 55
        else:
            self.rect.right = pos_x + 55
        self.rect.y = pos_y - 50
        self.damage = 1
        self.attacked = False

    def load_sprites(self, state):
        for i in range(1, 4):
            if state == Fist.right:
                self.sprites.append(specfunctions.load_image(f"weapons/fists/fist{i}_r.png"))
            else:
                self.sprites.append(specfunctions.load_image(f"weapons/fists/fist{i}_l.png"))

    def update(self, *args):
        if self.im == len(self.sprites):
            self.kill()
            return
        pygame.sprite.spritecollide(self, enemies_bullets, True)
        self.image = self.sprites[self.im]
        self.counter += 1
        if not self.counter % 5:
            self.im += 1
            self.counter = 0

    def is_alive(self):
        return not self.attacked


class Flamethrower(Weapon):
    image_left = specfunctions.load_image("weapons/weapon4_left.png")
    image_right = specfunctions.load_image("weapons/weapon4_right.png")

    def __init__(self, pos_x, pos_y, owner=None):
        self.image = Flamethrower.image_right
        super().__init__(pos_x, pos_y, owner)
        self.fire = None
        self.ammo_counter = 0

    def shoot(self, x, y):
        pass

    def update(self, *args):
        super().update(*args)
        if self.owner is None:
            return
        if not pygame.mouse.get_pressed()[0] or not self.owner.ammo:
            if self.fire:
                self.fire.kill()
                self.fire = None
            return
        if self.fire is None:
            self.fire = Fire(self)
        self.fire.update()
        if not self.ammo_counter % (consts.FPS // 2):
            self.owner.ammo -= 1
        self.ammo_counter = (self.ammo_counter + 1) % consts.FPS


class Fire(pygame.sprite.Sprite):
    def __init__(self, flamethrower):
        super().__init__(all_sprites, bullets, player_bullets)
        self.left_frames = []
        self.right_frames = []
        self.cur_frame = 0
        self.add_frames()
        self.flamethrower = flamethrower
        self.image = None
        self.rect = self.right_frames[0].get_rect()
        self.update_image()
        self.counter = 0
        self.damage = 1

    def add_frames(self):
        for i in range(1, 11):
            self.left_frames.append(specfunctions.load_image(f"weapons/fire_left/{i}.png"))
            self.right_frames.append(specfunctions.load_image(f"weapons/fire_right/{i}.png"))

    def update_image(self):
        if self.flamethrower.state == Weapon.right:
            self.image = self.right_frames[self.cur_frame]
            self.rect.x = self.flamethrower.rect.right
        else:
            self.image = self.left_frames[self.cur_frame]
            self.rect.right = self.flamethrower.rect.x
        self.rect.centery = self.flamethrower.rect.centery

    def update(self, *args):
        self.counter += 1
        self.update_image()
        sounds.fire_sound()
        if not self.counter % 3:
            self.cur_frame = (self.cur_frame + 1) % len(self.right_frames)
            self.counter = 0

    def is_alive(self):
        return True


weapons_list = [Rifle, ShotGun, AK47, Flamethrower]
