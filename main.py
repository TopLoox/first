import sys
import math
import time
import threading

import pygame
import pygame_widgets

print('loading...')

from Chess_board import Board
from Invisible_Buttons import InvisButtons

from Chess_pieces.Pawn import Pawn
from Chess_pieces.Horse import Horse
from Chess_pieces.Elephant import Elephant
from Chess_pieces.Castle import Castle
from Chess_pieces.Queen import Queen
from Chess_pieces.King import King
from Chess_pieces.Figurestype import Figures, Black, White, black_castle, white_castle, white_king, black_king

from client import getClr, getPart, send_server, createpotok, getSerb, getShah, getShahfig, getShahCoord

from Chess_pieces.figcon import con, getCastlin, getMoveing, shahcon

import data

pygame.init()

clock = pygame.time.Clock()

# настройки окна
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

move_xy, zmove_xy, zzmove_xy, zzzmove_xy, move, after, \
    after_but, after_but2, after_but3, after_but4, after_yes, \
    after_no, after_but_yesno, after_buts, after_butz, after_da, after_dev, after_place = [0 for _ in range(18)]
okno, clo, leg, sc, game, hod, fig, check, load, key, bk, moment, \
    songs_id, song_turn, back_lobby, develz = [0 for _ in range(16)]

const = 20

backgrounds = {'1920': [data.background11, data.background12, data.background13, data.background14, data.background15],
               '1440': [data.background21, data.background22, data.background23, data.background24, data.background25]}

songs = [data.forest_songs, data.on_call_songs, data.fortress_songs]

Checks = {'1920': {'white': [data.CheckWhite, data.CheckmateWhite], 'black': [data.CheckBlack, data.CheckmateBlack]},
          '1440': {'white': [data.CheckWhite_1440, data.CheckmateWhite_1440],
                   'black': [data.CheckBlack_1440, data.CheckmateBlack_1440]}}

Сhoses = {'1920': {'white': [data.CheckWhite, data.CheckmateWhite], 'black': [data.CheckBlack, data.CheckmateBlack]},
          '1440': {'white': [data.CheckWhite_1440, data.CheckmateWhite_1440],
                   'black': [data.CheckBlack_1440, data.CheckmateBlack_1440]}}

lobbyrect = data.lobby_image.get_rect()
lobbyrect = lobbyrect.move([-75, 3150 + lobbyrect[1]])

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
yes_button = InvisButtons(143, 43)
no_button = InvisButtons(143, 43)
Devel_butt = InvisButtons(143, 43)
turn_button = InvisButtons(35, 35)
back_button = InvisButtons(35, 35)

# yes_button = Button(screen, width / 2 - 190, height / 2 - 55, 150, 90, text='Yes', onClick=lambda: close_game())
# no_button = Button(screen, width / 2, height / 2 - 55, 200, 90, text='No', onClick=lambda: close_window_no())
# close_button = Button(screen, width - 60 - coords[2], 30+coords[3], 30, 30,
                      # image=data.close_paint, onClick=lambda: close_window())

# yes_button.hide()
# no_button.hide()

# Доска
b = Board()
[[Board.place(b, j, i) for i in range(8)] for j in range(8)]

pygame.mixer.Sound.play(songs[0])


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
    if clo == 0:
        clo = 1
    else:
        clo = 3


def close_game():
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(data.button_sound)
    pygame.time.delay(100)
    pygame.quit()
    sys.exit()


def scroll(g):
    global okno, scroll_button, sc, game
    sc, okno, game = 1, g, 1
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


def devel(condition):
    global develz
    if condition:
        develz = 1
    else:
        develz = 3

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


def turn_song():
    global song_turn
    if song_turn:
        pygame.mixer.Sound.play(songs[songs_id])
        song_turn = 0
    else:
        pygame.mixer.Sound.stop(songs[songs_id])
        song_turn = 1

