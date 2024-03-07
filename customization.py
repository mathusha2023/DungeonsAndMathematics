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


class SkinBoard(pygame.sprite.Sprite):
    def __init__(self, parent, skin_id, size, x, y, is_active, images, *groups):
        super().__init__(*groups)
        self.parent = parent
        self.id = skin_id
        self.size = size
        self.is_active = is_active
        self.images = images
        self.im = 0
        self.counter = consts.FPS // 5
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.update_image()

    def is_focused(self):
        return self.rect.collidepoint(*pygame.mouse.get_pos())

    def update_image(self):
        self.image.fill((0, 0, 0))
        if self.is_active:
            self.image.fill((255, 255, 0), (0, 0, 3, self.rect.height))
            self.image.fill((255, 255, 0), (0, 0, self.rect.width, 3))
            self.image.fill((255, 255, 0), (0, self.rect.height - 3, self.rect.width, 3))
            self.image.fill((255, 255, 0), (self.rect.width - 3, 0, 3, self.rect.height))
        img = self.images[self.im]
        self.image.blit(img, (
            (self.rect.width - img.get_rect().width) // 2, (self.rect.height - img.get_rect().height) // 2))

    def update(self, *args):
        self.update_image()
        if self.is_focused() or self.is_active:
            self.counter -= 1
            if not self.counter:
                self.im = (self.im + 1) % len(self.images)
                self.counter = consts.FPS // 5
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    self.parent.activate_skin(self)


class SkinsPlace:
    def __init__(self, parent, skins, active_skin, cell_size=(100, 100)):
        self.parent = parent
        self.cell_size = cell_size
        self.n_x = (consts.WIDTH - 50) // cell_size[0]
        self.n_y = 400 // cell_size[1]
        self.skinboards = []
        self.group = pygame.sprite.Group()
        self.create_skins(skins, active_skin)

    def create_skins(self, skins, active_skin):
        for y in range(self.n_y):
            for x in range(self.n_x):
                try:
                    a = y * self.n_x + x == active_skin
                    self.skinboards.append(SkinBoard(self, y * self.n_x + x, self.cell_size,
                                                     25 + self.cell_size[0] * x, 200 + self.cell_size[1] * y, a,
                                                     skins.pop(0), self.group))
                except IndexError:
                    return

    def activate_skin(self, skin):
        for s in self.skinboards:
            s.is_active = False
        skin.is_active = True
        settings.character_skin = skin.id

    def draw(self, surface):
        self.group.draw(surface)

    def update(self, *args):
        self.group.update(*args)


class SkinsMenu:
    def __init__(self, *groups):
        self.create_headers(*groups)
        self.create_skins()

    def create_headers(self, *groups):
        self.character_header = Header(self, 25, Localisation.character(), True, *groups)
        self.weapons_header = Header(self, consts.WIDTH // 4 + 25, Localisation.weapon(), False, *groups)
        self.bosses_header = Header(self, consts.WIDTH // 2 + 25, Localisation.bosses(), False, *groups)
        self.dungeon_header = Header(self, 3 * consts.WIDTH // 4 + 25, Localisation.dungeon(), False, *groups)
        self.headers = [self.character_header, self.weapons_header, self.bosses_header, self.dungeon_header]

    def create_skins(self):
        c = [[specfunctions.load_image("ura/default/ura_right_go1.png"),
              specfunctions.load_image("ura/default/ura_right_go2.png")],
             [specfunctions.load_image("ura/evil/ura_right_go1.png"),
              specfunctions.load_image("ura/evil/ura_right_go2.png")]]
        self.character_place = SkinsPlace(self, c, settings.character_skin)
        self.weapons_place = SkinsPlace(self, [], 0)
        self.bosses_place = SkinsPlace(self, [], 0)
        self.dungeon_place = SkinsPlace(self, [], 0)
        self.places = self.character_place, self.weapons_place, self.bosses_place, self.dungeon_place

    def activate_header(self, header):
        for h in self.headers:
            h.is_active = False
        header.is_active = True

    def draw_skins(self, surface):
        for i in range(len(self.headers)):
            if self.headers[i].is_active:
                self.places[i].draw(surface)

    def update(self, *args):
        for p in self.places:
            p.update(*args)


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
            menu.update(event)
        menu.update()
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        menu.draw_skins(consts.SCREEN)
        if button.clicked:
            return
        pygame.display.flip()
        clock.tick(consts.FPS)
