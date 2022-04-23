import pygame

import data
from data import white_king as white, black_king as black
from data import white_king_1440 as white_1440, black_king_1440 as black_1440

from Values import screen

class King:
    def __init__(self, x, y, colour):
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__type = 0
        self.__count_motion = 0

    def motion(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y
        self.__count_motion += 1
        return 1

    def castling(self, new_x, new_y):
        self.__count_motion += 1
        self.__x, self.__y = new_x, new_y 

    def pict(self):
        if self.__type == 0:
            resoliton, poss = data.getresol(), data.getposs()
            if self.__colour == 'White':
                if resoliton == '1440':
                    screen.blit(white_1440, (self.__x * (90 - poss[0]) + 600 - poss[1],
                                             self.__y * (90 - poss[0]) + 150 - poss[2]))
                else:
                    screen.blit(white, (self.__x * 90 + 600, self.__y * 90 + 150))
            else:
                if resoliton == '1440':
                    screen.blit(black_1440, (self.__x * (90 - poss[0]) + 600 - poss[1],
                                             self.__y * (90 - poss[0]) + 150 - poss[2]))
                else:
                    screen.blit(black, (self.__x * 90 + 600, self.__y * 90 + 150))

    def coord(self):
        return [self.__x, self.__y]

    def movement_pict(self):
        self.__type = 1
        poss = data.getposs()

        if data.getresol() == '1920':
            if self.__colour == 'White':
                mouse = pygame.mouse.get_pos()
                screen.blit(white, (mouse[0] - 45, mouse[1] - 45))

            else:
                mouse = pygame.mouse.get_pos()
                screen.blit(black, (mouse[0] - 45, mouse[1] - 45))
        else:
            if self.__colour == 'White':
                mouse = pygame.mouse.get_pos()
                screen.blit(white_1440, (mouse[0] - 45 + poss[0] / 2, mouse[1] - 45 + poss[0] / 2))

            else:
                mouse = pygame.mouse.get_pos()
                screen.blit(black_1440, (mouse[0] - 45 + poss[0] / 2, mouse[1] - 45 + poss[0] / 2))

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
    
    def getCount(self):
        return self.__count_motion

    def revpict(self):
        if self.__type == 0:
            resoliton, poss = data.getresol(), data.getposs()
            if self.__colour == 'White':
                if resoliton == '1440':
                    screen.blit(white_1440, (1230 - poss[1] - self.__x * (90 - poss[0]),
                                             780 - poss[2] - self.__y * (90 - poss[0])))
                else:
                    screen.blit(white, (1230 - self.__x * 90, 780 - self.__y * 90))
            else:
                if resoliton == '1440':
                    screen.blit(black_1440, (1230 - poss[1] - self.__x * (90 - poss[0]),
                                             780 - poss[2] - self.__y * (90 - poss[0])))
                else:
                    screen.blit(black, (1230 - self.__x * 90, 780 - self.__y * 90))

    @staticmethod
    def gettype():
        return 'King'
