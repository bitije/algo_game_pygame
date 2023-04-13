from data.settings import screen
from data.interface import draw_text
import pygame

pygame.init()


def start_selectionsort(debug_next, current_stage):
    screen.fill('black')
    draw_text('Selection sort')
    return current_stage