def connect(x, y):
    global hod, fig, load, key
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
                cord = fig.coord()

                if getShah() == 0:
                    condition = con(fig, x, y, getClr())
                else:
                    king_coord = getShahCoord()
                    condition = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x, y, getClr())

                if type(fig) == Pawn:
                    cord = fig.coord()
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

                if type(fig) == King:
                    if condition and (fig.getCount() == 0) and (cord[1] == y):
                        fig.castling(x, y)
                        castlin = getCastlin()
                        moveing = getMoveing()
                        castlin.castling(moveing, y)
                        part += 1
                        for i in White:
                            if fig in i.values():
                                for j in i:
                                    if fig == i[j]:
                                        key = j
                                        break
                                break
                        send_server(f'{key} {x} {y} {part}')
                        pygame.time.delay(200)
                        for i in White:
                            if castlin in i.values():
                                for j in i:
                                    if castlin == i[j]:
                                        key = j
                                        break
                                break
                        send_server(f'{key} {moveing} {y} {part}')
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
                    fig.ret()
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
                cord = fig.coord()

                if getShah() == 0:
                    condition = con(fig, x, y, getClr())
                else:
                    king_coord = getShahCoord()
                    condition = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x, y, getClr())

                if type(fig) == King:
                    if condition and (fig.getCount() == 0) and (cord[1] == y):
                        fig.castling(x, y)
                        castlin = getCastlin()
                        moveing = getMoveing()
                        castlin.castling(moveing, y)
                        part += 1
                        for i in Black:
                            if fig in i.values():
                                for j in i:
                                    if fig == i[j]:
                                        key = j
                                        break
                                break
                        send_server(f'{key} {x} {y} {part}')
                        pygame.time.delay(200)
                        for i in Black:
                            if castlin in i.values():
                                for j in i:
                                    if castlin == i[j]:
                                        key = j
                                        break
                                break
                        send_server(f'{key} {moveing} {y} {part}')
                        condition = False

                if type(fig) == Pawn:
                    cord = fig.coord()
                    for figs in White:
                        for m in figs.values():
                            cord2 = m.coord()

                            if (abs(cord[0] - cord2[0]) == 1) and (cord2[1] - cord[1] == 1) and (cord2 == [x, y]):
                                part += fig.eat(x, y)
                                m.eated()
                                for i in Black:
                                    if fig in i.values():
                                        for j in i:
                                            if fig == i[j]:
                                                key = j
                                                break
                                        break
                                send_server(f'{key} {x} {y} {part}')
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
                    fig.ret()
                else:
                    fig.ret()


def lobby_anima(condiiton):
    global zmove_xy, zzmove_xy, zzzmove_xy, after, okno, after_buts, after_but, after_da
    if zmove_xy <= math.pi * 30:
        zmove_xy += 1
        zzmove_xy += 1
        zzzmove_xy += 1
        scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, condiiton)
    elif condiiton:
        print('='*20)
        after, after_buts, after_but = math.sin(zmove_xy / 60) * 2000, \
                                        (math.sin(zmove_xy / 60) * 4000), \
                                        (math.sin(zzmove_xy / 30) * 2000 / 25) + 2
        after_da = (math.sin(zmove_xy / 60) * 2000)
        zmove_xy, zzmove_xy, zzzmove_xy = 0, 0, 0
        okno = 2
    elif condiiton == False:
        zmove_xy, zzmove_xy, zzzmove_xy, after, after_buts, after_but, after_da = [0 for _ in range(7)]
        okno = 0



def scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, condition):
    global lobbyrect, move_xy, after_buts, after_but, after_da
    if condition:
        factor = 2000
    else:
        factor = -2000

    lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                math.sin(move_xy / 30) * 30 - 3050 +
                                math.sin(zmove_xy / 60) * factor - lobbyrect[1]])

    # Уход кнопок
    screen.blit(data.placebutton3_1, (width / 4, height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(data.single_button, (width / 4 + 39,
                                     height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(data.placebutton3_2, (width / 4, height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(data.placebutton3_1, (width / 5 * 3,
                                      height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(data.server_button, (width / 5 * 3 + 39,
                                     height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(data.placebutton3_2, (width / 5 * 3, height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))

    if data.getresol() == '1920':
        screen.blit(data.Mini_back, (width - 105, 15 + (math.sin(zmove_xy / 60) * factor) - 2000 + after_da))
    else:
        screen.blit(data.Mini_back, (width - 350, 110 + (math.sin(zmove_xy / 60) * factor) - 2000 + after_da))

    screen.blit(data.placebutton1_1, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                                      (height / 7 * 2 - 21 - 120 + const) -
                                      (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.play_button, ((width / 2 - 75) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                                   (height / 7 * 2 - 120 + const) -
                                   (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton1_2, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                                      (height / 7 * 2 - 21 - 120 + const) -
                                      (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                    (height / 7 * 3.6 - 26 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                    (height / 7 * 3.6 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                    (height / 7 * 3.6 - 26 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton1_1,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                    (height / 7 * 5.2 - 21 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.exit_button,
                ((width / 2 - 75) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                    (height / 7 * 5.2 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton1_2,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                    (height / 7 * 5.2 - 21 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))

    screen.blit(data.da_screen,
                (math.sin(zmove_xy / 30) * 146 - 146, (math.sin(zmove_xy / 30) * factor * 2) - factor - 2000))
    screen.blit(data.da2_screen,
                (width - math.sin(zmove_xy / 30) * 146, (math.sin(zmove_xy / 30) * factor * 2) - factor - 2000))

    print((math.sin(zmove_xy / 30) * abs(factor) * 2) - 4000)

    if clo == 2:
        screen.blit(data.Yes, (math.sin(zzmove_xy / 60) * factor * 1.6 - 1200 + after_yes, height / 2 - 10 + const))
        screen.blit(data.No, (math.sin(zzmove_xy / 60) * -factor * 1.6 + 300 + width + after_no,
                              height / 2 - 135 - 10 + const))


def mini_sett_anima(zzmove_xy, factor):
    return math.sin(zzmove_xy / 30) * factor * 0.875 - 900 + after_but4 + after_but_yesno, height / 2 / 1.7 + const


def mini_yesno_anima(zzmove_xy, factor):
    return math.sin(zzmove_xy / 30) * factor / 25 + 1750 - 900 + after_but_yesno, height / 2 / 1.7 + const


def sett_anima(zzmove_xy, condition):
    global lobbyrect, after_but
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(data.setting_menu, mini_sett_anima(zzmove_xy, factor))

    if data.getresol() == '1920':
        screen.blit(data.Authorship, (width - 445, height - 55))
    else:
        screen.blit(data.Authorship, (width - width / 3, height - height / 6.5))

    if data.getresol() == '1920':
        screen.blit(data.resolition1, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(data.resolition2, mini_sett_anima(zzmove_xy, factor))

    if bk == 0:
        screen.blit(data.sett_background1, mini_sett_anima(zzmove_xy, factor))
    elif bk == 1:
        screen.blit(data.sett_background2, mini_sett_anima(zzmove_xy, factor))
    elif bk == 2:
        screen.blit(data.sett_background3, mini_sett_anima(zzmove_xy, factor))
    elif bk == 3:
        screen.blit(data.sett_background4, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(data.sett_background5, mini_sett_anima(zzmove_xy, factor))

    if songs_id == 0:
        screen.blit(data.Forest_songs, mini_sett_anima(zzmove_xy, factor))
    elif songs_id == 1:
        screen.blit(data.On_call_songs, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(data.Fortress_songs, mini_sett_anima(zzmove_xy, factor))

    screen.blit(data.placebutton1_1, (width / 2 - 316 + after_but_yesno, (height / 7 * 2 - 21 - 120 + const) -
                                      ( math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.play_button, (width / 2 - 75 + after_but_yesno, (height / 7 * 2 - 120 + const) -
                                   (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(data.placebutton1_2, (width / 2 - 316 + after_but_yesno, (height / 7 * 2 - 21 - 120 + const) -
                                      (math.sin(zzmove_xy / 30) * factor / 25) - after_but))

    screen.blit(data.placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 26 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(data.setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(data.placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 26 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))

    screen.blit(data.placebutton1_1, (width / 2 - 316 + after_but_yesno, (height / 7 * 5.2 - 21 - 120 + const) +
                                      (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(data.exit_button, (width / 2 - 75 + after_but_yesno, (height / 7 * 5.2 - 120 + const) +
                                   (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(data.placebutton1_2, (width / 2 - 316 + after_but_yesno, (height / 7 * 5.2 - 21 - 120 + const) +
                                      (math.sin(zzmove_xy / 30) * factor / 25) + after_but))


def yesno(zzmove_xy, condition):
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(data.Yes, (math.sin(zzmove_xy / 30) * factor * 0.875 - 1200 + after_yes, height / 2 - 10 + const))
    screen.blit(data.No, (math.sin(zzmove_xy / 30) * -factor * 0.875 + 300 + width + after_no,
                          height / 2 - 135 - 10 + const))

    screen.blit(data.placebutton1_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                      height / 7 * 2 - 21 - 120 + const - after_but))
    screen.blit(data.play_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                                   height / 7 * 2 - 120 + const - after_but))
    screen.blit(data.placebutton1_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                      height / 7 * 2 - 21 - 120 + const - after_but))

    screen.blit(data.placebutton1_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                      height / 7 * 5.2 - 21 - 120 + const + after_but))
    screen.blit(data.exit_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                                   height / 7 * 5.2 - 120 + const + after_but))
    screen.blit(data.placebutton1_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                      height / 7 * 5.2 - 21 - 120 + const + after_but))

    if okno == -2:
        screen.blit(data.setting_menu, mini_yesno_anima(zzmove_xy, factor))

        if data.getresol() == '1920':
            screen.blit(data.resolition1, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(data.resolition2, mini_yesno_anima(zzmove_xy, factor))

        if bk == 0:
            screen.blit(data.sett_background1, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 1:
            screen.blit(data.sett_background2, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 2:
            screen.blit(data.sett_background3, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 3:
            screen.blit(data.sett_background4, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(data.sett_background5, mini_yesno_anima(zzmove_xy, factor))

        if songs_id == 0:
            screen.blit(data.Forest_songs, mini_yesno_anima(zzmove_xy, factor))
        elif songs_id == 1:
            screen.blit(data.On_call_songs, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(data.Fortress_songs, mini_yesno_anima(zzmove_xy, factor))

    else:
        screen.blit(data.placebutton2_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 132,
                                          height / 7 * 3.6 - 26 - 120 + const))
        screen.blit(data.setting_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                                          height / 7 * 3.6 - 120 + const))
        screen.blit(data.placebutton2_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 132,
                                          height / 7 * 3.6 - 26 - 120 + const))

    pass


def dev_anima(zzmove_xy, condition):
    global after_da, after_dev, after_place

    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(data.placebutton3_1,
                (width / 4 - math.sin(zzmove_xy / 30) * factor  + after_place, height / 4 + const))
    screen.blit(data.single_button,
                (width / 4 + 39 - math.sin(zzmove_xy / 30) * factor  + after_place, height / 4 + 62 + const))
    screen.blit(data.placebutton3_2,
                (width / 4 - math.sin(zzmove_xy / 30) * factor  + after_place, height / 4 + const))

    print(height / 2 - math.sin(zzmove_xy / 30) * factor + 1870 - const + after_dev)

    screen.blit(data.Development,
                (width / 4 - 100, height / 2 - math.sin(zzmove_xy / 30) * factor + 1870 - const + after_dev))
    pass


def chose_anima(zzmove_xy, condition):
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(data.Choice_place, (width / 3 + 777, height / 3))
    screen.blit(data.Choice_place, ((math.sin(zzmove_xy / 30) * factor * 0.3885 + width / 3, height / 3)))

    pass


def check_anima(zzmove_xy, condition, fig, hod):
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(Checks[data.getresol()][fig][hod], (width / 3 + 777, height / 3 - 110))
    screen.blit(Checks[data.getresol()][fig][hod],
                ((math.sin(zzmove_xy / 30) * factor * 0.3885 + width / 3, height / 3 - 110)))
    pass


def next(a):
    pygame.time.delay(200)
    global backgrounds, bk, songs_id
    if a == 1 and bk < 4:
        bk += 1
    elif a == 2 and songs_id < 2:
        songs_id += 1
        pygame.mixer.Sound.stop(songs[songs_id - 1])
        pygame.mixer.Sound.play(songs[songs_id])
    elif a == 3:
        data.setresol()


def back(a):
    pygame.time.delay(200)
    global backgrounds, bk, songs_id
    if a == 1 and bk > 0:
        bk -= 1
    elif a == 2 and songs_id > 0:
        songs_id -= 1
        pygame.mixer.Sound.stop(songs[songs_id + 1])
        pygame.mixer.Sound.play(songs[songs_id])
    elif a == 3:
        data.setresol()


while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            close_game()

    move_xy += 1

    if okno != 5:
        if okno != 2:
            lobbyrect[1] = lobbyrect[1] + after
        screen.blit(data.lobby_image, lobbyrect)

    else:
        if data.getresol() == '1920':
            screen.blit(backgrounds[data.getresol()][bk], (lobbyrect[0], lobbyrect[1] + 1000))
        else:
            screen.blit(backgrounds[data.getresol()][bk], (lobbyrect[0] + 240, lobbyrect[1] + 1000 + 90))

    if okno == -10 and zmove_xy > math.pi * 30:
        after = 0

    if okno != 1:
        lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                    math.sin(move_xy / 30) * 30 - 3050 - lobbyrect[1] + after])

    if clo == 1:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            yesno(zzmove_xy, True)
        else:
            after_yes, after_no, after_but_yesno = (math.sin(zzmove_xy / 30) * 2000 * 0.875), \
                                  (math.sin(zzmove_xy / 30) * -2000 * 0.875), \
                                                   (math.sin(zzmove_xy / 30) * 2000 / 25)
            zzmove_xy, clo = 0, 2

    if clo == 3:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            yesno(zzmove_xy, False)
        else:
            after_yes, after_no, after_but_yesno = 0, 0, 0
            zzmove_xy, clo = 0, 0

    if clo != 1 and clo != 3:
        if okno == 1:
            lobby_anima(True)

        elif okno == -10:
            lobby_anima(False)

    if clo == 2 and okno < 1:
        screen.blit(data.Yes, (after_yes - 1200, height / 2 - 10 + const))
        screen.blit(data.No, (after_no + 300 + width, height / 2 - 135 - 10 + const))
        yes_button.paint(after_yes + 94 - 1200,
                         height / 2 + 15 + const, data.button_sound, 0, 0, 'yes', action=close_game)
        yes_button.paint(after_no + 329 + width,
                         height / 2 - 145 + 27 + const, data.button_sound, 0, 0, 'no', action=close_window)

    # Выдвижение настроек
    if okno == -1:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            sett_anima(zzmove_xy, True)
        else:
            after_but, after_but4 = (math.sin(zzmove_xy / 30) * 2000 / 25), math.sin(zzmove_xy / 30) * 2000 * 0.875
            after_but2, after_but3 = (math.sin(zzmove_xy / 60) * 4000), (math.sin(zzmove_xy / 450) * 1000)
            zzmove_xy = 0
            okno = -2

    if okno == -3 and clo != 1 and clo != 3:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            sett_anima(zzmove_xy, False)
        else:
            after_but, after_but2, after_but3, after_but4, zzmove_xy, okno = [0 for i in range(6)]

    if okno == 2 and clo != 1 and clo != 3:
        # Кнопки меню выбора между сервером и одиночной игрой
        if develz == 0:
            screen.blit(data.placebutton3_1, (width / 4, height / 4 + const))
            screen.blit(data.single_button, (width / 4 + 39, height / 4 + 62 + const))
            screen.blit(data.placebutton3_2, (width / 4, height / 4 + const))
            Single_button.paint(width / 4 + 39,
                                height / 4 + 62 + const, data.button_sound, True, 0, 'devel', action=devel)
        screen.blit(data.placebutton3_1, (width / 5 * 3, height / 4 + const))
        screen.blit(data.server_button, (width / 5 * 3 + 39, height / 4 + 62 + const))
        screen.blit(data.placebutton3_2, (width / 5 * 3, height / 4 + const))
        Server_button.paint(width / 5 * 3 + 39,
                            height / 4 + 62 + const, data.button_sound, 0, 0, 'scrolling', action=scrolling)

        if data.getresol() == '1920':
            screen.blit(data.Mini_back, (width - 105, 15))
            back_button.paint(width - 105, 15, data.button_sound, -10, 0, 'mini_scroll', action=scroll)
        else:
            screen.blit(data.Mini_back, (width - 350, 110))
            back_button.paint(width - 350, 110, data.button_sound, -10, 0, 'mini_scroll', action=scroll)


    if (okno == 0 or okno == -2) and clo != 1 and clo != 3:
        screen.blit(data.placebutton1_1, (width / 2 - 316 + after_but_yesno,
                                          height / 7 * 2 - 21 - 120 - after_but + const))
        screen.blit(data.play_button, (width / 2 - 75 + after_but_yesno,
                                       height / 7 * 2 - 120 - after_but + const))
        screen.blit(data.placebutton1_2, (width / 2 - 316 + after_but_yesno,
                                          height / 7 * 2 - 21 - 120 - after_but + const))
        screen.blit(data.placebutton1_1, (width / 2 - 316 + after_but_yesno,
                                          height / 7 * 5.2 - 21 - 120 + after_but + const))
        screen.blit(data.exit_button, (width / 2 - 75 + after_but_yesno,
                                       height / 7 * 5.2 - 120 + after_but + const))
        screen.blit(data.placebutton1_2, (width / 2 - 316 + after_but_yesno,
                                          height / 7 * 5.2 - 21 - 120 + after_but + const))


        if okno == -2:
            screen.blit(data.setting_menu, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if data.getresol() == '1920':
                screen.blit(data.resolition1, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(data.resolition2, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if bk == 0:
                screen.blit(data.sett_background1, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 1:
                screen.blit(data.sett_background2, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 2:
                screen.blit(data.sett_background3, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 3:
                screen.blit(data.sett_background4, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(data.sett_background5, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if songs_id == 0:
                screen.blit(data.Forest_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif songs_id == 1:
                screen.blit(data.On_call_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(data.Fortress_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            Back_background.paint(width / 7 * 3.21 + after_but_yesno,
                                  height / 1.98 + const, data.button_sound, 1, 0, 'back', action=back)
            Next_background.paint(width / 7 * 3.832 + after_but_yesno,
                                  height / 1.98 + const, data.button_sound, 1, 0, 'next', action=next)
            Back_songs.paint(width / 7 * 3.265 + after_but_yesno,
                             height / 2.33 + const, data.button_sound, 2, 0, 'back', action=back)
            Next_songs.paint(width / 7 * 3.785 + after_but_yesno,
                             height / 2.33 + const, data.button_sound, 2, 0, 'next', action=next)
            Back_resolition.paint(width / 7 * 3.265 + after_but_yesno,
                                  height / 2.64 + const, data.button_sound, 3, 0, 'back', action=back)
            Next_resolition.paint(width / 7 * 3.785 + after_but_yesno,
                                  height / 2.64 + const, data.button_sound, 3, 0, 'next', action=next)

            Back_sett.paint(width / 7 * 3.294 + after_but_yesno - 1,
                            height / 1.7 + const, data.button_sound, 0, 0, 'back_setts', action=back_setts)

            if data.getresol() == '1920':
                screen.blit(data.Authorship, (width - 445, height - 55))
            else:
                screen.blit(data.Authorship, (width - width / 3, height - height / 6.5))

        else:
            screen.blit(data.placebutton2_2, (width / 2 - 132 + after_but_yesno,
                                              height / 7 * 3.6 - 26 - 120 + after_but + const))
            screen.blit(data.setting_button, (width / 2 - 75 + after_but_yesno,
                                              height / 7 * 3.6 - 120 + after_but + const))
            screen.blit(data.placebutton2_1, (width / 2 - 132 + after_but_yesno,
                                              height / 7 * 3.6 - 26 - 120 + after_but + const))

            scroll_button.paint(width / 2 - 75 + after_but_yesno, height / 7 * 2 - 120 - after_but / 1.9 + const,
                                data.button_sound, 1, 0, 'scroll', action=scroll)

            Exit_button.paint(width / 2 - 75 + after_but_yesno, height / 7 * 5.2 - 120 + after_but + const,
                              data.button_sound, 0, 0, 'close_window', action=close_window)

            if data.getresol() == '1920':
                screen.blit(data.Authorship, (width - 445, height - 55))
            else:
                screen.blit(data.Authorship, (width - width / 3, height - height / 6.5))

            Setting_button.paint(width / 2 - 75 + after_but_yesno,
                                 height / 7 * 3.6 - 120 + const, data.button_sound, 0, 0, 'setts', action=setts)

    if getSerb() == 1:
        okno = 5

    if okno == 5 and clo != 1 and clo != 3:
        if data.getresol() == '1920':
            screen.blit(data.place_image, [0, -30])
        else:
            screen.blit(data.place_image_1440, [240, 60])
        blit_place()

        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            chose_anima(zzmove_xy, True)
        else:
            zzmove_xy = 0

        if zzzmove_xy <= math.pi * 15:
            zzzmove_xy += 1
            check_anima(zzzmove_xy, True, 'white', 0)
        else:
            zzzmove_xy = 0

        # screen.blit(data.Choice_place, (width / 3 + 777, height / 3))
        # screen.blit(data.CheckmateBlack, (width / 3 + 777, height / 3 - 110))

        if hod == 1 and getShah() == 0:
            for y1 in range(8):
                for x1 in range(8):
                    if fig.coord() != [x1, y1]:
                        blik = con(fig, x1, y1, getClr())
                        if blik:
                            if getClr() == 'White':
                                screen.blit(data.stroke2, (600 + (90 * x1), 150 + (90 * y1)))
                            else:
                                screen.blit(data.stroke2, (600 + (90 * (7 - x1)), 150 + (90 * (7 - y1))))
        elif hod == 1 and getShah() == 1:
            for y1 in range(8):
                for x1 in range(8):
                    if fig.coord() != [x1, y1]:
                        king_coord = getShahCoord()
                        blik = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x1, y1, getClr())
                        if blik:
                            if getClr() == 'White':
                                screen.blit(data.stroke2, (600 + (90 * x1), 150 + (90 * y1)))
                            else:
                                screen.blit(data.stroke2, (600 + (90 * (7 - x1)), 150 + (90 * (7 - y1))))
        print_chess()

        if okno == 5 and zmove_xy <= math.pi * 6:
            zmove_xy += 1

            screen.blit(data.go, (-(math.cos(zmove_xy / 12) * 2300) - 300, 0))

    if okno == 2 and clo == 0 and check == 0:
        check = 1

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

    if data.getresol() == '1920':
        turn_button.paint(width - 55, 15, data.button_sound, 0, 0, 'turn', action=turn_song)
        if song_turn:
            screen.blit(data.Mini_song_off, (width - 55, 15))
        else:
            screen.blit(data.Mini_song_on, (width - 55, 15))
    else:
        turn_button.paint(width - 55, 15, data.button_sound, 0, 0, 'turn', action=turn_song)
        if song_turn:
            screen.blit(data.Mini_song_off, (width - 295, 110))
        else:
            screen.blit(data.Mini_song_on, (width - 295, 110))

    # Примечание
    if develz == 1:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            dev_anima(zzmove_xy, True)
        else:
            after_dev, develz, after_place = - math.sin(zzmove_xy / 30) * 2000, 2, - math.sin(zzmove_xy / 30) * 2000
            zzmove_xy = 0

    elif develz == 2:
        screen.blit(data.Development, (width / 4 - 100, height / 2 - const + after_dev + 1870))
        Devel_butt.paint(width / 4 + 134, height / 2 - const + after_dev + 1870 + 73,
                          data.button_sound, False, 0, 'devel', action=devel)

    elif develz == 3:
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            dev_anima(zzmove_xy, False)
        else:
            after_dev, develz, after_place = 0, 0, 0
            zzmove_xy = 0

    clock.tick(60)
    pygame_widgets.update(events)
    pygame.display.update()
