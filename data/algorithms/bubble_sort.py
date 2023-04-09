from data.settings import screen, Palette
import pygame


pygame.init()


class ArrElement(pygame.sprite.Sprite):
    def __init__(self, pos, element, group) -> None:
        super().__init__()
        self.pos = pos
        self.element = element
        self.image = pygame.Surface((40, 30 + element*2))
        self.image.fill(Palette.white)
        self.rect = self.image.get_rect(midbottom=pos)
        self.add(group)

    def colour_it(self, color=None):
        if color is not None:
            self.image.fill(color)
        # Text attributes
        font = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = font.render(f'{self.element}', 1, Palette.black)
        screen.blit(textSurf, (self.pos[0]-10, self.pos[1]-20))


class BubbleSort():
    def __init__(self, elements) -> None:
        self.slide_num = 5
        self.keydown = 0
        self.elements = elements
        print(elements)
        self.inner_flag = 0
        self.outer_flag = 0
        self.create_arr(self.elements)

    def create_arr(self, elements):
        # Append elements in arr_elements
        self.arr_elements = pygame.sprite.OrderedUpdates()
        for element in range(len(elements)):
            x, y = 50 + 50 * element, 250
            ArrElement((x, y), elements[element], self.arr_elements)
        for n in range(len(self.elements)-1, -1, -1):
            self.arr_elements.sprites()[n].colour_it()

    def show_arr(self):
        """Draw every arr element and fill it"""
        self.arr_elements.draw(screen)
        for n in range(len(self.elements)-1, -1, -1):
            self.arr_elements.sprites()[n].colour_it()

    def bubblesort(self):
        swapped = False
        # Looping from size of array from last index[-1] to index [0]
        for n in range(len(self.elements)-1, 0, -1):
            for i in range(n - self.inner_flag):
                self.arr_elements.sprites()[i].colour_it(Palette.green)  # Change color
                self.arr_elements.sprites()[i+1].colour_it(Palette.green)  # Change color
                if self.elements[i] > self.elements[i + 1]:
                    swapped = True
                    # swapping data if the element
                    # is less than next element in the array
                    self.elements[i], self.elements[i + 1] = self.elements[i + 1], self.elements[i]
            if not swapped:
                # exiting the function if we didn't make a single swap
                # meaning that the array is already sorted.
                return
        # After sorting is done create sorted array
        self.create_arr(self.elements)

    def bubblesort_prototype(self, player_input):
        swapped = False
        # Looping from size of array from last index[-1] to index [0]
        for n in range(len(self.elements)-1 - self.outer_flag, 0, -1):
            self.arr_elements.sprites()[n].colour_it(Palette.red)  # Change color
            if player_input is True:
                n += self.outer_flag
                for i in range(n - self.inner_flag):
                    if player_input is False:
                        self.inner_flag += 1
                        return
                    print(n, n-self.inner_flag, i)
                    i += self.inner_flag
                    player_input = False
                    self.arr_elements.sprites()[i].colour_it(Palette.green)  # Change color
                    # self.arr_elements.sprites()[i+1].colour_it(Palette.green)  # Change color
                    if self.elements[i] > self.elements[i + 1]:
                        self.arr_elements.sprites()[i+1].colour_it(Palette.blue)  # Change color
                        swapped = True
                        # swapping data if the element
                        # is less than next element in the array
                        self.elements[i], self.elements[i + 1] = self.elements[i + 1], self.elements[i]
                self.inner_flag = 0
                self.outer_flag += 1
                if not swapped:
                    # exiting the function if we didn't make a single swap
                    # meaning that the array is already sorted.
                    return
            if player_input is False:
                return
            # After sorting is done create sorted array
            self.create_arr(self.elements)
        self.outer_flag = 0

    def next_slide(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_SPACE]:
            self.keydown = 0
            return True
        elif keys[pygame.K_SPACE] and self.keydown == 0:
            # self.slide_num -= 1
            self.keydown = 1
            return False

    def show(self, player_input):
        screen.fill('black')
        self.show_arr()
        self.bubblesort()
        # self.bubblesort_prototype(player_input)


array_to_demo = [1, 99, 85, 72, 10, 2, 28]
bs = BubbleSort(array_to_demo)


def start_bubblesort(player_input):
    bs.show(player_input)
    if bs.slide_num == 0:
        return 2
    else:
        return 3
