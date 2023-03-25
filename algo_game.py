import pygame
from interface import MainMenu, MenuPointer, draw_text
from settings import screen, clock, Palette


pygame.init()
menu = MainMenu()
pointer = MenuPointer()
current_stage = 0
running = True
clock.tick(60)

screen.fill("white")
ground_surface = pygame.Surface((screen.get_width(), 100))
ground_surface.fill('green')
sky_surface = pygame.Surface((screen.get_width(), screen.get_height() - 100))
sky_surface.fill('blue')


def use_main_menu(event):
    if event.key == pygame.K_w:
        pointer.move_pointer('UP')

    elif event.key == pygame.K_s:
        pointer.move_pointer('DOWN')

    if event.key == pygame.K_RETURN:
        button_selected = pointer.buttons_available[pointer.current_position][0]
        if button_selected == "Start":
            return 1
        elif button_selected == "Quit":
            return -1
    return 0


while running:
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT or current_stage == -1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill("black")

    if current_stage == 0:
        menu.show()
        pointer.show()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                current_stage = use_main_menu(event)

    if current_stage == 1:
        screen.blit(ground_surface, (0, screen.get_height() - 100))
        screen.blit(sky_surface, (0, 0))
        draw_text('Next stage! Press ESC to leave.', text_color=Palette.white)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
