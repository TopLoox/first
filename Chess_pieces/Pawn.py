import pygame

import data
from data import after_coord
from data import white_pawn as white, black_pawn as black, getmoment, setmoment
from data import white_pawn_1440 as white_1440, black_pawn_1440 as black_1440

screen = pygame.display.set_mode((1920, 1080))

moment = False
count_moment = 0


class Pawn:
    def __init__(self, x, y, colour):
        self.__count_motion = 0
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__type = 0
        self.__EAT = False

    def motion(self, new_x, new_y):
        if self.__count_motion == 0:
            if (0 < new_y - self.__y <= 2) and (self.__colour == 'Black') and (new_x == self.__x):
                self.__y = new_y
                self.__count_motion += 1
                self.__type = 0
            elif (0 < self.__y - new_y <= 2) and (self.__colour == 'White') and (new_x == self.__x):
                self.__y = new_y
                self.__count_motion += 1
                self.__type = 0
            else:
                self.__type = 0
                return 0

        else:
            if (new_y - self.__y == 1) and (self.__colour == 'Black') and (new_x == self.__x):
                self.__y = new_y
                self.__count_motion += 1
                self.__type = 0
            elif (self.__y - new_y == 1) and (self.__colour == 'White') and (new_x == self.__x):
                self.__y = new_y
                self.__count_motion += 1
                self.__type = 0
            else:
                self.__type = 0
                return 0

        self.__type = 0
        return 1

    def eat(self, new_x, new_y):
        if (self.__y - new_y == 1) and (self.__colour == 'White') and abs(new_x-self.__x) == 1:
            self.__x = new_x
            self.__y = new_y

        if (new_y - self.__y == 1) and (self.__colour == 'Black') and abs(new_x-self.__x) == 1:
            self.__x = new_x
            self.__y = new_y
        self.__type = 0
        return 1

    def coord(self):
        return [self.__x, self.__y]

    def pict(self):
        if self.__EAT:
            if self.__colour == 'White':
                screen.blit(white, after_coord['upper'][count_moment])
            else:
                screen.blit(black, after_coord['lower'][count_moment])
        else:
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

    def eated(self):
        global count_moment, moment
        if moment == False:
            moment = True
            setmoment()
            count_moment = getmoment()

        self.__EAT = True
        self.__x = -10
        self.__y = -10

    def ret(self):
        self.__type = 0

    def coloured(self):
        return self.__colour

    def getCount(self):
        return self.__count_motion

    def revpict(self):
        if self.__EAT:
            if self.__colour == 'White':
                screen.blit(white, after_coord['lower'][count_moment])
            else:
                screen.blit(black, after_coord['upper'][count_moment])
        else:
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
        return 'Pawn'
