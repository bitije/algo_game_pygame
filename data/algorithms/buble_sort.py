from data.settings import screen, Palette
import pygame


pygame.init()


class ArrElement(pygame.sprite.Sprite):
    def __init__(self, pos, element, group) -> None:
        super().__init__()

        # Basic attributes
        self.image = pygame.Surface((40, element*2))
        self.change_color(Palette.white)
        self.rect = self.image.get_rect(midbottom=pos)
        self.add(group)

        # Text attributes
        font = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = font.render(f'{element}', 1, Palette.green)
        screen.blit(textSurf, (pos[0]-10, pos[1]+10))

    def change_color(self, color=Palette.red):
        self.image.fill(color)


class BubbleSort():
    def __init__(self) -> None:
        self.slide_num = 5
        self.keydown = 0
        self.arr_elements = pygame.sprite.OrderedUpdates()
        self.elements = [40, 12, 18, 99, 72, 10, 2, 18]

    def show_arr(self):
        for element in range(len(self.elements)):
            x, y = 50 + 50 * element, 250
            ArrElement((x, y), self.elements[element], self.arr_elements)
        self.arr_elements.draw(screen)

    def bubblesort(self):
        swapped = False
        # Looping from size of array from last index[-1] to index [0]
        for n in range(len(self.elements)-1, 0, -1):
            self.arr_elements.sprites()[n].change_color()
            for i in range(n):
                if self.elements[i] > self.elements[i + 1]:
                    swapped = True
                    # swapping data if the element
                    # is less than next element in the array
                    self.elements[i], self.elements[i + 1] = self.elements[i + 1], self.elements[i]
            if not swapped:
                # exiting the function if we didn't make a single swap
                # meaning that the array is already sorted.
                return

    def next_slide(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_SPACE]:
            self.keydown = 0
        elif keys[pygame.K_SPACE] and self.keydown == 0:
            self.slide_num -= 1
            self.keydown = 1

    def show(self):
        screen.fill('black')
        self.show_arr()
        self.bubblesort()


bs = BubbleSort()


def start_bubblesort():
    bs.show()
    if bs.slide_num == 0:
        return 2
    else:
        return 3
