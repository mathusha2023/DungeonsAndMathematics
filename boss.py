import pygame
import random
import consts
import specfunctions
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
        self.qu_lvl_1 = [["2 + 2 = ", (1, 2, 3, 4), 3], ["2 + 2 = ", (2, 3, 4, 5), 2], ["2 + 2 = ", (4, 24, 34, 44), 0]]
        self.qu_lvl_2 = [["1 + 2 = ", (1, 2, 3, 4), 2], ["1 + 2 = ", (2, 3, 4, 5), 1], ["1 + 2 = ", (4, 3, 34, 44), 1]]
        self.qu_lvl_3 = [["2 + 2 = ", (1, 2, 3, 4), 3], ["2 + 2 = ", (2, 3, 4, 5), 2], ["2 + 2 = ", (4, 24, 34, 44), 0],
                         ["1 + 2 = ", (1, 2, 3, 4), 2]]
        self.cur_question = 1
        self.question = None
        self.right_answer = None
        self.font = pygame.font.Font(None, 36)
        self.ask_counter = 0
        self.damage = 2
        self.hp = 3
        self.damaged = False
        self.answered = None

    def update_checkrect(self):
        self.checking_rect.x = self.rect.x - self.checkrect_sizex // 2
        self.checking_rect.y = self.rect.y - self.checkrect_sizey // 2

    def check_player(self):
        return self.checking_rect.colliderect([i for i in player_group][0].rect)

    def spawn_answerstones(self, x, y):
        self.answerstones.append(AnswerStone(x - 8, y - 4, self))
        self.answerstones.append(AnswerStone(x + 8, y - 4, self))
        self.answerstones.append(AnswerStone(x - 8, y + 6, self))
        self.answerstones.append(AnswerStone(x + 8, y + 6, self))

    def draw(self, surface):
        for stone in self.answerstones:
            stone.draw_(surface)
        surface.blit(self.image, self.rect)
        if self.question:
            surface.blit(self.question, (self.rect.centerx - self.question.get_rect().width // 2,
                                         self.rect.y - self.question.get_rect().height - 10))
        if self.fight:
            self.draw_bossbar(surface)
            self.draw_timer(surface)

    def draw_bossbar(self, surface):
        pygame.draw.rect(consts.SCREEN, (155, 45, 48), (240, 630, 200 * self.hp, 40))
        pygame.draw.rect(consts.SCREEN, (0, 0, 0), (240 + 200 * self.hp, 630, (3 - self.hp) * 200, 40))
        txt = pygame.font.Font(None, 40).render("Синус: Посланник Математики",
                                                True, (255, 255, 255))
        surface.blit(txt, (consts.WIDTH // 2 - txt.get_rect().width // 2, 650 - txt.get_rect().height // 2))

    def draw_timer(self, surface):
        txt = pygame.font.Font(None, 38).render(f"Время на ответ: {self.ask_counter / consts.FPS:.2f}",
                                                True, (255, 255, 255))
        surface.blit(txt, (consts.WIDTH // 2 - txt.get_rect().width // 2, 600 - txt.get_rect().height // 2))

    def update(self, *args):
        self.update_checkrect()
        if not ((self.cur_question - 1) % 3 or self.damaged or self.cur_question == 1):
            self.get_damage()
            self.damaged = True
        if self.ask_counter:
            self.ask_counter -= 1
        if self.check_player() and not self.fight:
            self.update_boss_walls()
            self.fight = True
        if not self.fight:
            return
        if not self.ask_counter:
            if self.question and not self.answered:
                self.get_answer(-1)
            self.ask()
            self.ask_counter = 15 * consts.FPS

    def update_boss_walls(self):
        if self.fight:
            for wall in boss_walls:
                wall.kill()
                all_sprites.add(wall)
        else:
            walls.add(boss_walls)

    def ask(self):
        if self.cur_question < 4:
            q = self.qu_lvl_1.pop(random.randrange(len(self.qu_lvl_1)))
        elif 3 < self.cur_question < 7:
            q = self.qu_lvl_2.pop(random.randrange(len(self.qu_lvl_2)))
        elif self.cur_question > 6:
            q = self.qu_lvl_3.pop(random.randrange(len(self.qu_lvl_3)))
        q_text, variants, r_variant = q
        self.question = self.font.render(q_text, True, (255, 255, 255))
        self.right_answer = r_variant
        self.take_variants(variants)
        self.answered = False

    def take_variants(self, variants):
        for stone, variant in zip(self.answerstones, variants):
            stone.load_variant(variant)

    # вызывается камнем с вариантом ответа, в который выстрелил игрок
    def get_answer(self, stone):
        try:
            i = self.answerstones.index(stone)
        except ValueError:
            i = stone
        if i != self.right_answer:
            [i for i in player_group][0].get_damage(self.damage)
            self.damage += 2
        self.ask_counter = 0
        self.cur_question += 1
        self.damaged = False
        self.answered = True

    def get_damage(self):
        self.hp -= 1
        if self.hp <= 0:
            self.update_boss_walls()
            self.fight = False
            self.kill()

    def is_alive(self):
        return self.hp > 0


class AnswerStone(pygame.sprite.Sprite):
    image = specfunctions.load_image("bosses/answerstones/answer_stone.png")
    image_right = specfunctions.load_image("bosses/answerstones/answer_stone_right.png")
    image_wrong = specfunctions.load_image("bosses/answerstones/answer_stone_wrong.png")

    def __init__(self, pos_x, pos_y, boss):
        super().__init__(all_sprites, boss_group)
        self.image = AnswerStone.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.boss = boss
        self.variant = None
        self.font = pygame.font.Font(None, 34)

    def draw_(self, surface):
        surface.blit(self.image, self.rect)
        if self.variant:
            if self.rect.y < self.boss.rect.y:
                surface.blit(self.variant, (self.rect.centerx - self.variant.get_rect().width // 2,
                                            self.rect.bottom + 10))
            else:
                surface.blit(self.variant, (self.rect.centerx - self.variant.get_rect().width // 2,
                                            self.rect.y - self.variant.get_rect().height - 10))

    def draw(self, surface):
        if self.boss.is_alive():
            return
        surface.blit(self.image, self.rect)

    def load_variant(self, variant):
        self.variant = self.font.render(str(variant), True, (255, 255, 255))

    def check_player_shot(self):
        if pygame.sprite.spritecollideany(self, player_bullets) and self.variant:
            for bullet in player_bullets:
                bullet.kill()
            self.boss.get_answer(self)

    def update(self, *args):
        self.check_player_shot()
        if not self.boss.is_alive():
            self.variant = None
