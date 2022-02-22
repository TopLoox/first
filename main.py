import sys
import math

import pygame
import pygame_widgets
from pygame_widgets.button import Button

from Chess_board import Board
from Invisible_Buttons import InvisButtons

from Chess_pieces.Pawn import Pawn
from Chess_pieces.Horse import Horse
from Chess_pieces.Elephant import Elephant
from Chess_pieces.Castle import Castle
from Chess_pieces.Queen import Queen
from Chess_pieces.King import King

import data

pygame.init()

# Списки для фигур
black_pawn = [0] * 8
white_pawn = [0] * 8
black_castle = [0] * 2
white_castle = [0] * 2
black_horse = [0] * 2
white_horse = [0] * 2
black_el = [0] * 2
white_el = [0] * 2

# просто закоментируй, эти строчки
coords = [175, 30, 230, 80]
# coords = [0, 0, 0, 0]

clock = pygame.time.Clock()
# настройки окна
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

lobbyrect = data.fight_image.get_rect()
lobbyrect = lobbyrect.move([-75, 3100 + lobbyrect[1]])

move_xy, zmove_xy, zzmove_xy, zzzmove_xy, move, after = [0 for _ in range(6)]
okno, clo, leg, sc, game, hod, fig, check, part, load = [0 for _ in range(10)]

scroll_button = InvisButtons(150, 150)
Exit_button = InvisButtons(150, 150)
Setting_button = InvisButtons(150, 150)
Server_button = InvisButtons(150, 150)
Single_button = InvisButtons(150, 150)

yes_button = Button(screen, width / 2 - 190, height / 2 - 55, 150, 90, text='Yes', onClick=lambda: close_game())
no_button = Button(screen, width / 2, height / 2 - 55, 200, 90, text='No', onClick=lambda: close_window_no())
close_button = Button(screen, width - 60 - coords[2], 30+coords[3], 30, 30,
                      image=data.close_paint, onClick=lambda: close_window())

yes_button.hide()
no_button.hide()

# Пешки
for i in range(8):
    white_pawn[i], black_pawn[i] = Pawn(i, 6, 'White'), Pawn(i, 1, 'Black')

# Ладьи
white_castle[0], white_castle[1] = Castle(0, 7, 'White'), Castle(7, 7, 'White')
black_castle[0], black_castle[1] = Castle(0, 0, 'Black'), Castle(7, 0, 'Black')

# Кони
white_horse[0], white_horse[1] = Horse(1, 7, 'White'), Horse(6, 7, 'White')
black_horse[0], black_horse[1] = Horse(1, 0, 'Black'), Horse(6, 0, 'Black')

# Слоны
white_el[0], white_el[1] = Elephant(2, 7, 'White'), Elephant(5, 7, 'White')
black_el[0], black_el[1] = Elephant(2, 0, 'Black'), Elephant(5, 0, 'Black')


# Короли и Ферзи
white_queen, black_queen = Queen(3, 7, 'White'), Queen(3, 0, 'Black')
white_king, black_king = King(4, 7, 'White'), King(4, 0, 'Black')

# Все существующие фигуры
White = [white_castle, white_el, white_horse, [white_king], [white_queen], white_pawn]
Black = [black_castle, black_el, black_horse, [black_king], [black_queen], black_pawn]
Figures = [white_castle, white_el, white_horse, [white_king], [white_queen], white_pawn,
           black_castle, black_el, black_horse, [black_king], [black_queen], black_pawn]

# Доска
b = Board()
[[Board.place(b, j, i) for i in range(8)] for j in range(8)]


def print_chess():
    [[k.pict() for k in f] for f in Figures]


def close_window():
    global clo, yes_button, no_button, b
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(data.button_sound)
    clo = 1
    yes_button.show()
    no_button.show()


def close_window_no():
    global clo, yes_button, no_button, b
    clo = 0
    yes_button.hide()
    no_button.hide()
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(data.button_sound)


def close_game():
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(data.button_sound)
    pygame.time.delay(100)
    pygame.quit()
    sys.exit()


def scroll():
    global okno, scroll_button, sc, game
    sc, okno, game = 1, 1, 1
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(data.button_sound)


def scrolling():
    global okno
    okno = 3


def print_text(mes, x, y, font_size, font_color=(0, 0, 0), font_type='font1.ttf'):
    global screen
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(mes, True, font_color)
    screen.blit(text, (x, y))


def blit_place():
    [[InvisButtons.paint(b.board[row][line], 600 + (90 * row), 150 + (90 * line), data.place_sound,
                         row, line, 'connect', action=connect) for row in range(8)] for line in range(8)]


