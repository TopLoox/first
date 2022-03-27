import pygame
from data import stroke, stroke4, stroke5

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)


class InvisButtons:
    def __init__(self, inactive_width, inactive_height):
        self.__inactive_width = inactive_width
        self.__inactive_height = inactive_height

    def paint(self, x_coord, y_coord, button_sound, x, y, name, action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(num_buttons=3)

        if (x_coord < mouse[0] < x_coord + self.__inactive_width) and \
                (y_coord < mouse[1] < y_coord + self.__inactive_height):

            if name == 'scroll' or name == 'setts' or name == 'close_window' or name == 'scrolling':
                screen.blit(stroke4, [x_coord, y_coord])
            elif name == 'back_setts':
                screen.blit(stroke5, [x_coord, y_coord])
            elif name != 'back' and name != 'next':
                screen.blit(stroke, [x_coord, y_coord])

            if click[0] == 1 and action is not None and (name == 'next' or name == 'back'):
                pygame.mixer.Sound.play(button_sound)
                action(x)

            elif click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(button_sound)
                if name == 'connect' or name == 'sett_anima':
                    action(x, y)
                else:
                    action()
