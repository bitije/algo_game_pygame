from pytmx.util_pygame import load_pygame
from data.settings import screen, TILE_SIZE
from data.characters import Inspector
import pygame


pygame.init()


class Lobby():
    """
    Load lobby tmx
    """
    def __init__(self) -> None:
        self.the_map = pygame.sprite.Group()
        lobby_map = load_pygame('data/tmx/lobby.tmx')
        for layer in lobby_map.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surface in layer.tiles():
                    pos = (x * TILE_SIZE, y * TILE_SIZE)
                    Tile(pos, surface, self.the_map)

    def show(self):
        self.the_map.draw(screen)
        inspector.draw(screen)
        inspector.update()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


if __name__ != '__main__':
    inspector = pygame.sprite.GroupSingle()
    inspector.add(Inspector())