def connect(x, y):
    global hod, fig, part, load
    part = 0
    pygame.time.delay(200)
    condition = True
    if part % 2 == 0:
        if hod == 0:
            for figs in White:
                for m in figs:
                    cord = m.coord()

                    if x == cord[0] and y == cord[1]:
                        hod, fig, load = 1, m, 1

        else:
            hod = 0
            load = 0
            if type(fig) == Pawn:
                cord = fig.coord()

                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if ((cord[1] > cord2[1] >= y) and cord[0] == cord2[0]) or (x != cord[0]):
                            condition = False

                for figs in Black:
                    for m in figs:
                        cord2 = m.coord()

                        if (abs(cord[0] - cord2[0]) == 1) and (cord[1] - cord2[1] == 1) and \
                                (x == cord2[0]) and (y == cord2[1]):
                            part += fig.eat(x, y)
                            m.eated()

            if type(fig) == Castle:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if cord[0] == x:
                            if m.coloured() == 'Black':
                                if ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and (cord[0] == cord2[0]):
                                    condition = False
                            else:
                                if ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and (cord[0] == cord2[0]):
                                    condition = False

                        elif cord[1] == y:
                            if m.coloured() == 'Black':
                                if ((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1]):
                                    condition = False
                            else:
                                if ((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1]):
                                    condition = False

            if type(fig) == Elephant:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'Black':
                            if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                    (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                                     ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y))) or (abs(cord[0]-x) == 0):
                                condition = False

                        else:
                            if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                    (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                                     ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y))) or (abs(cord[0]-x) == 0):
                                condition = False

            if type(fig) == King:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'White':
                            if (cord2 == [x, y]) or (abs(cord[0]-x) > 1) or (abs(cord[1]-y) > 1):
                                condition = False

            if type(fig) == Queen:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'Black':
                            if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                                (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                                 ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)))) or \
                                    ((cord[0] == x) and ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and
                                     (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] < x) or
                                                                (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1])):
                                condition = False

                        else:
                            if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                                (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                                 ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)))) or \
                                    ((cord[0] == x) and ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and
                                     (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] <= x) or
                                                                (cord[0] > cord2[0] >= x)) and (cord[1] == cord2[1])):
                                condition = False

            if type(fig) == Horse:
                if fig.testmotion(x, y) == 0:
                    condition = False

            if condition:
                part += fig.motion(x, y)
                for figs in Black:
                    for m in figs:
                        cord2 = m.coord()
                        if cord2 == [x, y]:
                            m.eated()
                print(fig.coloured(), fig.getType(), x, y)
            else:
                fig.ret()

    else:
        if hod == 0:
            for figs in Black:
                for m in figs:
                    cord = m.coord()

                    if x == cord[0] and y == cord[1]:
                        hod, fig, load = 1, m, 1
        else:
            hod. load = 0, 0
            if type(fig) == Pawn:
                cord = fig.coord()

                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if ((cord[1] < cord2[1] <= y) and cord[0] == cord2[0]) or (x != cord[0]):
                            condition = False

                for figs in White:
                    for m in figs:
                        cord2 = m.coord()

                        if (abs(cord[0] - cord2[0]) == 1) and (cord2[1] - cord[1] == 1) and (cord2 == [x, y]):
                            part += fig.eat(x, y)
                            m.eated()
                            condition = False

            if type(fig) == Castle:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if cord[0] == x:

                            if m.coloured() == 'White':
                                if ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and (cord[0] == cord2[0]):
                                    condition = False
                            else:
                                if ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and (cord[0] == cord2[0]):
                                    condition = False

                        elif cord[1] == y:

                            if m.coloured() == 'White':
                                if ((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1]):
                                    condition = False
                            else:
                                if ((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and (cord[1] == cord2[1]):
                                    condition = False

            if type(fig) == Elephant:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'White':
                            if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                    (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                                     ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y))) or (abs(cord[0]-x) == 0):
                                condition = False

                        else:
                            if (abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and \
                                    (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                                     ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y))) or (abs(cord[0]-x) == 0):
                                condition = False

            if type(fig) == King:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'Black':
                            if (cord2 == [x, y]) or (abs(cord[0]-x) > 1) or (abs(cord[1]-y) > 1):
                                condition = False

            if type(fig) == Queen:
                cord = fig.coord()
                for figs in Figures:
                    for m in figs:
                        cord2 = m.coord()

                        if m.coloured() == 'White':
                            if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                                (((cord[0] < cord2[0] < x) or (cord[0] > cord2[0] > x)) and
                                 ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)))) or \
                                    ((cord[0] == x) and ((cord[1] < cord2[1] < y) or (cord[1] > cord2[1] > y)) and
                                     (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] < x) or
                                                                (cord[0] > cord2[0] > x)) and (cord[1] == cord2[1])):
                                condition = False

                        else:
                            if ((abs(cord[0] - cord2[0]) == abs(cord[1] - cord2[1])) and
                                (((cord[0] < cord2[0] <= x) or (cord[0] > cord2[0] >= x)) and
                                 ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)))) or \
                                    ((cord[0] == x) and ((cord[1] < cord2[1] <= y) or (cord[1] > cord2[1] >= y)) and
                                     (cord[0] == cord2[0])) or ((cord[1] == y) and ((cord[0] < cord2[0] <= x) or
                                                                (cord[0] > cord2[0] >= x)) and (cord[1] == cord2[1])):
                                condition = False

            if type(fig) == Horse:
                if fig.testmotion(x, y) == 0:
                    condition = False

            if condition:
                part += fig.motion(x, y)
                for figs in White:
                    for m in figs:
                        cord2 = m.coord()
                        if cord2 == [x, y]:
                            m.eated()
                print(fig.coloured(), fig.getType(), x, y)

            else:
                fig.ret()


