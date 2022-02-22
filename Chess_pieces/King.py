import pygame

screen = pygame.display.set_mode((1920, 1080))

white = pygame.image.load('Image/White_King.png') 
black = pygame.image.load('Image/Black_King.png')


class King:
    def __init__(self, x, y, colour):
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__type = 0

    def motion(self, new_x, new_y):
        if ((abs(self.__x - new_x) == 1) and ((abs(self.__y - new_y) == 1) or (self.__y == new_y))) or \
                ((abs(self.__y - new_y) == 1) and ((abs(self.__x - new_x) == 1) or (self.__x == new_x))):
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
                screen.blit(white, (self.__x * 75 + 650, self.__y * 75 + 200))
            else:
                screen.blit(black, (self.__x * 75 + 650, self.__y * 75 + 200))

    def coord(self):
        return [self.__x, self.__y]

    def movement_pict(self):
        self.__type = 1

        if self.__colour == 'White':
            mouse = pygame.mouse.get_pos()
            screen.blit(white, (mouse[0] - 37.5, mouse[1] - 37.5))

        else:
            mouse = pygame.mouse.get_pos()
            screen.blit(black, (mouse[0] - 37.5, mouse[1] - 37.5))

    def ret(self):
        self.__type = 0

    def coloured(self):
        return self.__colour

    def testmotion(self, new_x, new_y):
        if ((abs(self.__x - new_x) == 1) and ((abs(self.__y - new_y) == 1) or (self.__y == new_y))) or \
                ((abs(self.__y - new_y) == 1) and ((abs(self.__x - new_x) == 1) or (self.__x == new_x))):
            return 1
        else:
            return 0
    
    def eated(self):
        self.__x = -1
        self.__y = -1

    @staticmethod
    def gettype():
        return 'King'
