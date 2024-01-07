import pygame
import consts
import specfunctions
import weapon
from spriteGroups import all_sprites, player_group, player_bullets, walls, boss_walls, boss_group


class BossSinus(pygame.sprite.Sprite):
    image = specfunctions.load_image("bosses/sinus/sinus.png")

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, boss_group)
        self.image = BossSinus.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.checkrect_sizex = 7 * consts.TILE_WIDTH
        self.checkrect_sizey = 7 * consts.TILE_HEIGHT
        self.checking_rect = pygame.Rect(
            (0, 0, self.rect.width + self.checkrect_sizex, self.rect.height + self.checkrect_sizey))
        self.update_checkrect()
        self.answerstones = []
        self.spawn_answerstones(pos_x, pos_y)
        self.fight = False
        self.hp = 20

    def update_checkrect(self):
        self.checking_rect.x = self.rect.x - self.checkrect_sizex // 2
        self.checking_rect.y = self.rect.y - self.checkrect_sizey // 2

    def check_player(self):
        return self.checking_rect.colliderect([i for i in player_group][0].rect)

    def spawn_answerstones(self, x, y):
        self.answerstones.append(AnswerStone(x - 8, y - 4))
        self.answerstones.append(AnswerStone(x + 8, y - 4))
        self.answerstones.append(AnswerStone(x - 8, y + 6))
        self.answerstones.append(AnswerStone(x + 8, y + 6))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, *args):
        self.update_checkrect()
        self.check_player_shot()
        if self.check_player() and not self.fight:
            self.update_boss_walls()
            self.fight = True
        if not self.fight:
            return

    def update_boss_walls(self):
        if self.fight:
            for wall in boss_walls:
                wall.kill()
                all_sprites.add(wall)
        else:
            walls.add(boss_walls)

    def check_player_shot(self):
        for bullet in pygame.sprite.spritecollide(self, player_bullets, False):
            if bullet.is_alive():
                if isinstance(bullet, weapon.Bullet):
                    bullet.kill()
                if isinstance(bullet, weapon.Fist):
                    bullet.attacked = True
                self.hp -= bullet.damage
                if self.hp <= 0:
                    self.update_boss_walls()
                    self.fight = False
                    self.kill()


class AnswerStone(pygame.sprite.Sprite):
    image = specfunctions.load_image("bosses/answerstones/answer_stone.png")

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, boss_group)
        self.image = AnswerStone.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect)
