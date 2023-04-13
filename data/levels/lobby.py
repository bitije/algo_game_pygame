from pytmx.util_pygame import load_pygame
from data.settings import TILE_SIZE, X, Y, Palette
from data.characters import Inspector
import pygame
import pytmx

pygame.init()


class Lobby():
    """
    Load lobby tmx
    """
    def __init__(self) -> None:
        self.level_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.lobby_map = load_pygame('data/tmx/lobby.tmx')
        self.objects_done = []
        self.load_tmx_map()

    def load_player(self, x, y):
        collisions = self.collision_sprites
        self.player = Inspector((x, y), self.level_sprites, collisions)

    def load_tmx_map(self):
        for layer in self.lobby_map.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surface in layer.tiles():
                    pos = (x * TILE_SIZE, y * TILE_SIZE)
                    add_to = [self.level_sprites]
                    if ('Walls') == getattr(layer, 'name'):
                        add_to.append(self.collision_sprites)
                    elif ('Computers') == getattr(layer, 'name'):
                        add_to.append(self.collision_sprites)
                    Tile(pos, surface, add_to)
        if len(self.objects_done) > 0:
            coords = self.objects_done[-1]
            self.load_player(coords.x, coords.y)
        else:
            for obj in self.lobby_map.get_layer_by_name('Player'):
                if obj.name == 'Start':
                    self.load_player(obj.x, obj.y)

    def player_location(self):
        for layer in self.lobby_map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "Computers-OBJ":
                    for obj in layer:
                        computer = pygame.Rect(
                            obj.x, obj.y, obj.width, obj.height
                            )
                        if computer.colliderect(self.player.rect) is True:
                            if computer not in self.objects_done:
                                self.objects_done.append(computer)
                                return len(self.objects_done) + 2
                            else:
                                pass  # object is done
                            break

    def show(self, dt):
        self.level_sprites.custom_draw(self.player)
        self.level_sprites.update(dt)
        trigger = self.player_location()
        if trigger is not None:
            return trigger
        else:
            return 2


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        infl_w = self.rect.width * 0.2
        infl_h = self.rect.height * 0.2
        self.hitbox = self.rect.copy().inflate(infl_w, infl_h)


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.fake_screen = pygame.Surface((240, 160))
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - (X-666)
        self.offset.y = player.rect.centery - (Y-520)
        self.fake_screen.fill(Palette.grey_floor)
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.fake_screen.blit(sprite.image, offset_rect)
        self.display_surface.blit(pygame.transform.scale(self.fake_screen, (X, Y)), (0, 0))


if __name__ != '__main__':
    pass
