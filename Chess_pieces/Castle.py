import pygame

screen = pygame.display.set_mode((1920, 1080))

white = pygame.image.load('Image/White_Castle.png') 
black = pygame.image.load('Image/Black_Castle.png')


class Castle:
    def __init__(self, x, y, colour):
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__type = 0

    def motion(self, new_x, new_y):
        if (self.__x == new_x) and (self.__y != new_y):
            self.__x = new_x
            self.__y = new_y

        elif (self.__y == new_y) and (self.__x != new_x):
            self.__x = new_x
            self.__y = new_y

        else:
            self.__type = 0
            return 0
        self.__type = 0
        return 1

    def pict(self):
        if self.__type == 0:
            if self.__colour == 'White':
                screen.blit(white, (self.__x * 90 + 600, self.__y * 90 + 150))
            else:
                screen.blit(black, (self.__x * 90 + 600, self.__y * 90 + 150))
            
    def coord(self):
        return [self.__x, self.__y]

    def movement_pict(self):
        self.__type = 1

        if self.__colour == 'White':
            mouse = pygame.mouse.get_pos()
            screen.blit(white, (mouse[0] - 45, mouse[1] - 45))

        else:
            mouse = pygame.mouse.get_pos()
            screen.blit(black, (mouse[0] - 45, mouse[1] - 45))

    def ret(self):
        self.__type = 0

    def coloured(self):
        return self.__colour

    def eated(self):
        self.__x = -1
        self.__y = -1

    @staticmethod
    def gettype():
        return 'Castle'
