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

from Chess_pieces.Figurestype import Figures, Black, White

from client import getClr, getPart, send_server, createpotok, getSerb, part

import data

pygame.init()

# просто закоментируй, эти строчки
coords = [175, 30, 230, 80]
# coords = [0, 0, 0, 0]

clock = pygame.time.Clock()
# настройки окна
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

move_xy, zmove_xy, zzmove_xy, zzzmove_xy, move, after, after_but, after_but2, after_but3, after_but4 = [0 for _ in range(10)]
okno, clo, leg, sc, game, hod, fig, check, load, key, bk, songs = [0 for _ in range(12)]

resolition = '1440'
backgrounds = {'1440': [data.background11, data.background12, data.background13],
               '1920': [data.background21, data.background22, data.background23]}

lobbyrect = data.lobby_image.get_rect()
lobbyrect = lobbyrect.move([-75, 3100 + lobbyrect[1]])

scroll_button = InvisButtons(150, 150)
Exit_button = InvisButtons(150, 150)
Setting_button = InvisButtons(150, 150)
Server_button = InvisButtons(150, 150)
Single_button = InvisButtons(150, 150)
Back_background = InvisButtons(20, 41)
Next_background = InvisButtons(20, 41)
Back_songs = InvisButtons(14, 27)
Next_songs = InvisButtons(14, 27)
Back_resolition = InvisButtons(14, 27)
Next_resolition = InvisButtons(14, 27)
Back_sett = InvisButtons(143, 43)

yes_button = Button(screen, width / 2 - 190, height / 2 - 55, 150, 90, text='Yes', onClick=lambda: close_game())
no_button = Button(screen, width / 2, height / 2 - 55, 200, 90, text='No', onClick=lambda: close_window_no())
close_button = Button(screen, width - 60 - coords[2], 30+coords[3], 30, 30,
                      image=data.close_paint, onClick=lambda: close_window())

yes_button.hide()
no_button.hide()

# Доска
b = Board()
[[Board.place(b, j, i) for i in range(8)] for j in range(8)]


def print_chess():
    if getClr() == 'White':
        for f in Figures:
            for k in f.values():
                k.pict()
    else:
        for f in Figures:
            for k in f.values():
                k.revpict()


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


def setts():
    global okno
    okno = -1


def back_setts():
    global okno
    okno = -3


def print_text(mes, x, y, font_size, font_color=(0, 0, 0), font_type='font1.ttf'):
    global screen
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(mes, True, font_color)
    screen.blit(text, (x, y))


def blit_place():
    if getClr() == 'White':
        [[InvisButtons.paint(b.board[row][line], 600 + (90 * row), 150 + (90 * line), data.place_sound,
                         row, line, 'connect', action=connect) for row in range(8)] for line in range(8)]
    elif getClr() == 'Black':
        [[InvisButtons.paint(b.board[row][line], 1230 - (90 * row), 780 - (90 * line), data.place_sound,
                         row, line, 'connect', action=connect) for row in range(8)] for line in range(8)]             


