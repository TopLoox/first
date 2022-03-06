import pygame

screen = pygame.display.set_mode((1920, 1080))

white = pygame.image.load('Image/White_Pawn.png') 
black = pygame.image.load('Image/Black_Pawn.png')


class Pawn:
    def __init__(self, x, y, colour):
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__count_motion = 0
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
                screen.blit(white, (247, 349))
            else:
                screen.blit(black, (247, 544))
        else:
            if self.__type == 0:
                if self.__colour == 'White':
                    screen.blit(white, (self.__x * 90 + 600, self.__y * 90 + 150))
                else:
                    screen.blit(black, (self.__x * 90 + 600, self.__y * 90 + 150))

    def movement_pict(self):
        self.__type = 1

        if self.__colour == 'White':
            mouse = pygame.mouse.get_pos()
            screen.blit(white, (mouse[0] - 45, mouse[1] - 45))

        else:
            mouse = pygame.mouse.get_pos()
            screen.blit(black, (mouse[0] - 45, mouse[1] - 45))

    def eated(self):
        self.__EAT = True
        self.__x = -1
        self.__y = -1

    def ret(self):
        self.__type = 0

    def coloured(self):
        return self.__colour

    def revpict(self):
        if self.__EAT:
            if self.__colour == 'White':
                screen.blit(white, (247, 544))
            else:
                screen.blit(black, (247, 349))
        else:
            if self.__type == 0:
                if self.__colour == 'White':
                    screen.blit(white, (self.__x * 90 + 600, self.__y * 90 + 150))
                else:
                    screen.blit(black, (self.__x * 90 + 600, self.__y * 90 + 150))

    @staticmethod
    def gettype():
        return 'Pawn'

    
