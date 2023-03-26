import pygame
from settings import Palette, screen


pygame.init()
X = screen.get_width()
Y = screen.get_height()
font_base = pygame.font.Font('freesansbold.ttf', 35)
font_base_small = pygame.font.Font('freesansbold.ttf', 20)


def draw_text(
        text='your text',
        font=font_base,
        text_color=Palette.green,
        coords=(X // 2, Y // 2)
        ):

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(text, True, text_color)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (coords)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(text, textRect)


class MainMenu():
    # Fonts for text
    font_logo = pygame.font.Font('freesansbold.ttf', 70)
    font_buttons = pygame.font.Font('freesansbold.ttf', 35)

    # Buttons in main menu
    buttons = [
        ['Start',  (X // 2, Y // 2)],
        ['Quit', (X // 2, Y // 1.5)],
    ]

    @staticmethod
    def use_main_menu(pointer):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pygame.time.delay(100)
            pointer.move_pointer('UP')

        elif keys[pygame.K_s]:
            pygame.time.delay(100)
            pointer.move_pointer('DOWN')

        if keys[pygame.K_SPACE]:
            selected = pointer.buttons_available[pointer.current_position][0]
            if selected == "Start":
                pygame.time.delay(200)
                return 1
            elif selected == "Quit":
                return -1
        return 0

    def show(self):
        # Draw logo
        draw_text(
            'Algo game',
            self.font_logo,
            coords=(X // 2, Y // 4)
            )

        # Draw all buttons from list 'buttons'
        for i in range(len(self.buttons)):
            draw_text(
                self.buttons[i][0],
                self.font_buttons,
                coords=self.buttons[i][1]
            )


class MenuPointer():
    current_position = 0
    buttons_available = MainMenu.buttons

    def show(self):
        draw_text(
            '>>',
            pygame.font.Font('freesansbold.ttf', 30),
            Palette.green,
            (self.buttons_available[self.current_position][1][0] - X // 12,
             self.buttons_available[self.current_position][1][1],)
        )

    def move_pointer(self, direction):
        if direction == 'UP':
            if 0 != self.current_position:
                self.current_position -= 1
            else:
                self.current_position = len(self.buttons_available) - 1
        elif direction == 'DOWN':
            if len(self.buttons_available) - 1 != self.current_position:
                self.current_position += 1
            else:
                self.current_position = 0


class GameOverScreen():
    @staticmethod
    def show():
        start_time = int(pygame.time.get_ticks() / 1000)
        screen.fill('black')
        draw_text('Game over!')
        draw_text('Press any button to try again.', coords=(X // 2, Y // 1.5))
        draw_text('ESC to leave',
                  font=pygame.font.Font('freesansbold.ttf', 20),
                  coords=(X//2, Y/1.2))
        pygame.display.flip()
        pygame.time.wait(500)
        return start_time


class Etc():
    @staticmethod
    def display_score(start_time, destination):
        current_time = destination - int(pygame.time.get_ticks() / 1000)
        if start_time != 0:
            current_time += start_time
        score_surf = font_base.render(f'{current_time}', True, Palette.white)
        score_rect = score_surf.get_rect(center=(X//2, Y//4))
        screen.blit(score_surf, score_rect)
        return current_time
