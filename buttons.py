import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0), press_event=None):
        super().__init__(*groups)
        font1 = pygame.font.Font(font, f_size)
        font2 = pygame.font.Font(font, f_size + 6)
        self.text1 = font1.render(text, True, f_color)
        self.text2 = font2.render(text, True, f_active_color)
        self.center = (x, y)
        self.config_image(1)
        self.event = press_event

    def config_image(self, im):
        if im == 1:
            self.image = self.text1
        else:
            self.image = self.text2
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def update(self, *args):
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            self.config_image(2)
        else:
            self.config_image(1)
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    if self.event is not None:
                        self.event()


class RightButton(Button):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0), press_event=None):
        super().__init__(*groups, text=text, font=font, f_size=f_size, f_color=f_color, f_active_color=f_active_color,
                         press_event=press_event)
        self.rect.right = x
        self.rect.bottom = y
        self.center = self.rect.center
