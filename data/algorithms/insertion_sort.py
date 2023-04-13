from data.settings import screen
from data.interface import draw_text
import pygame

pygame.init()

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


class InsertionSort():
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

    def insertionsort(self, player_input):
        """ Insertion sort """
        # Traverse through 1 to len(arr)
        for i in range(self.outer_flag, len(self.elements)):
            self.arr_elements.sprites()[i].color(Palette.pale_green)
            if player_input is True and self.exit_flag is False:
                key = self.elements[i]
                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                j = i-1-self.inner_flag

                if player_input is False:
                    return
                player_input = False
                print(f'i: {i} outer: {self.outer_flag}')
                while j >= 0 and key < self.elements[j]:
                    self.elements[j + 1] = self.elements[j]
                    j -= 1
                    self.inner_flag += 1
                self.elements[j + 1] = key

                self.outer_flag += 1
                self.create_arr(self.elements)
            self.inner_flag = 0

        if self.outer_flag == len(self.elements):
            print('exit flag')
            self.exit_flag = True

        if player_input is True:
            return self.exit_flag

        else:
            return self.exit_flag

    def show_text(self):
        """ Show explanation text about bubble sort"""

        draw_text('Insertion sort', coords=(X//2, 50))
        synopsis = 'The selection sort algorithm sorts an array by repeatedly finding the'
        synopsis2 = 'minimum element from unsorted part and putting it at the beginning.'
        controls = '"Space" button to sort'
        draw_text(synopsis, font=font_base_small)
        draw_text(synopsis2, font=font_base_small, coords=(X // 2, Y // 2 + 20))
        draw_text(controls, font=font_base_small, coords=(X//2, Y - 50))
        explanation = 'repeat (numOfElements - 1) times'
        explanation2 = 'set the first unsorted element as the minimum'
        explanation3 = 'for each of the unsorted elements'
        explanation4 = 'if element < currentMinimum'
        explanation5 = 'set element as new minimum'
        explanation6 = 'swap minimum with first unsorted position'
        draw_text('Algorithm:', font=font_base_small, coords=(X//2, Y//2+60))
        draw_text(explanation, font=font_base_small, coords=(X//2-100+50, Y//2+100))
        draw_text(explanation2, font=font_base_small, coords=(X//2-60+50, Y//2+120))
        draw_text(explanation3, font=font_base_small, coords=(X//2-100+50, Y//2+140))
        draw_text(explanation4, font=font_base_small, coords=(X//2-50+50, Y//2+160))
        draw_text(explanation5, font=font_base_small, coords=(X//2+50, Y//2+180))
        draw_text(explanation6, font=font_base_small, coords=(X//2-65+50, Y//2+200))

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
            self.sort_res = self.insertionsort(player_input)
            self.show_text()


array_to_demo = [20, 3, 63, 70, 50, 10, 2, 47]
bs = InsertionSort(array_to_demo)


def start_insertionsort(player_input, current_stage):
    """ Start bubble sort explanation """

    res = bs.show(player_input)

    # If bubble sort is done then leave to lobby
    if res is True:
        return 2

    # Else begin this stage again
    else:
        return current_stage