def connect(x, y):
    global hod, fig, load, key, part
    pygame.time.delay(200)
    condition = True
    part = getPart()
    if getClr() == 'White':
        if part % 2 == 0:
            if hod == 0:
                for figs in White:
                    for m in figs.values():
                        cord = m.coord()

                        if x == cord[0] and y == cord[1]:
                            hod, fig, load = 1, m, 1

            else:
                hod = 0
                load = 0
                if type(fig) == Pawn:
                    cord = fig.coord()

                    for figs in Figures:
                        for m in figs.values():
                            cord2 = m.coord()

                            if ((cord[1] > cord2[1] >= y) and cord[0] == cord2[0]) or (x != cord[0]):
                                condition = False

                    for figs in Black:
                        for m in figs.values():
                            cord2 = m.coord()

                            if (abs(cord[0] - cord2[0]) == 1) and (cord[1] - cord2[1] == 1) and \
                                    (x == cord2[0]) and (y == cord2[1]):
                                part += fig.eat(x, y)
                                m.eated()
                                for i in White:
                                    if fig in i.values():
                                        for j in i:
                                            if fig == i[j]:
                                                key = j
                                                break
                                        break
                                send_server(f'{key} {x} {y} {part}')
                                condition = False

                if type(fig) == Castle:
                    cord = fig.coord()
                    for figs in Figures:
                        for m in figs.values():
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
                        for m in figs.values():
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
                        for m in figs.values():
                            cord2 = m.coord()

                            if m.coloured() == 'White':
                                if (cord2 == [x, y]) or (abs(cord[0]-x) > 1) or (abs(cord[1]-y) > 1):
                                    condition = False

                if type(fig) == Queen:
                    cord = fig.coord()
                    for figs in Figures:
                        for m in figs.values():
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
                        for m in figs.values():
                            cord2 = m.coord()
                            if cord2 == [x, y]:
                                m.eated()
                    for i in White:
                        if fig in i.values():
                            for j in i:
                                if fig == i[j]:
                                    key = j
                                    break
                            break
                    send_server(f'{key} {x} {y} {part}')
                else:
                    fig.ret()
    else:
        if part % 2 == 1:
            if hod == 0:
                for figs in Black:
                    for m in figs.values():
                        cord = m.coord()

                        if x == cord[0] and y == cord[1]:
                            hod, fig, load = 1, m, 1
            else:
                hod, load = 0, 0
                if type(fig) == Pawn:
                    cord = fig.coord()

                    for figs in Figures:
                        for m in figs.values():
                            cord2 = m.coord()

                            if ((cord[1] < cord2[1] <= y) and cord[0] == cord2[0]) or (x != cord[0]):
                                condition = False

                    for figs in White:
                        for m in figs.values():
                            cord2 = m.coord()

                            if (abs(cord[0] - cord2[0]) == 1) and (cord2[1] - cord[1] == 1) and (cord2 == [x, y]):
                                part += fig.eat(x, y)
                                m.eated()
                                condition = False

                if type(fig) == Castle:
                    cord = fig.coord()
                    for figs in Figures:
                        for m in figs.values():
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
                        for m in figs.values():
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
                        for m in figs.values():
                            cord2 = m.coord()

                            if m.coloured() == 'Black':
                                if (cord2 == [x, y]) or (abs(cord[0]-x) > 1) or (abs(cord[1]-y) > 1):
                                    condition = False

                if type(fig) == Queen:
                    cord = fig.coord()
                    for figs in Figures:
                        for m in figs.values():
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
                        for m in figs.values():
                            cord2 = m.coord()
                            if cord2 == [x, y]:
                                m.eated()
                    for i in Black:
                        if fig in i.values():
                            for j in i:
                                if fig == i[j]:
                                    key = j
                                    break
                            break
                    send_server(f'{key} {x} {y} {part}')

                else:
                    fig.ret()



def scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, condition):
    global lobbyrect, move_xy
    if condition:
        factor = 2000
    else:
        factor = -2000

    lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                math.sin(move_xy / 30) * 30 - 3100 +
                                math.sin(zmove_xy / 60) * factor - lobbyrect[1]])

    # Уход кнопок
    screen.blit(data.placebutton3_1, (width / 4, height / 4 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.single_button, (width / 4 + 39,
                                     height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.placebutton3_2, (width / 4, height / 4 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.placebutton3_1, (width / 5 * 3,
                                      height / 4 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.server_button, (width / 5 * 3 + 39,
                                     height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.placebutton3_2, (width / 5 * 3, height / 4 + math.sin(zmove_xy / 60) * factor - 2000))
    screen.blit(data.placebutton1_1, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2),
                                      (height / 7 * 2 - 21 - 120) - (math.sin(zmove_xy / 450) * factor / 2)))
    screen.blit(data.play_button, ((width / 2 - 75) - (math.sin(zmove_xy / 60) * factor * 2),
                                   (height / 7 * 2 - 120) - (math.sin(zmove_xy / 450) * factor / 2)))
    screen.blit(data.placebutton1_2, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2),
                                      (height / 7 * 2 - 21 - 120) - (math.sin(zmove_xy / 450) * factor / 2)))

    screen.blit(data.placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2),
                    (height / 7 * 3.6 - 26 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))
    screen.blit(data.setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * 4000),
                    (height / 7 * 3.6 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))
    screen.blit(data.placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * 4000),
                    (height / 7 * 3.6 - 26 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))
    screen.blit(data.placebutton1_1,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2),
                    (height / 7 * 5.2 - 21 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))
    screen.blit(data.exit_button,
                ((width / 2 - 75) - (math.sin(zzzmove_xy / 60) * factor * 2),
                    (height / 7 * 5.2 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))
    screen.blit(data.placebutton1_2,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2),
                    (height / 7 * 5.2 - 21 - 120) - (math.sin(zzmove_xy / 450) * factor / 2)))

    screen.blit(data.da_screen, (math.sin(zmove_xy / 30) * 146 - 146, (math.sin(zmove_xy / 60) * factor * 2) - 4000))
    screen.blit(data.da2_screen, (width - math.sin(zmove_xy / 30) * 146, -(math.sin(zmove_xy / 60) * factor * 2)))


