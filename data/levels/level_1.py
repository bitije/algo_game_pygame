from data.settings import X, Y, screen
import pygame
from data.interface import Etc
from data.spritesheet import SpriteSheet
from data.settings import Palette


def collision_sprites(player_runner, bubble_group):
    if pygame.sprite.spritecollide(player_runner.sprite, bubble_group, False):
        bubble_group.empty()
        return -2
    else:
        return 1


class LevelOne():
    def __init__(self) -> None:

        path_to_inspector = 'data/imgs/assets/inspector_spritesheet.png'
        path_to_alien = 'data/imgs/assets/inmate_1_spritesheet.png'
        path_to_junk = 'data/imgs/assets/doodads_spritesheet.png'
        inspector = SpriteSheet(path_to_inspector)
        alien = SpriteSheet(path_to_alien)
        junk = SpriteSheet(path_to_junk)

        # Tuple of frames
        coords_junk = (32, 48, 16, 16)
        coords_inspector = [
            (0, 48, 16, 16),
            (16, 48, 16, 16),
            (32, 48, 16, 16),
            (48, 48, 16, 16)
            ]
        coords_alien = [
            (0, 0, 16, 16),
            (16, 0, 16, 16),
            (32, 0, 16, 16)
        ]

        frames_player = inspector.images_at(coords_inspector, (50, 150), Palette.blue)
        self.frames_alien = alien.images_at(coords_alien, (50, 50), Palette.blue)
        self.frame_junk = junk.image_at(coords_junk, (80, 80), Palette.blue)

        self.player_runner = pygame.sprite.GroupSingle()
        self.player_runner.add(PlayerRunner(frames_player))
        self.bubble_group = pygame.sprite.Group()

        self.ground_surf = pygame.Surface((X, 100)).convert()
        self.ground_surf.fill(Palette.grey_floor)
        self.sky_surf = pygame.Surface((X, Y - 100)).convert()
        self.sky_surf.fill(Palette.grey_wall)

    def show(self, start_time):
        screen.blit(self.ground_surf, (0, Y - 100))
        screen.blit(self.sky_surf, (0, 0))

        self.player_runner.draw(screen)
        self.player_runner.update()

        self.bubble_group.draw(screen)
        self.bubble_group.update()

        total_score = Etc().display_score(start_time, 30)

        if total_score == 0:
            return 2
        else:
            return collision_sprites(self.player_runner, self.bubble_group)

    def tick(self, entity):
        if entity == 'flying':
            frames = self.frames_alien
        else:
            frames = self.frame_junk
        self.bubble_group.add(BubbleEnemy(entity, frames))


class BubbleEnemy(pygame.sprite.Sprite):
    def __init__(self, type, frames):
        super().__init__()

        if type == 'flying':
            self.frames = frames
            self.player_index = 0
            self.image = self.frames[self.player_index]
            self.rect = self.image.get_rect(midbottom=(X + 100, Y - 200))
        else:
            self.image = frames
            self.rect = self.image.get_rect(midbottom=(X + 100, Y - 100))

    def apply_animation(self):
        if self.player_index >= len(self.frames) - 1:
            self.player_index = 0
        else:
            self.player_index += 1

        self.image = self.frames[int(self.player_index)]

    def update(self):
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill


class PlayerRunner(pygame.sprite.Sprite):
    def __init__(self, frames_of_running):
        super().__init__()
        self.frames_of_running = frames_of_running
        self.player_index = 0
        self.image = self.frames_of_running[self.player_index]
        self.rect = self.image.get_rect(midbottom=(60, Y - 100))
        self.gravity = 0
        self.crouch = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= Y - 100:
            self.crouch = -1
            self.gravity = -20

        elif keys[pygame.K_s] and self.rect.bottom == Y - 100:
            self.crouch = 1

        elif not keys[pygame.K_s] and self.rect.bottom == Y - 100:
            self.crouch = 0

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= Y - 100:
            self.gravity = 0
            self.rect.bottom = Y - 100

    def apply_animation(self):
        if self.player_index >= len(self.frames_of_running) - 1:
            self.player_index = 0
        else:
            self.player_index += 0.2

        self.image = self.frames_of_running[int(self.player_index)]

        if self.crouch == 1:
            self.image = pygame.transform.scale(self.image, (60, 80))
            self.rect = self.image.get_rect(midbottom=(60, Y - 100))
        elif self.crouch == 0:
            self.image = pygame.transform.scale(self.image, (50, 150))
            self.rect = self.image.get_rect(midbottom=(60, Y - 100))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.apply_animation()


if __name__ != '__main__':
    level_one = LevelOne()
