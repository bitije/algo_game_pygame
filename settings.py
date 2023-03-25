from dataclasses import dataclass
import os
import pygame


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


@dataclass
class Palette():
    # define the RGB value for colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    green = (127, 255, 0)
