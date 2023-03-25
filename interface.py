import pygame
from settings import Palette, screen


pygame.init()
X = screen.get_width()
Y = screen.get_height()


def draw_text(
        text='your text',
        font=pygame.font.Font('freesansbold.ttf', 35),
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
        # ['zxc', (X // 2, Y // 3)]
    ]

    def show(self):
        # set the pygame window name
        pygame.display.set_caption('Main menu')

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


if __name__ != "__main__":
    pointer = MenuPointer()
