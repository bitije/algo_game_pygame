import pygame
from settings import Palette, screen


pygame.init()
X = screen.get_width()
Y = screen.get_height()


def draw_text(text, font, text_color, coords):
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


class MenuPointer():
    current_position = (X // 2.5, Y // 2)
    buttons_available = []
    where = "UP"

    def show(self):
        draw_text(
            '>>>',
            pygame.font.Font('freesansbold.ttf', 30),
            Palette.red,
            self.current_position
        )

    def move_pointer(self, where):
        if where == 'UP':
            self.current_position = (X // 2.5, Y // 2)
            self.where = "UP"
            self.show()
        elif where == 'DOWN':
            self.current_position = (X // 2.5, Y // 1.5)
            self.where = "DOWN"
            self.show()


class Menus():
    font_logo = pygame.font.Font('freesansbold.ttf', 70)
    font_buttons = pygame.font.Font('freesansbold.ttf', 35)

    def show_main(self):
        # set the pygame window name
        pygame.display.set_caption('Main menu')

        draw_text(
            'Algo game',
            self.font_logo,
            Palette.black,
            (X // 2, Y // 4)
            )

        draw_text(
            'Start',
            self.font_buttons,
            Palette.black,
            (X // 2, Y // 2)
        )

        draw_text(
            'Quit',
            self.font_buttons,
            Palette.black,
            (X // 2, Y // 1.5)
        )
