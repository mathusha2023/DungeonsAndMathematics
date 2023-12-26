import pygame
import buttons
import specfunctions

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dungeons&Mathematics")

menu_buttons = pygame.sprite.Group()

buttons.Button(menu_buttons, text="Играть!", x=width // 2, y=300, f_size=40,
               press_event=lambda: print("PLAYING!"))
buttons.Button(menu_buttons, text="Рекорды", x=width // 2, y=350, f_size=40,
               press_event=lambda: print("RECORDS!"))
buttons.Button(menu_buttons, text="Настройки", x=width // 2, y=400, f_size=40,
               press_event=lambda: print("SETTINGS!"))
buttons.Button(menu_buttons, text="Выход", x=width // 2, y=450, f_size=40,
               press_event=specfunctions.terminate)

fps = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            specfunctions.terminate()
        menu_buttons.update(event)
    screen.fill((0, 0, 0))
    menu_buttons.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
