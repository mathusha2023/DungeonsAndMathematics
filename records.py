import pygame
import consts
import db
import specfunctions
import buttons
from localisation import Localisation


class Record(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((601, 551))
        self.rect = self.image.get_rect()
        self.rect.centerx = consts.WIDTH // 2
        self.rect.y = 50
        self.draw_lines()
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 30)
        self.draw_records()

    def draw_lines(self):
        for y in range(0, 551, 55):
            pygame.draw.line(self.image, (255, 255, 255), (0, y), (600, y))
        for x in range(0, 601, 200):
            pygame.draw.line(self.image, (255, 255, 255), (x, 0), (x, 550))

    def draw_records(self):
        txt1 = self.title_font.render(Localisation.weapon(), True, (255, 255, 255))
        self.image.blit(txt1, (100 - txt1.get_rect().width // 2,
                               27 - txt1.get_rect().height // 2))

        txt2 = self.title_font.render(Localisation.time(), True, (255, 255, 255))
        self.image.blit(txt2, (300 - txt2.get_rect().width // 2,
                               27 - txt2.get_rect().height // 2))

        txt3 = self.title_font.render(Localisation.date(), True, (255, 255, 255))
        self.image.blit(txt3, (500 - txt3.get_rect().width // 2,
                               27 - txt3.get_rect().height // 2))

        i = 55
        for weapon, result, date in db.get_records():
            self.draw_weapon(weapon, i)
            res_txt = self.font.render(result, True, (255, 255, 255))
            self.image.blit(res_txt, (300 - res_txt.get_rect().width // 2,
                                      i + 27 - res_txt.get_rect().height // 2))

            date_txt = self.font.render(date, True, (255, 255, 255))
            self.image.blit(date_txt, (500 - date_txt.get_rect().width // 2,
                                       i + 27 - date_txt.get_rect().height // 2))

            i += 55

    def draw_weapon(self, weapon, y):
        if weapon:
            im = specfunctions.load_image(f"weapons/weapon{weapon}_right.png")
        else:
            im = specfunctions.load_image(f"weapons/records_fist.png")
        self.image.blit(im, (100 - im.get_rect().width // 2,
                             y + 27 - im.get_rect().height // 2))


def records_menu():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    button = buttons.EscapeButton(all_sprites, text=Localisation.back(), x=consts.WIDTH // 2, y=650, f_size=45)
    Record(all_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            all_sprites.update(event)
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        if button.clicked:
            return
        pygame.display.flip()
        clock.tick(consts.FPS)
