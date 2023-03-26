from settings import X, Y, screen
import pygame
from interface import Etc


def collision_sprites(player_runner, bubble_group):
    if pygame.sprite.spritecollide(player_runner.sprite, bubble_group, False):
        bubble_group.empty()
        return -2
    else:
        return 1


class LevelOne():
    def __init__(self) -> None:
        self.player_runner = pygame.sprite.GroupSingle()
        self.player_runner.add(PlayerRunner())
        self.bubble_group = pygame.sprite.Group()

        self.ground_surf = pygame.Surface((X, 100))
        self.ground_surf.fill('green')
        self.sky_surf = pygame.Surface((X, Y - 100))
        self.sky_surf.fill('blue')

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
        self.bubble_group.add(BubbleEnemy(entity))


class BubbleEnemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'flying':
            self.image = pygame.Surface((50, 50))
            self.rect = self.image.get_rect(midbottom=(X + 100, Y - 200))
            self.image.fill('yellow')
        else:
            self.image = pygame.Surface((50, 50))
            self.rect = self.image.get_rect(midbottom=(X + 100, Y - 100))
            self.image.fill('pink')

    def update(self):
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill


class PlayerRunner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 150))
        self.image.fill('red')
        self.rect = self.image.get_rect(midbottom=(60, Y - 100))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= Y - 100:
            self.gravity = -20

        if keys[pygame.K_s] and self.rect.bottom == Y - 100:
            self.image = pygame.Surface((100, 80))
            self.image.fill('red')
            self.rect = self.image.get_rect(midbottom=(120, Y - 100))

        if not keys[pygame.K_s] and self.rect.bottom == Y - 100:
            self.image = pygame.Surface((50, 150))
            self.image.fill('red')
            self.rect = self.image.get_rect(midbottom=(120, Y - 100))

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= Y - 100:
            self.gravity = 0
            self.rect.bottom = Y - 100

    def update(self):
        self.player_input()
        self.apply_gravity()


if __name__ != '__main__':
    level_one = LevelOne()
