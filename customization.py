import pygame
import consts
import buttons
import specfunctions
from settings import settings
from localisation import Localisation


class Header(pygame.sprite.Sprite):
    def __init__(self, parent, x, text, is_active, *groups):
        super().__init__(*groups)
        self.parent = parent
        inactive_text = pygame.font.Font(None, 42).render(text, True, (255, 255, 255))
        active_text = pygame.font.Font(None, 42).render(text, True, (0, 0, 0))
        self.inactive_image = pygame.Surface(((consts.WIDTH - 200) // 4, 60))
        self.inactive_image.blit(inactive_text,
                                 (self.inactive_image.get_rect().width // 2 - inactive_text.get_rect().width // 2,
                                  (self.inactive_image.get_rect().height - inactive_text.get_rect().height) // 2))
        self.active_image = pygame.Surface(((consts.WIDTH - 200) // 4, 60))
        self.active_image.fill((255, 255, 0))
        self.active_image.blit(active_text,
                               (self.active_image.get_rect().width // 2 - active_text.get_rect().width // 2,
                                (self.active_image.get_rect().height - active_text.get_rect().height) // 2))
        self.is_active = is_active
        self.image = None
        self.config_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 50

    def config_image(self):
        if self.is_active:
            self.image = self.active_image
        else:
            self.image = self.inactive_image

    def update(self, *args):
        self.config_image()
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    self.parent.activate_header(self)


class SkinsPlace(pygame.sprite.Sprite):
    def __init__(self, parent, *groups):
        super().__init__(*groups)
        self.parent = parent



class SkinsMenu(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.create_headers(*groups)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)

    def create_headers(self, *groups):
        self.character_header = Header(self, 25, Localisation.character(), True, *groups)
        self.weapons_header = Header(self, consts.WIDTH // 4 + 25, Localisation.weapon(), False, *groups)
        self.bosses_header = Header(self, consts.WIDTH // 2 + 25, Localisation.bosses(), False, *groups)
        self.dungeon_header = Header(self, 3 * consts.WIDTH // 4 + 25, Localisation.dungeon(), False, *groups)
        self.headers = [self.character_header, self.weapons_header, self.bosses_header, self.dungeon_header]

    def activate_header(self, header):
        for h in self.headers:
            h.is_active = False
        header.is_active = True


def customization_menu():
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    menu = SkinsMenu(all_sprites)
    button = buttons.EscapeButton(all_sprites, text=Localisation.back(), x=consts.WIDTH // 2, y=650, f_size=45)

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