while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            close_game()

    move_xy += 1
    if okno != 5:
        screen.blit(data.lobby_image, lobbyrect)
    else:
        screen.blit(data.fight_image, (lobbyrect[0], lobbyrect[1] + 1000))

    if okno != 1:
        lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                    math.sin(move_xy / 30) * 30 - 3100 - lobbyrect[1] + after])

    if okno == 0:
        screen.blit(data.placebutton1_1, ((width / 2 - 316), height / 7 * 2 - 21 - 120))
        screen.blit(data.play_button, (width / 2 - 75, height / 7 * 2 - 120))
        screen.blit(data.placebutton1_2, (width / 2 - 316, height / 7 * 2 - 21 - 120))
        screen.blit(data.placebutton2_2, (width / 2 - 132, height / 7 * 3.5 - 26 - 120))
        screen.blit(data.setting_button, (width / 2 - 75, height / 7 * 3.5 - 120))
        screen.blit(data.placebutton2_1, (width / 2 - 132, height / 7 * 3.5 - 26 - 120))
        screen.blit(data.placebutton1_1, (width / 2 - 316, height / 7 * 5 - 21 - 120))
        screen.blit(data.exit_button, (width / 2 - 75, height / 7 * 5 - 120))
        screen.blit(data.placebutton1_2, (width / 2 - 316, height / 7 * 5 - 21 - 120))

        scroll_button.paint(width / 2 - 75, height / 7 * 2 - 120, data.button_sound, 0, 0, 'scroll', action=scroll)
        Setting_button.paint(width / 2 - 75, height / 7 * 3.5 - 120, data.button_sound, 0, 0, 'scroll', action=scroll)
        Exit_button.paint(width / 2 - 75, height / 7 * 5 - 120, data.button_sound, 0, 0, 'scroll', action=scroll)

    if okno == 1:
        if zmove_xy <= math.pi * 30:

            # Движение бекграунда
            zmove_xy += 1
            lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                        math.sin(move_xy / 30) * 30 - 3100 +
                                        math.sin(zmove_xy / 60) * 2000 - lobbyrect[1]])

            # Движение кнопок
            screen.blit(data.placebutton3_1, (width / 4, height / 4 + math.sin(zmove_xy / 60) * 2000 - 2000))
            screen.blit(data.single_button, (width / 4 + 39,
                                             height / 4 + 62 + math.sin(zmove_xy / 60) * 2000 - 2000))
            screen.blit(data.placebutton3_2, (width / 4, height / 4 + math.sin(zmove_xy / 60) * 2000 - 2000))
            screen.blit(data.placebutton3_1, (width / 5 * 3,
                                              height / 4 + math.sin(zmove_xy / 60) * 2000 - 2000))
            screen.blit(data.server_button, (width / 5 * 3 + 39,
                                             height / 4 + 62 + math.sin(zmove_xy / 60) * 2000 - 2000))
            screen.blit(data.placebutton3_2, (width / 5 * 3, height / 4 + math.sin(zmove_xy / 60) * 2000 - 2000))

            screen.blit(data.placebutton1_1, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * 4000),
                                              (height / 7 * 2 - 21 - 120) - (math.sin(move_xy / 450) * 1000) + 25))
            screen.blit(data.play_button, ((width / 2 - 75) - (math.sin(zmove_xy / 60) * 4000),
                                           (height / 7 * 2 - 120) - (math.sin(move_xy / 450) * 1000) + 25))
            screen.blit(data.placebutton1_2, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * 4000),
                                              (height / 7 * 2 - 21 - 120) - (math.sin(move_xy / 450) * 1000) + 25))

            if zmove_xy > 2:
                zzmove_xy += 1
                screen.blit(data.placebutton2_2,
                            ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * 4000),
                             (height / 7 * 3.5 - 26 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
                screen.blit(data.setting_button,
                            ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * 4000),
                             (height / 7 * 3.5 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
                screen.blit(data.placebutton2_1,
                            ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * 4000),
                             (height / 7 * 3.5 - 26 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
            else:
                screen.blit(data.placebutton2_2, (width / 2 - 132, height / 7 * 3.5 - 26 - 120))
                screen.blit(data.setting_button, (width / 2 - 75, height / 7 * 3.5 - 120))
                screen.blit(data.placebutton2_1, (width / 2 - 132, height / 7 * 3.5 - 26 - 120))

            if zmove_xy > 3:
                zzzmove_xy += 1
                screen.blit(data.placebutton1_1,
                            ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * 4000),
                             (height / 7 * 5 - 21 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
                screen.blit(data.exit_button,
                            ((width / 2 - 75) - (math.sin(zzzmove_xy / 60) * 4000),
                             (height / 7 * 5 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
                screen.blit(data.placebutton1_2,
                            ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * 4000),
                             (height / 7 * 5 - 21 - 120) - (math.sin(zzmove_xy / 450) * 1000) + 25))
            else:
                screen.blit(data.placebutton1_1, (width / 2 - 316, height / 7 * 5 - 21 - 120))
                screen.blit(data.exit_button, (width / 2 - 75, height / 7 * 5 - 120))
                screen.blit(data.placebutton1_2, (width / 2 - 316, height / 7 * 5 - 21 - 120))

            screen.blit(data.da_screen, (math.sin(zmove_xy / 30) * 146 - 146, (math.sin(zmove_xy / 60) * 4000) - 4000))
            screen.blit(data.da2_screen, (width - math.sin(zmove_xy / 30) * 146, -(math.sin(zmove_xy / 60) * 4000)))

        else:
            after = math.sin(zmove_xy / 60) * 2000
            zmove_xy, zzmove_xy, zzzmove_xy = 0, 0, 0
            okno = 2

    if okno == 2 and clo == 0:
        # Кнопки меню выбора между сервером и одиночной игрой
        screen.blit(data.placebutton3_1, (width / 4, height / 4))
        screen.blit(data.single_button, (width / 4 + 39, height / 4 + 62))
        screen.blit(data.placebutton3_2, (width / 4, height / 4))
        screen.blit(data.placebutton3_1, (width / 5 * 3, height / 4))
        screen.blit(data.server_button, (width / 5 * 3 + 39, height / 4 + 62))
        screen.blit(data.placebutton3_2, (width / 5 * 3, height / 4))
        Server_button.paint(width / 4 + 39, height / 4 + 62, data.button_sound, 0, 0, 'scrolling', action=scrolling)
        Single_button.paint(width / 5 * 3 + 39, height / 4 + 62, data.button_sound, 0, 0, 'scrolling', action=scrolling)

        # screen.blit(place_image, [0, -30])
        # blit_place()
        # print_chess()

    if okno == 2 and clo == 0 and check == 0:
        # check = 1
        # blit_place()
        pass

    if load == 1:
        fig.movement_pict()

    if okno == 3 or okno == 4:
        if okno == 3 and zmove_xy <= math.pi * 6:
            zmove_xy += 1

            screen.blit(data.go, (-(math.sin(zmove_xy / 12) * 2300) + 1920, 0))
        else:
            screen.blit(data.go, (-300, 0))
            okno = 4

    if okno == 4:
        zzmove_xy += 1
        screen.blit(data.player_button, (width / 9 * 3.2, height / 2.5))
        screen.blit(data.pk_button, (width / 9 * 5.2, height / 2.5))
        for nums, i in enumerate([0, 1, 2]):
            screen.blit(data.runs[i - zzmove_xy // 4 % 3], (width / 9 * (4.03 + nums * 0.3), height / 2.5 + 17))

    if clo == 1:
        screen.blit(data.clo_window, (560, 240))

    clock.tick(60)
    pygame_widgets.update(events)
    pygame.display.update()
