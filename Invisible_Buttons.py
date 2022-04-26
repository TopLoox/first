from tkinter.messagebox import NO
from Values import *


class InvisButtons:
    def __init__(self, inactive_width, inactive_height):
        self.__inactive_width = inactive_width
        self.__inactive_height = inactive_height
        self.__press = 0

    def paint(self, x_coord, y_coord, button_sound, x, y, name, action, srh = None, dop_values = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(num_buttons=3)

        if (x_coord < mouse[0] < x_coord + self.__inactive_width) and \
                (y_coord < mouse[1] < y_coord + self.__inactive_height):

            if name == 'scroll' or name == 'setts' or name == 'close_window' or name == 'scrolling' or name == 'devel':
                screen.blit(stroke4, [x_coord, y_coord])
            elif name == 'back_setts' or name == 'yes' or name == 'no' or name == 'back_devel':
                screen.blit(stroke5, [x_coord, y_coord])
            elif name == 'turn' or name == 'mini_scroll':
                screen.blit(Mini_stroke, [x_coord, y_coord])
            elif name != 'back' and name != 'next':
                if getresol() == '1920':
                    screen.blit(stroke, [x_coord, y_coord])
                else:
                    screen.blit(stroke_1440, [x_coord, y_coord])

            if click[0] == 1 and action is not None:
                if (name == 'next' or name == 'back' or name == 'scroll' or name == 'mini_scroll' or
                                                         name == 'back_devel' or name == 'devel'):
                    if self.__press == 0:
                        pygame.mixer.Sound.play(button_sound)
                        action(x)
                        self.__press = 1

                elif srh == 'change':
                    action(dop_values, x, y, name)

                else:
                    if self.__press == 0:
                        pygame.mixer.Sound.play(button_sound)
                        if name == 'connect' or name == 'sett_anima':
                            action(x, y)
                        else:
                            action()
                        self.__press = 1

            elif click[0] == 0:
                self.__press = 0
