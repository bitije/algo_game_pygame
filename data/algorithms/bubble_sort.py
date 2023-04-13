from data.settings import screen, Palette, X, Y
from data.interface import draw_text, font_base_small
import pygame


pygame.init()


class ArrElement(pygame.sprite.Sprite):
    """ Sprite of array element """

    def __init__(self, pos, element, group) -> None:
        super().__init__()
        self.pos = pos
        self.element = element
        self.image = pygame.Surface((40, 30 + element*2))
        self.image.fill(Palette.white)
        self.rect = self.image.get_rect(midbottom=pos)
        self.add(group)

    def color(self, color=None):
        """ Fill sprite with color text etc """

        # If color is not defined dont change it
        if color is not None:
            self.image.fill(color)

        # Text attributes
        font = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = font.render(f'{self.element}', 1, Palette.black)
        screen.blit(textSurf, (self.pos[0]-10, self.pos[1]-20))


class BubbleSort():
    """ Algorithm class """

    def __init__(self, elements) -> None:
        self.elements = elements
        self.sort_res = False
        self.reset()
        self.create_arr(self.elements)

    def reset(self):
        """ Reset all flags """
        self.inner_flag = 0
        self.outer_flag = 0
        self.swapped = False
        self.exit_flag = False

    def create_arr(self, elements):
        """ Create sprites from array """

        self.arr_elements = pygame.sprite.OrderedUpdates()

        # Create sprite for every array element and add it to group
        for element in range(len(elements)):
            x, y = 50 + 50 * element, 250
            ArrElement((x+150, y), elements[element], self.arr_elements)

        # Fill sprites with content
        for n in range(len(self.elements)-1, -1, -1):
            self.arr_elements.sprites()[n].color()

    def show_arr(self):
        """Draw every arr element and fill it"""
        self.arr_elements.draw(screen)
        for n in range(len(self.elements)-1, -1, -1):
            self.arr_elements.sprites()[n].color()

    def bubblesort(self, player_input):
        """ Bubble sort """

        # Highlight first pair of elements
        if self.inner_flag == 0:
            self.arr_elements.sprites()[0].color(Palette.yellow_green)
            self.arr_elements.sprites()[1].color(Palette.pale_green)

        # Classic bubble sort
        for n in range(len(self.elements) - (1 + self.outer_flag), -1, -1):

            # If user hit space and sorting is not done show current step
            if player_input is True and self.exit_flag is False:
                for i in range(n - self.inner_flag):

                    # After loop iteration we break it until user input
                    if player_input is False:
                        self.inner_flag += 1
                        return

                    # Toggle input flag, because user need to activate every
                    # loop iteration by himself
                    player_input = False

                    # If the user did not press the space button, the function
                    # closes and the next time the cycle starts from the
                    # beginning, then we need to indicate where user stopped
                    # last time, flags are used for this
                    n += self.outer_flag
                    i += self.inner_flag

                    # Compare elements
                    if self.elements[i] > self.elements[i + 1]:
                        self.swapped = True
                        self.elements[i], self.elements[i + 1] = self.elements[i + 1], self.elements[i]

                    # Create array after sort operation
                    self.create_arr(self.elements)

                    # Remove selection on first elements
                    if self.inner_flag != 0:
                        self.arr_elements.sprites()[0].color(Palette.white)
                        self.arr_elements.sprites()[1].color(Palette.white)

                    # Clear less element from prev iteration
                    self.arr_elements.sprites()[i-1].color(Palette.white)

                    # Greater element
                    self.arr_elements.sprites()[i+1].color(Palette.yellow_green)

                    # Compared element
                    if n - self.inner_flag != 1:
                        self.arr_elements.sprites()[i+2].color(Palette.pale_green)

                    # Color fully sorted part
                    for j in range(self.outer_flag):
                        self.arr_elements.sprites()[-j-1].color(Palette.green)

                # Flags for loop
                self.inner_flag = 0
                self.outer_flag += 1

                # Sorting is done
                if n == 0:
                    self.swapped = False
                    player_input = False
                    self.exit_flag = True

            # If there is nothing to swap then sorting is done
            elif player_input is True and self.exit_flag is True:
                if not self.swapped:
                    return True

            # Exit function until user input
            elif player_input is False:
                return

        # Reset outer flag when loop is done
        self.outer_flag = 0

    def show_text(self):
        """ Show explanation text about bubble sort"""

        draw_text('Bubble sort', coords=(X//2, 50))
        synopsis = 'Bubble Sort is the simplest sorting algorithm that works'
        synopsis2 = 'by repeatedly swapping the adjacent elements if they are in the wrong order.'
        controls = '"Space" button to sort'
        draw_text(synopsis, font=font_base_small)
        draw_text(synopsis2, font=font_base_small, coords=(X // 2, Y // 2 + 20))
        draw_text(controls, font=font_base_small, coords=(X//2, Y - 50))
        explanation = 'do'
        explanation2 = 'swapped = false'
        explanation3 = 'for i = 1 to indexOfLastUnsortedElement-1'
        explanation4 = 'if leftElement > rightElement'
        explanation5 = 'swap(leftElement, rightElement)'
        explanation6 = 'swapped = true; ++swapCounter'
        explanation7 = 'while swapped'
        draw_text('Algorithm:', font=font_base_small, coords=(X//2, Y//2+60))
        draw_text(explanation, font=font_base_small, coords=(X//2-150, Y//2+80))
        draw_text(explanation2, font=font_base_small, coords=(X//2-100, Y//2+100))
        draw_text(explanation3, font=font_base_small, coords=(X//2-10, Y//2+120))
        draw_text(explanation4, font=font_base_small, coords=(X//2, Y//2+140))
        draw_text(explanation5, font=font_base_small, coords=(X//2+50, Y//2+160))
        draw_text(explanation6, font=font_base_small, coords=(X//2+50, Y//2+180))
        draw_text(explanation7, font=font_base_small, coords=(X//2-100, Y//2+200))

    def show_end_screen(self, player_input):
        """ End screen shows that sorting is done"""

        screen.fill('black')
        self.show_text()
        draw_text('Sorting is done', coords=(X//2, Y//2-100))
        # If user hit space end function
        if player_input:
            return True

    def show(self, player_input):
        """ Show bubble sort if its not done else show end screen"""

        # If sorting is done show end screen
        if self.sort_res is True:
            if self.show_end_screen(player_input) is True:
                return True

        # Else continue sorting
        else:
            screen.fill('black')
            self.show_arr()
            self.sort_res = self.bubblesort(player_input)
            self.show_text()


array_to_demo = [20, 3, 63, 70, 50, 10, 2, 47]
bs = BubbleSort(array_to_demo)


def start_bubblesort(player_input, current_stage):
    """ Start bubble sort explanation """

    res = bs.show(player_input)

    # If bubble sort is done then leave to lobby
    if res is True:
        return 2

    # Else begin this stage again
    else:
        return current_stage
