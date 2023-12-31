import pygame
import consts
import specfunctions

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    left_st_im = specfunctions.load_image("ura_left_st.png")
    left_go1_im = specfunctions.load_image("ura_left_go1.png")
    left_go2_im = specfunctions.load_image("ura_left_go2.png")
    right_st_im = specfunctions.load_image("ura_right_st.png")
    right_go1_im = specfunctions.load_image("ura_right_go1.png")
    right_go2_im = specfunctions.load_image("ura_right_go2.png")

    right = 0
    left = 1

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player_group)
        self.image = Player.right_st_im
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.left_ims = [Player.left_go1_im, Player.left_go2_im]
        self.right_ims = [Player.right_go1_im, Player.right_go2_im]
        self.im = 0
        self.counter = 0
        self.state = Player.right
        self.speed = 5
        # self.speed = 100

    def update(self, *args):
        pressed_keys = pygame.key.get_pressed()
        if any([pressed_keys[pygame.K_a], pressed_keys[pygame.K_d],
                pressed_keys[pygame.K_w], pressed_keys[pygame.K_s]]):
            self.prev_x = self.rect.x
            self.prev_y = self.rect.y
            if pressed_keys[pygame.K_a]:
                self.image = self.left_ims[self.im]
                self.state = Player.left
                self.rect.x -= self.speed
            elif pressed_keys[pygame.K_d]:
                self.image = self.right_ims[self.im]
                self.state = Player.right
                self.rect.x += self.speed
            self.stop_wall_moving()
            self.prev_x = self.rect.x
            if pressed_keys[pygame.K_w]:
                self.image = self.left_ims[self.im] if self.state == Player.left else self.right_ims[self.im]
                self.rect.y -= self.speed
            elif pressed_keys[pygame.K_s]:
                self.image = self.left_ims[self.im] if self.state == Player.left else self.right_ims[self.im]
                self.rect.y += self.speed
            self.stop_wall_moving()
            self.counter += 1
            if not self.counter % 5:
                self.im = 1 - self.im
                self.counter = 0
        else:
            self.image = Player.left_st_im if self.state == Player.left else Player.right_st_im

    def stop_wall_moving(self):
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x = self.prev_x
            self.rect.y = self.prev_y


class TileImages:
    wall = specfunctions.load_image("wall.png")
    floor = specfunctions.load_image("floor.png")


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_im, pos_x, pos_y, *groups):
        super().__init__(all_sprites, *groups)
        self.image = tile_im
        self.rect = self.image.get_rect().move(
            consts.TILE_WIDTH * pos_x, consts.TILE_HEIGHT * pos_y)


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.frames = []
        self.cur_frame = 0
        self.add_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * consts.TILE_WIDTH
        self.rect.y = pos_y * consts.TILE_HEIGHT
        self.counter = 0

    def add_frames(self):
        for i in range(1, 25):
            self.frames.append(specfunctions.load_image(f"portals/portal{i}.png"))

    def update(self, *args):
        self.counter += 1
        if not self.counter % 3:
            self.image = self.frames[self.cur_frame]
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.counter = 0


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - consts.WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - consts.HEIGHT // 2)


def load_level(filename):
    filename = "data/maps/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile(TileImages.floor, x, y)
            elif level[y][x] == '|':
                Tile(TileImages.wall, x, y, walls)
            elif level[y][x] == "#":
                Portal(x, y)
            elif level[y][x] == '@':
                Tile(TileImages.floor, x, y)
                new_player = Player(x, y)
    return new_player, x, y


def empty_groups():
    all_sprites.empty()
    walls.empty()
    player_group.empty()


def apply_all(camera):
    for sprite in all_sprites:
        camera.apply(sprite)


def start_game(clock):
    empty_groups()
    player, level_x, level_y = generate_level(load_level('map1.txt'))
    camera = Camera()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                specfunctions.terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        consts.SCREEN.fill((0, 0, 0))
        all_sprites.draw(consts.SCREEN)
        player_group.draw(consts.SCREEN)
        all_sprites.update()
        camera.update(player)
        apply_all(camera)
        pygame.display.flip()
        clock.tick(consts.FPS)
