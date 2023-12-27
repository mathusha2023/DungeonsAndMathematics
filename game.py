import pygame
import consts
import specfunctions


class Player(pygame.sprite.Sprite):
    left_st_im = specfunctions.load_image("ura_left_st.png")
    left_go1_im = specfunctions.load_image("ura_left_go1.png")
    left_go2_im = specfunctions.load_image("ura_left_go2.png")
    right_st_im = specfunctions.load_image("ura_right_st.png")
    right_go1_im = specfunctions.load_image("ura_right_go1.png")
    right_go2_im = specfunctions.load_image("ura_right_go2.png")

    right = 0
    left = 1

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Player.right_st_im
        self.rect = self.image.get_rect()
        self.left_ims = [Player.left_go1_im, Player.left_go2_im]
        self.right_ims = [Player.right_go1_im, Player.right_go2_im]
        self.im = 0
        self.counter = 0
        self.state = Player.right
        self.speed = 5

    def update(self, *args):
        pressed_keys = pygame.key.get_pressed()
        if any([pressed_keys[pygame.K_a], pressed_keys[pygame.K_d],
                pressed_keys[pygame.K_w], pressed_keys[pygame.K_s]]):
            if pressed_keys[pygame.K_a]:
                self.image = self.left_ims[self.im]
                self.state = Player.left
                self.rect.x -= self.speed
            elif pressed_keys[pygame.K_d]:
                self.image = self.right_ims[self.im]
                self.state = Player.right
                self.rect.x += self.speed
            if pressed_keys[pygame.K_w]:
                self.image = self.left_ims[self.im] if self.state == Player.left else self.right_ims[self.im]
                self.rect.y -= self.speed
            elif pressed_keys[pygame.K_s]:
                self.image = self.left_ims[self.im] if self.state == Player.left else self.right_ims[self.im]
                self.rect.y += self.speed
            self.counter += 1
            if not self.counter % 5:
                self.im = 1 - self.im
                self.counter = 0
        else:
            self.image = Player.left_st_im if self.state == Player.left else Player.right_st_im


def start_game(clock):
    all_sprites = pygame.sprite.Group()
    Player(all_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(consts.FPS)
