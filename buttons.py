import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0), press_event=None):
        super().__init__(*groups)
        self.font1 = pygame.font.Font(font, f_size)
        self.font2 = pygame.font.Font(font, f_size + 6)
        self.f_color = f_color
        self.f_active_color = f_active_color
        self.text1 = self.font1.render(text, True, f_color)
        self.text2 = self.font2.render(text, True, f_active_color)
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

    def is_focused(self):
        return self.rect.collidepoint(*pygame.mouse.get_pos())

    def update(self, *args):
        if self.is_focused():
            self.config_image(2)
        else:
            self.config_image(1)
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    if self.event is not None:
                        self.event()
                        self.config_image(1)

    def set_text(self, text):
        self.text1 = self.font1.render(text, True, self.f_color)
        self.text2 = self.font2.render(text, True, self.f_active_color)


class RightButton(Button):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0), press_event=None):
        self.right = x
        self.bottom = y
        super().__init__(*groups, text=text, font=font, f_size=f_size, f_color=f_color,
                         f_active_color=f_active_color, press_event=press_event)

    def config_image(self, im):
        super().config_image(im)
        if im == 1:
            self.rect.bottomright = (self.right, self.bottom)
        else:
            self.rect.bottomright = (self.right + 9, self.bottom + 1)


class EscapeButton(Button):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0)):
        super().__init__(*groups, text=text, x=x, y=y,
                         font=font, f_size=f_size, f_color=f_color, f_active_color=f_active_color)
        self.clicked = False

    def update(self, *args):
        if self.is_focused():
            self.config_image(2)
        else:
            self.config_image(1)
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    self.clicked = True


class EscapeEventButton(Button):
    def __init__(self, *groups, text="Button", x=0, y=0,
                 font=None, f_size=24, f_color=(255, 255, 255), f_active_color=(255, 255, 0), press_event=None):
        super().__init__(*groups, text=text, x=x, y=y, font=font, f_size=f_size, f_color=f_color,
                         f_active_color=f_active_color, press_event=press_event)
        self.escape = False

    def update(self, *args):
        if self.is_focused():
            self.config_image(2)
        else:
            self.config_image(1)
        if args:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(*event.pos):
                    if self.event is not None:
                        self.escape = self.event()
                        self.config_image(1)


class RightEscapeEventButton(EscapeEventButton, RightButton):
    pass
