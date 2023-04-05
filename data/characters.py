from data.spritesheet import get_frames
import pygame

pygame.init()


class Inspector(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites) -> None:
        super().__init__(group)

        # Animation attributes
        path = 'data/imgs/assets/inspector_spritesheet.png'
        self.frames = get_frames(path, rows=4, columns=4)
        self.anim_index = 0
        self.frame_index = 0
        self.entity_movement = False

        # Basic attributes
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Movement attributes
        self.direction_move = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 70

        # Collision attributes
        self.collision_sprites = collision_sprites
        self.hitbox = self.rect.copy().inflate(-5, -5)

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):

                    if direction == 'horizontal':
                        if self.direction_move.x > 0:  # Moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction_move.x < 0:  # Moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction_move.y > 0:  # Moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction_move.y < 0:  # Moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def move(self, dt):

        # Normalizing vector
        if self.direction_move.magnitude() > 0:
            self.direction_move = self.direction_move.normalize()

        # Horizontal vector
        self.pos.x += self.direction_move.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # Vertical vector
        self.pos.y += self.direction_move.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def player_input(self):
        keys = pygame.key.get_pressed()
        self.entity_movement = False
        self.anim_index = 0
        self.direction_move.x = 0
        self.direction_move.y = 0
        if keys[pygame.K_w]:
            self.direction_move.y = -1
            self.anim_index = 1
            self.entity_movement = True
        elif keys[pygame.K_s]:
            self.direction_move.y = 1
            self.entity_movement = True
        elif keys[pygame.K_d]:
            self.direction_move.x = 1
            self.anim_index = 3
            self.entity_movement = True
        elif keys[pygame.K_a]:
            self.direction_move.x = -1
            self.anim_index = 2
            self.entity_movement = True

    def apply_animation(self):
        if self.entity_movement is True:
            if round(self.frame_index) >= 4:
                self.frame_index = 0
            else:
                self.frame_index += 0.2
        self.image = self.frames[int(self.frame_index) + self.anim_index * 4]

    def update(self, dt):
        self.player_input()
        self.move(dt)
        self.apply_animation()


if __name__ != '__main__':
    pass
