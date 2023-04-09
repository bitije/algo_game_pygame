import pygame

from random import choice

from data.settings import clock
from data.interface import MainMenu, MenuPointer, Etc
from data.levels.runner import RunnerLevel
from data.levels.lobby import Lobby
from data.algorithms import bubble_sort


pygame.init()

menu = MainMenu()
pointer = MenuPointer()
runner = RunnerLevel()
lobby = Lobby()

current_stage = 3
running = True
start_time = 0

# Timer
runner_timer = pygame.USEREVENT + 1
pygame.time.set_timer(runner_timer, 1000)

# Delta time
FPS_LOCK = 60
dt = clock.tick(FPS_LOCK) / 1000

debug_next = False

while running:
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

        # Every second generate enemy on runner
        if event.type == runner_timer and current_stage == 1:
            runner.tick(choice(['flying', 'sneaky', 'sneaky']))

        elif current_stage >= 3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    debug_next = True
            else:
                continue

    # Main Menu
    if current_stage == 0:
        clock.tick(15)
        current_stage = menu.use_main_menu(pointer)

    # Runner mini game
    elif current_stage == 1:
        current_stage = runner.show(start_time, dt)

    # Lobby
    elif current_stage == 2:
        current_stage = lobby.show(dt)
        if current_stage == 1:
            start_time = int(pygame.time.get_ticks() / 1000)

    # Algorithms
    elif current_stage >= 3:
        algo_levels = [
            # 1,
            bubble_sort.start_bubblesort(debug_next), -228
        ]
        current_stage = algo_levels[current_stage - 3]
        debug_next = False
        if current_stage == 1:
            start_time = int(pygame.time.get_ticks() / 1000)

    # Game over
    elif current_stage == -2:
        start_time = Etc().game_over()

    # Not done screen
    elif current_stage == -228:
        current_stage = Etc().not_done()

    dt = clock.tick(FPS_LOCK) / 1000

    # Put work on screen
    pygame.display.flip()

pygame.quit()
