import pygame

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

stroke = pygame.image.load("Image/Blackout_place.png")


class InvisButtons:
    def __init__(self, inactive_width, inactive_height):
        self.__inactive_width = inactive_width
        self.__inactive_height = inactive_height

    def paint(self, x_coord, y_coord, button_sound, x, y, name, action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(num_buttons=3)

        if (x_coord < mouse[0] < x_coord + self.__inactive_width) and \
                (y_coord < mouse[1] < y_coord + self.__inactive_height):
            screen.blit(stroke, [x_coord, y_coord])

            if click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(button_sound)
                if name == 'connect':
                    action(x, y)
                else:
                    action()
