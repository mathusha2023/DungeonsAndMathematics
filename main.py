import pygame
import consts
import buttons
import specfunctions

pygame.init()

screen = pygame.display.set_mode(consts.SIZE)
pygame.display.set_caption(consts.TITLE)

menu_buttons = pygame.sprite.Group()

buttons.Button(menu_buttons, text="Играть!", x=consts.WIDTH // 2, y=300, f_size=40,
               press_event=lambda: print("PLAYING!"))
buttons.Button(menu_buttons, text="Рекорды", x=consts.WIDTH // 2, y=350, f_size=40,
               press_event=lambda: print("RECORDS!"))
buttons.Button(menu_buttons, text="Настройки", x=consts.WIDTH // 2, y=400, f_size=40,
               press_event=lambda: print("SETTINGS!"))
buttons.Button(menu_buttons, text="Выход", x=consts.WIDTH // 2, y=450, f_size=40,
               press_event=specfunctions.terminate)


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            specfunctions.terminate()
        menu_buttons.update(event)
    screen.fill((0, 0, 0))
    menu_buttons.draw(screen)
    pygame.display.flip()
    clock.tick(consts.FPS)
