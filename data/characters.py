from data.spritesheet import get_frames
import pygame

pygame.init()


class Inspector(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        path = 'data/imgs/assets/inspector_spritesheet.png'
        self.frames = get_frames(path, rows=4, columns=4, scale=(100, 100))
        self.direction = 0
        self.frame_index = 0
        self.entity_movement = False
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def player_input(self):
        keys = pygame.key.get_pressed()
        self.entity_movement = False
        self.direction = 0
        if keys[pygame.K_w]:
            self.direction = 1
            self.entity_movement = True
        elif keys[pygame.K_d]:
            self.direction = 3
            self.entity_movement = True
        elif keys[pygame.K_a]:
            self.direction = 2
            self.entity_movement = True
        elif keys[pygame.K_s]:
            self.entity_movement = True

    def apply_animation(self):
        if self.entity_movement is True:
            if round(self.frame_index) >= 4:
                self.frame_index = 0
            else:
                self.frame_index += 0.1
        else:
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index) + self.direction * 4]

    def update(self):
        self.player_input()
        self.apply_animation()


if __name__ != '__main__':
    pass
