import pygame
from Invisible_Buttons import InvisButtons
from data import poss

pygame.init()
clock = pygame.time.Clock()

# Изображения
zero = pygame.image.load("Image/Zero.png")
place_image = pygame.image.load('Image/place.png')

white_pawn = pygame.image.load('Image/White_Pawn.png')
black_pawn = pygame.image.load('Image/Black_Pawn.png')
# настройки окна
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
# Переменные для доски
colour = 0

array = {'black_pawn': black_pawn, 'white_pawn': white_pawn}


class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.isMotionActive = False
        self.motion = [0, 0]
        self.move = 0
        self.array = {'black_pawn': black_pawn, 'white_pawn': white_pawn}

    @property
    def get_board(self):
        return self.board

    # Панелька
    def place(self, x, y):
        self.board[x][y] = InvisButtons(90 - poss[0], 90 - poss[0])
