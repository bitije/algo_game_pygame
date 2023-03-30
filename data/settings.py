from dataclasses import dataclass
import pygame


# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TILE_SIZE = 16

# Screen set up
screen = pygame.display.set_mode((800, 600))
X = screen.get_width()
Y = screen.get_height()

# Clock
clock = pygame.time.Clock()

# Window icon and caption
pygame.display.set_caption('Algo game')
Icon = pygame.image.load('data/imgs/icon.png')
pygame.display.set_icon(Icon)


# Dataclass for RGB codes used in game
@dataclass
class Palette():
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    green = (127, 255, 0)
    grey_wall = (77, 85, 89)
    grey_floor = (155, 173, 183)
