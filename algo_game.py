import pygame
from interface import MainMenu, MenuPointer, draw_text, GameOverScreen
from settings import screen, clock
from random import choice
from levels.level_1 import LevelOne


pygame.init()
menu = MainMenu()
pointer = MenuPointer()
level_one = LevelOne()

# Timer
runner_timer = pygame.USEREVENT + 1
pygame.time.set_timer(runner_timer, 1000)

current_stage = 0
running = True
start_time = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT or current_stage == -1:
            running = False

        # Where to go from game over screen
        elif event.type == pygame.KEYDOWN and current_stage == -2:
            if event.key == pygame.K_ESCAPE:
                current_stage = 0
            else:
                current_stage = 1

        # Every second generate bubble on 1st level
        if event.type == runner_timer and current_stage == 1:
            level_one.tick(choice(['flying', 'sneaky', 'sneaky']))

    # Show Main Menu
    if current_stage == 0:
        clock.tick(15)
        screen.fill("black")
        menu.show()
        pointer.show()
        current_stage = menu.use_main_menu(pointer)
        if current_stage == 1:
            start_time = int(pygame.time.get_ticks() / 1000)

    # Show 1st level
    if current_stage == 1:
        current_stage = level_one.show(start_time)

    if current_stage == 2:
        screen.fill('black')
        draw_text('Second level is not done yet :)')
        pygame.display.flip()
        pygame.time.wait(2000)
        current_stage = -2

    # Show game over screen
    elif current_stage == -2:
        start_time = GameOverScreen().show()

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