def sett_anima(zzmove_xy, condition):
    global lobbyrect, after_but
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(data.setting_menu, (math.sin(zzmove_xy / 30) * factor * 0.875 - 900 + after_but4, height / 2 / 1.7))

    if resolition == '1920':
        screen.blit(data.resolition1, (math.sin(zzmove_xy / 30) * factor * 0.875 - 900  + after_but4, height / 2 / 1.7))
    else:
        screen.blit(data.resolition2, (math.sin(zzmove_xy / 30) * factor * 0.875 - 900  + after_but4, height / 2 / 1.7))

    if bk == 0:
        screen.blit(data.sett_background1,
                    (math.sin(zzmove_xy / 30) * factor * 0.875 - 900  + after_but4, height / 2 / 1.7))
    elif bk == 1:
        screen.blit(data.sett_background2,
                    (math.sin(zzmove_xy / 30) * factor * 0.875 - 900  + after_but4, height / 2 / 1.7))
    else:
        screen.blit(data.sett_background3,
                    (math.sin(zzmove_xy / 30) * factor * 0.875 - 900 + after_but4, height / 2 / 1.7))

    screen.blit(data.placebutton1_1, (width / 2 - 316,
                                      (height / 7 * 2 - 21 - 120) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.play_button, (width / 2 - 75,
                                   (height / 7 * 2 - 120) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton1_2, (width / 2 - 316,
                                      (height / 7 * 2 - 21 - 120) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))

    screen.blit(data.placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2,
                    (height / 7 * 3.7 - 26 - 120) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(data.setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2,
                    (height / 7 * 3.7 - 120) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(data.placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2,
                    (height / 7 * 3.7 - 26 - 120) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))

    screen.blit(data.placebutton1_1,
                (width / 2 - 316,
                    (height / 7 * 5.2 - 21 - 120) + (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(data.exit_button,
                (width / 2 - 75,
                    (height / 7 * 5.2 - 120) + (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(data.placebutton1_2,
                (width / 2 - 316,
                    (height / 7 * 5.2 - 21 - 120) + (math.sin(zzmove_xy / 30) * factor / 25) + after_but))


def Next(a):
    pygame.time.delay(200)
    global backgrounds, bk, resolition, songs
    if a == 1 and bk < 2:
        bk += 1
    elif a == 2 and songs < 2:
        songs += 1
    elif a == 3 and resolition == '1920':
        resolition = '1440'
    elif a == 3 and resolition == '1440':
        resolition = '1920'


def Back(a):
    pygame.time.delay(200)
    global backgrounds, bk, resolition, songs
    if a == 1 and bk > 0:
        bk -= 1
    elif a == 2 and songs > 0:
        songs -= 1
    elif a == 3 and resolition == '1920':
        resolition = '1440'
    elif a == 3 and resolition == '1440':
        resolition = '1920'


while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            close_game()

    move_xy += 1
    if okno != 5:
        screen.blit(data.lobby_image, lobbyrect)
    else:
        screen.blit(backgrounds[resolition][bk], (lobbyrect[0], lobbyrect[1] + 1000))

    if okno != 1:
        lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                    math.sin(move_xy / 30) * 30 - 3100 - lobbyrect[1] + after])

    if okno == 1:
        if zmove_xy <= math.pi * 30:
            zmove_xy += 1
            zzmove_xy += 1
            zzzmove_xy += 1
            scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, True)

        else:
            after = math.sin(zmove_xy / 60) * 2000
            zmove_xy, zzmove_xy, zzzmove_xy = 0, 0, 0
            okno = 2

    # Выдвижение настроек
    if okno == -1:
        if zmove_xy <= math.pi * 15:
            zmove_xy += 1
            zzmove_xy += 1
            zzzmove_xy += 1
            sett_anima(zzmove_xy, True)
        else:
            after_but, after_but4 = (math.sin(zzmove_xy / 30) * 2000 / 25), math.sin(zzmove_xy / 30) * 2000 * 0.875
            after_but2, after_but3 = (math.sin(zzmove_xy / 60) * 4000), (math.sin(zzmove_xy / 450) * 1000)
            zmove_xy, zzmove_xy, zzzmove_xy = 0, 0, 0
            okno = -2

    if okno == -3:
        if zmove_xy <= math.pi * 15:
            zmove_xy += 1
            zzmove_xy += 1
            zzzmove_xy += 1
            sett_anima(zzmove_xy, False)
        else:
            after_but, zmove_xy, zzmove_xy, zzzmove_xy, okno = 0, 0, 0, 0, 0

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

    if okno == 0 or okno == -2:
        screen.blit(data.placebutton1_1, ((width / 2 - 316), height / 7 * 2 - 21 - 120 - after_but))
        screen.blit(data.play_button, (width / 2 - 75, height / 7 * 2 - 120 - after_but))
        screen.blit(data.placebutton1_2, (width / 2 - 316, height / 7 * 2 - 21 - 120 - after_but))
        screen.blit(data.placebutton1_1, (width / 2 - 316, height / 7 * 5.2 - 21 - 120 + after_but))
        screen.blit(data.exit_button, (width / 2 - 75, height / 7 * 5.2 - 120 + after_but))
        screen.blit(data.placebutton1_2, (width / 2 - 316, height / 7 * 5.2 - 21 - 120 + after_but))

        if okno == -2:
            screen.blit(data.setting_menu, (1750 - 900, height / 2 / 1.7))

            if resolition == '1920':
                screen.blit(data.resolition1, (1750 - 900, height / 2 / 1.7))
            else:
                screen.blit(data.resolition2, (1750 - 900, height / 2 / 1.7))

            if bk == 0:
                screen.blit(data.sett_background1, (1750 - 900, height / 2 / 1.7))
            elif bk == 1:
                screen.blit(data.sett_background2, (1750 - 900, height / 2 / 1.7))
            else:
                screen.blit(data.sett_background3, (1750 - 900, height / 2 / 1.7))

            Back_background.paint(width / 7 * 3.21, height / 1.98, data.button_sound, 1, 0, 'next', action=Back)
            Next_background.paint(width / 7 * 3.832, height / 1.98, data.button_sound, 1, 0, 'next', action=Next)
            Back_songs.paint(width / 7 * 3.265, height / 2.33, data.button_sound, 2, 0, 'next', action=Back)
            Next_songs.paint(width / 7 * 3.785, height / 2.33, data.button_sound, 2, 0, 'next', action=Next)
            Back_resolition.paint(width / 7 * 3.265, height / 2.64, data.button_sound, 3, 0, 'next', action=Back)
            Next_resolition.paint(width / 7 * 3.785, height / 2.64, data.button_sound, 3, 0, 'next', action=Next)

            Back_sett.paint(width / 7 * 3.294, height / 1.7, data.button_sound, 0, 0, 'back_setts', action=back_setts)
        else:
            Setting_button.paint(width / 2 - 75, height / 7 * 3.6 - 120, data.button_sound, 0, 0, 'setts',action=setts)
            screen.blit(data.placebutton2_2, (width / 2 - 132, height / 7 * 3.6 - 26 - 120 + after_but))
            screen.blit(data.setting_button, (width / 2 - 75, height / 7 * 3.6 - 120 + after_but))
            screen.blit(data.placebutton2_1, (width / 2 - 132, height / 7 * 3.6 - 26 - 120 + after_but))

            scroll_button.paint(width / 2 - 75, height / 7 * 2 - 120 - after_but / 1.9,
                            data.button_sound, 0, 0, 'scroll', action=scroll)
            Exit_button.paint(width / 2 - 75, height / 7 * 5.2 - 120 + after_but,
                          data.button_sound, 0, 0, 'scroll', action=close_window)
    
    if getSerb() == 1:
        okno = 5

    if okno == 5:
        screen.blit(data.place_image, [0, -30])
        blit_place()
        print_chess()

        if okno == 5 and zmove_xy <= math.pi * 6:
            zmove_xy += 1

            screen.blit(data.go, (-(math.cos(zmove_xy / 12) * 2300) - 300, 0))
        
    if okno == 2 and clo == 0 and check == 0:
        check = 1
        blit_place()
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
        if zzmove_xy == 0: 
            createpotok()

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
