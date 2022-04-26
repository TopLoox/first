from concurrent.futures.process import _check_system_limits
import sys
import math
from tkinter import Y

import pygame_widgets

from Chess_board import Board
from Invisible_Buttons import InvisButtons

from Chess_pieces.Pawn import Pawn
from Chess_pieces.King import King
from Chess_pieces.Figurestype import Figures, Black, White

from client import getChClr, getChcd, getClr, getPart, send_server, createpotok, getSerb, getShah, getShahfig, getShahCoord, getPh, getPhFig, getFin

from Chess_pieces.figcon import con, getCastlin, getMoveing, shahcon
from Values import *

pygame.init()

clock = pygame.time.Clock()

lobbyrect = lobby_image.get_rect()
lobbyrect = lobbyrect.move([-75, 3120 + lobbyrect[1]])

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
horse_button = InvisButtons(90, 90)
el_button = InvisButtons(90, 90)
castle_button = InvisButtons(90, 90)
queen_button = InvisButtons(90, 90)

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
        pygame.mixer.Sound.play(button_sound)
    if clo == 0:
        clo = 1
    else:
        clo = 3


def close_game():
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(button_sound)
    pygame.time.delay(100)
    pygame.quit()
    sys.exit()


def scroll(g):
    global okno, scroll_button, sc, game
    sc, okno, game = 1, g, 1
    click = pygame.mouse.get_pressed(num_buttons=3)
    if click[0]:
        pygame.mixer.Sound.play(button_sound)


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


def blit_place():
    if getClr() == 'White':
        [[InvisButtons.paint(b.board[row][line], 600 - poss[1] + ((90 - poss[0]) * row),
                             150 - poss[2] + ((90 - poss[0]) * line), place_sound, row, line,
                             'connect', action=connect) for row in range(8)] for line in range(8)]
    elif getClr() == 'Black':
        [[InvisButtons.paint(b.board[row][line], 1230 - poss[1] - ((90 - poss[0]) * row),
                             780 - poss[2] - ((90 - poss[0]) * line), place_sound, row, line,
                             'connect', action=connect) for row in range(8)] for line in range(8)]


def turn_song():
    global song_turn
    if song_turn:
        pygame.mixer.Sound.play(songs[songs_id])
        song_turn = 0
    else:
        pygame.mixer.Sound.stop(songs[songs_id])
        song_turn = 1


def getDates(x, y, key):
    global chX, chY, chKey
    chX = x
    chY = y
    chKey = key


def connect(x, y):
    global hod, fig, load, key
    pygame.time.delay(200)
    condition = True
    part = getPart()
    if not getChcd():
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
                        condition = con(fig, x, y, getClr(),phant)
                    else:
                        king_coord = getShahCoord()
                        condition = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x, y, getClr(),phant)

                    if type(fig) == Pawn:
                        if y == 0 and condition:
                            for i in White:
                                if fig in i.values():
                                    for j in i:
                                        if fig == i[j]:
                                            key = j
                                            break
                                    break
                            Choose_condition = True
                            send_server(f'{Choose_condition} {"White"} {""}') 
                            pygame.time.delay(200)
                            getDates(x, y, key)  

                        cord = fig.coord()
                        for figs in Black:
                            for m in figs.values():
                                cord2 = m.coord()
                                cordph = phant.coord()
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
                        if (abs(cord[0] - cordph[0]) == 1) and (cord[1] - cordph[1] == 1) and \
                                (x == cordph[0]) and (y == cordph[1]):
                            part += fig.eat(x, y)
                            for phfigs in Black:
                                for phm in phfigs.values():
                                    cordphm = phm.coord()
                                    if (cordph[0] == cordphm[0]) and (cordphm[1] - cordph[1] == 1):
                                        phm.eated()
                                        print("EATALL")
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
                        condition = con(fig, x, y, getClr(),phant)
                    else:
                        king_coord = getShahCoord()
                        condition = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x, y, getClr(),phant)

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
                        if y == 0 and condition:
                            for i in Black:
                                if fig in i.values():
                                    for j in i:
                                        if fig == i[j]:
                                            key = j
                                            break
                                    break
                            Choose_condition = True
                            send_server(f'{Choose_condition} {"Black"} {""}') 
                            pygame.time.delay(200)  
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


# Сокращающие код функции
# =============================================================================================
def stroke():
    if blik:
        if getresol() == '1920':
            if getClr() == 'White':
                screen.blit(stroke2, (600 + (90 * x1), 150 + (90 * y1)))
            else:
                screen.blit(stroke2, (600 + (90 * (7 - x1)), 150 + (90 * (7 - y1))))
        else:
            if getClr() == 'White':
                screen.blit(stroke2_1440, (600 - poss[1] + ((90 - poss[0]) * x1),
                                           150 - poss[2] + ((90 - poss[0]) * y1)))
            else:
                screen.blit(stroke2_1440, (600 - poss[1] + ((90 - poss[0]) * (7 - x1)),
                                           150 - poss[2] + ((90 - poss[0]) * (7 - y1))))


def mini_sett_anima(zzmove_xy, factor):
    return math.sin(zzmove_xy / 30) * factor * 0.875 - 900 + after_but4 + after_but_yesno, height / 2 / 1.7 + const


def mini_yesno_anima(zzmove_xy, factor):
    return math.sin(zzmove_xy / 30) * factor / 25 + 1750 - 900 + after_but_yesno, height / 2 / 1.7 + const


def lobby_anima(condiiton):
    global zmove_xy, zzmove_xy, zzzmove_xy, after, okno, after_buts, after_but, after_da, after_dev, after_dev2
    if zmove_xy <= math.pi * 30:
        zmove_xy += 1
        zzmove_xy += 1
        zzzmove_xy += 1
        scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, condiiton)
    elif condiiton:
        after, after_buts, after_but = math.sin(zmove_xy / 60) * 2000, \
                                       (math.sin(zmove_xy / 60) * 4000), \
                                       (math.sin(zzmove_xy / 30) * 2000 / 25) + 2,
        after_da, after_dev2 = (math.sin(zmove_xy / 60) * 2000), (math.sin(zmove_xy / 60) * 2000)
        zmove_xy, zzmove_xy, zzzmove_xy = 0, 0, 0
        okno = 2
    elif condiiton == False:
        zmove_xy, zzmove_xy, zzzmove_xy, after, after_buts,\
        after_but, after_da, after_but2 = [0 for _ in range(8)]
        after_dev2 = 4000
        okno = 0


# =============================================================================================


# Анимация прокрутки
def scroll_anima(zmove_xy, zzmove_xy, zzzmove_xy, condition):
    global lobbyrect, move_xy, after_buts, after_but, after_da, after_dev2
    if condition:
        factor = 2000
    else:
        factor = -2000

    lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                math.sin(move_xy / 30) * 30 - 3100 +
                                math.sin(zmove_xy / 60) * factor - lobbyrect[1]])

    # Уход кнопок
    if develz == 0:
        screen.blit(placebutton3_1, (width / 4, height / 4 + math.sin(zmove_xy / 60)
                                     * factor - 2000 + const + after_da))
        screen.blit(single_button, (width / 4 + 39,
                                    height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
        screen.blit(placebutton3_2, (width / 4, height / 4 + math.sin(zmove_xy / 60)
                                     * factor - 2000 + const + after_da))
    else:
        screen.blit(Development, (width / 4 - 100, height / 2 + math.sin(zmove_xy / 60)
                                     * factor + 1870 - const - after_dev2))

    screen.blit(placebutton3_1, (width / 5 * 3,
                                 height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(server_button, (width / 5 * 3 + 39,
                                height / 4 + 62 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(placebutton3_2,
                (width / 5 * 3, height / 4 + math.sin(zmove_xy / 60) * factor - 2000 + const + after_da))
    screen.blit(Mini_back, (width - 350, 110 + (math.sin(zmove_xy / 60) * factor) - 2000 + after_da))

    screen.blit(placebutton1_1, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                                 (height / 7 * 2 - 21 - 120 + const) -
                                 (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(play_button, ((width / 2 - 75) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                              (height / 7 * 2 - 120 + const) -
                              (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton1_2, ((width / 2 - 316) - (math.sin(zmove_xy / 60) * factor * 2) - after_buts,
                                 (height / 7 * 2 - 21 - 120 + const) -
                                 (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                 (height / 7 * 3.6 - 26 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                 (height / 7 * 3.6 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_buts,
                 (height / 7 * 3.6 - 26 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton1_1,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                 (height / 7 * 5.2 - 21 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(exit_button,
                ((width / 2 - 75) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                 (height / 7 * 5.2 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton1_2,
                ((width / 2 - 316) - (math.sin(zzzmove_xy / 60) * factor * 2) - after_buts,
                 (height / 7 * 5.2 - 21 - 120 + const) - (math.sin(zzmove_xy / 30) * factor / 25) - after_but))

    if resolition == '1920':
        screen.blit(da_screen,
                    (math.sin(zmove_xy / 30) * 146 - 146, (math.sin(zmove_xy / 30) * factor * 2) - factor - 2000))
        screen.blit(da2_screen,
                    (width - math.sin(zmove_xy / 30) * 146, (math.sin(zmove_xy / 30) * factor * 2) - factor - 2000))
    else:
        screen.blit(da_screen,
                    (math.sin(zmove_xy / 30) * 146 - 146 + 200, (math.sin(zmove_xy / 30) * factor) - factor - 2000))
        screen.blit(da2_screen,
                    (width - math.sin(zmove_xy / 30) * 146 - 200, (math.sin(zmove_xy / 30) * factor) - factor - 2000))

    if clo == 2:
        screen.blit(Yes, (math.sin(zzmove_xy / 60) * factor * 1.6 - 1200 + after_yes, height / 2 - 10 + const))
        screen.blit(No, (math.sin(zzmove_xy / 60) * -factor * 1.6 + 300 + width + after_no,
                         height / 2 - 135 - 10 + const))


#Замена пешки на другие фигуры
def changeFig(key, figs, x, y):
    chg = 'change'
    send_server(f'{key} {x} {y} {figs} {chg}')                


# Анимация выдвижения настроек
def sett_anima(zzmove_xy, condition):
    global lobbyrect, after_but
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(setting_menu, mini_sett_anima(zzmove_xy, factor))

    if getresol() == '1920':
        screen.blit(resolition1, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(resolition2, mini_sett_anima(zzmove_xy, factor))

    if bk == 0:
        screen.blit(sett_background1, mini_sett_anima(zzmove_xy, factor))
    elif bk == 1:
        screen.blit(sett_background2, mini_sett_anima(zzmove_xy, factor))
    elif bk == 2:
        screen.blit(sett_background3, mini_sett_anima(zzmove_xy, factor))
    elif bk == 3:
        screen.blit(sett_background4, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(sett_background5, mini_sett_anima(zzmove_xy, factor))

    if songs_id == 0:
        screen.blit(Forest_songs, mini_sett_anima(zzmove_xy, factor))
    elif songs_id == 1:
        screen.blit(On_call_songs, mini_sett_anima(zzmove_xy, factor))
    else:
        screen.blit(Fortress_songs, mini_sett_anima(zzmove_xy, factor))

    screen.blit(placebutton1_1, (width / 2 - 316 + after_but_yesno, (height / 7 * 2 - 21 - 120 + const) -
                                 (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(play_button, (width / 2 - 75 + after_but_yesno, (height / 7 * 2 - 120 + const) -
                              (math.sin(zzmove_xy / 30) * factor / 25) - after_but))
    screen.blit(placebutton1_2, (width / 2 - 316 + after_but_yesno, (height / 7 * 2 - 21 - 120 + const) -
                                 (math.sin(zzmove_xy / 30) * factor / 25) - after_but))

    screen.blit(placebutton2_2,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 26 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(setting_button,
                ((width / 2 - 75) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))
    screen.blit(placebutton2_1,
                ((width / 2 - 132) + (math.sin(zzmove_xy / 60) * factor * 2) + after_but2 + after_but_yesno,
                 (height / 7 * 3.7 - 26 - 120 + const) - (math.sin(zzmove_xy / 450) * factor / 2) - after_but3 - 15))

    screen.blit(placebutton1_1, (width / 2 - 316 + after_but_yesno, (height / 7 * 5.2 - 21 - 120 + const) +
                                 (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(exit_button, (width / 2 - 75 + after_but_yesno, (height / 7 * 5.2 - 120 + const) +
                              (math.sin(zzmove_xy / 30) * factor / 25) + after_but))
    screen.blit(placebutton1_2, (width / 2 - 316 + after_but_yesno, (height / 7 * 5.2 - 21 - 120 + const) +
                                 (math.sin(zzmove_xy / 30) * factor / 25) + after_but))


# Анимация yes / no
def yesno(zzmove_xy, condition):
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(Yes, (math.sin(zzmove_xy / 30) * factor * 0.875 - 1200 + after_yes, height / 2 - 10 + const))
    screen.blit(No, (math.sin(zzmove_xy / 30) * -factor * 0.875 + 300 + width + after_no,
                     height / 2 - 135 - 10 + const))

    screen.blit(placebutton1_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                 height / 7 * 2 - 21 - 120 + const - after_but))
    screen.blit(play_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                              height / 7 * 2 - 120 + const - after_but))
    screen.blit(placebutton1_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                 height / 7 * 2 - 21 - 120 + const - after_but))

    screen.blit(placebutton1_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                 height / 7 * 5.2 - 21 - 120 + const + after_but))
    screen.blit(exit_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                              height / 7 * 5.2 - 120 + const + after_but))
    screen.blit(placebutton1_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 316,
                                 height / 7 * 5.2 - 21 - 120 + const + after_but))

    if okno == -2:
        screen.blit(setting_menu, mini_yesno_anima(zzmove_xy, factor))

        if getresol() == '1920':
            screen.blit(resolition1, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(resolition2, mini_yesno_anima(zzmove_xy, factor))

        if bk == 0:
            screen.blit(sett_background1, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 1:
            screen.blit(sett_background2, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 2:
            screen.blit(sett_background3, mini_yesno_anima(zzmove_xy, factor))
        elif bk == 3:
            screen.blit(sett_background4, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(sett_background5, mini_yesno_anima(zzmove_xy, factor))

        if songs_id == 0:
            screen.blit(Forest_songs, mini_yesno_anima(zzmove_xy, factor))
        elif songs_id == 1:
            screen.blit(On_call_songs, mini_yesno_anima(zzmove_xy, factor))
        else:
            screen.blit(Fortress_songs, mini_yesno_anima(zzmove_xy, factor))

    else:
        screen.blit(placebutton2_2, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 132,
                                     height / 7 * 3.6 - 26 - 120 + const))
        screen.blit(setting_button, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 75,
                                     height / 7 * 3.6 - 120 + const))
        screen.blit(placebutton2_1, ((math.sin(zzmove_xy / 30) * factor / 25) + after_but_yesno + width / 2 - 132,
                                     height / 7 * 3.6 - 26 - 120 + const))


# Анимация предупреждения
def dev_anima(zzmove_xy, condition):
    global after_da, after_dev, after_place

    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(placebutton3_1,
                (width / 4 - math.sin(zzmove_xy / 30) * factor + after_place, height / 4 + const))
    screen.blit(single_button,
                (width / 4 + 39 - math.sin(zzmove_xy / 30) * factor + after_place, height / 4 + 62 + const))
    screen.blit(placebutton3_2,
                (width / 4 - math.sin(zzmove_xy / 30) * factor + after_place, height / 4 + const))

    screen.blit(Development,
                (width / 4 - 100, height / 2 - math.sin(zzmove_xy / 30) * factor + 1870 - const + after_dev))


# Анимация выдвижения выбора
def chose_anima(condition, x, y, keys):   
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(Choice_place, (width / 3 + 777, height / 3 - 110))
    screen.blit(choice, (width / 3 + 777, height / 3 - 110))
    screen.blit(Choice_white, (width / 3 + 777, height / 3 - 110))

    horse_button.paint(width / 3 + 777, height / 3 - 110, button_sound, x, y, 'Horse', action=change, srh='change', dop_values=keys)
    el_button.paint(width / 3 + 887, height / 3 - 110, button_sound, x, y, 'Elephant', action=change, srh='change', dop_values=keys)
    castle_button.paint(width / 3 + 997, height / 3 - 110, button_sound, x, y, 'Castle', action=change, srh='change', dop_values=keys)
    queen_button.paint(width / 3 + 1007, height / 3 - 110, button_sound, x, y, 'Queen', action=change, srh='change', dop_values=keys)

    #screen.blit(Choice_place, ((math.sin(zzmove_xy / 30) * factor * 0.3885 + width / 3, height / 3)))


#Отправляем на сервер инфу об изменении пешки
def change(key, x, y, figs):
    send_server(f'{key} {x} {y} {figs} {getClr()}')


# Анимация предупреждения о шахе / мате
def check_anima(zzmove_xy, condition, fig, hod):
    if condition:
        factor = 2000
    else:
        factor = -2000

    screen.blit(Checks[getresol()][fig][hod], (width / 3 + 777 + poss[1], height / 3 - poss[2]))
    #screen.blit(Checks[getresol()][fig][hod],
                #((math.sin(zzmove_xy / 30) * factor * 0.3885 + width / 3, height / 3 - 110)))


# Кнопка далее в настройках
def next(a):
    pygame.time.delay(200)
    global backgrounds, bk, songs_id
    if a == 1 and bk < 4:
        bk += 1
    elif a == 2 and songs_id < 2:
        songs_id += 1
        pygame.mixer.Sound.stop(songs[songs_id - 1])
        if not(song_turn):
            pygame.mixer.Sound.play(songs[songs_id])
    elif a == 3:
        setresol()


# Кнопка возврата в настройках
def back(a):
    pygame.time.delay(200)
    global backgrounds, bk, songs_id
    if a == 1 and bk > 0:
        bk -= 1
    elif a == 2 and songs_id > 0:
        songs_id -= 1
        pygame.mixer.Sound.stop(songs[songs_id + 1])
        if not (song_turn):
            pygame.mixer.Sound.play(songs[songs_id])
    elif a == 3:
        setresol()


# Тело игры
while 1:
    # Обновление событий
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            close_game()

    move_xy += 1

    # Фон
    if okno != 5:
        if okno != 2 and okno != 3:
            lobbyrect[1] = lobbyrect[1] + after
        screen.blit(lobby_image, lobbyrect)

    else:
        if getresol() == '1920':
            screen.blit(backgrounds[getresol()][bk], (lobbyrect[0], lobbyrect[1] + 1000))
        else:
            screen.blit(backgrounds[getresol()][bk], (lobbyrect[0] + 240, lobbyrect[1] + 1000 + 90))

    # Контроль переменной after
    if okno == -10 and zmove_xy > math.pi * 30:
        after = 0

    if okno != 1:
        lobbyrect = lobbyrect.move([math.cos(move_xy / 60) * 30 - 75 - lobbyrect[0],
                                    math.sin(move_xy / 30) * 30 - 3100 - lobbyrect[1] + after])

    # Настройка выдвигающей анимации yes / no
    if clo == 1:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
        else:
            after_yes, after_no, after_but_yesno = (math.sin(zzmove_xy / 30) * 2000 * 0.875), \
                                                   (math.sin(zzmove_xy / 30) * -2000 * 0.875), \
                                                   (math.sin(zzmove_xy / 30) * 2000 / 25)
            zzmove_xy, clo = 0, 2
            anima = 0

    # Настройка обратной анимации yes / no
    if clo == 3:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
        else:
            after_yes, after_no, after_but_yesno = 0, 0, 0
            zzmove_xy, clo = 0, 0
            anima = 0

    # Отрисовка Yes / no
    if clo == 2 and okno < 1:
        screen.blit(Yes, (after_yes - 1200, height / 2 - 10 + const))
        screen.blit(No, (after_no + 300 + width, height / 2 - 135 - 10 + const))
        if anima == 0:
            yes_button.paint(after_yes + 94 - 1200,
                             height / 2 + 15 + const, button_sound, 0, 0, 'yes', action=close_game)
            yes_button.paint(after_no + 329 + width,
                             height / 2 - 145 + 27 + const, button_sound, 0, 0, 'no', action=close_window)

    # Выдвижение настроек
    if okno == -1:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            sett_anima(zzmove_xy, True)
        else:
            after_but, after_but4 = (math.sin(zzmove_xy / 30) * 2000 / 25), math.sin(zzmove_xy / 30) * 2000 * 0.875
            after_but2, after_but3 = (math.sin(zzmove_xy / 60) * 4000), (math.sin(zzmove_xy / 450) * 1000)
            zzmove_xy, anima = 0, 0
            okno = -2

    # Обратная анимация настроек
    if okno == -3 and clo != 1 and clo != 3:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            sett_anima(zzmove_xy, False)
        else:
            after_but, after_but2, after_but3, after_but4, zzmove_xy, okno, anima = [0 for i in range(7)]

    # Маленькая кнопка назад
    if okno == 2 and clo != 1 and clo != 3:
        back_button.paint(width - 350, 110, button_sound, -10, 0, 'mini_scroll', action=scroll)
        pass

    # Анимация перехода вверх / вниз
    if clo != 1 and clo != 3:
        if okno == 1:
            lobby_anima(True)

        elif okno == -10:
            lobby_anima(False)

    # Примечание
    if develz == 1:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            dev_anima(zzmove_xy, True)
        else:
            after_dev, develz, after_place = - math.sin(zzmove_xy / 30) * 2000, 2, - math.sin(zzmove_xy / 30) * 2000
            zzmove_xy, anima = 0, 0

    elif develz == 3:
        anima = 1
        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            dev_anima(zzmove_xy, False)
        else:
            after_dev, develz, after_place = 0, 0, 0
            zzmove_xy, anima = 0, 0

    if develz == 2 and zzmove_xy == 0 and okno != 0:
        screen.blit(Development, (width / 4 - 100, height / 2 - const + after_dev + 1870))
        if anima == 0:
            Devel_butt.paint(width / 4 + 134, height / 2 - const + after_dev + 1870 + 72,
                                button_sound, False, 0, 'back_devel', action=devel)

    # Кнопки меню выбора между сервером и одиночной игрой
    if (okno == 2 or okno == 3) and clo != 1 and clo != 3:
        if develz == 0:
            screen.blit(placebutton3_1, (width / 4, height / 4 + const))
            screen.blit(single_button, (width / 4 + 39, height / 4 + 62 + const))
            screen.blit(placebutton3_2, (width / 4, height / 4 + const))
        screen.blit(placebutton3_1, (width / 5 * 3, height / 4 + const))
        screen.blit(server_button, (width / 5 * 3 + 39, height / 4 + 62 + const))
        screen.blit(placebutton3_2, (width / 5 * 3, height / 4 + const))

        # Отображение маленькой кнопки назад
        screen.blit(Mini_back, (width - 350, 110))

        if anima == 0:
            if develz == 0:
                Single_button.paint(width / 4 + 39,
                                    height / 4 + 62 + const, button_sound, True, 0, 'devel', action=devel)
            Server_button.paint(width / 5 * 3 + 39,
                                height / 4 + 62 + const, button_sound, 0, 0, 'scrolling', action=scrolling)
            back_button.paint(width - 350, 110, button_sound, -10, 0, 'mini_scroll', action=scroll)

    # Отрисовка меню
    if (okno == 0 or okno == -2) and clo != 1 and clo != 3:
        screen.blit(placebutton1_1, (width / 2 - 316 + after_but_yesno,
                                     height / 7 * 2 - 21 - 120 - after_but + const))
        screen.blit(play_button, (width / 2 - 75 + after_but_yesno,
                                  height / 7 * 2 - 120 - after_but + const))
        screen.blit(placebutton1_2, (width / 2 - 316 + after_but_yesno,
                                     height / 7 * 2 - 21 - 120 - after_but + const))
        screen.blit(placebutton1_1, (width / 2 - 316 + after_but_yesno,
                                     height / 7 * 5.2 - 21 - 120 + after_but + const))
        screen.blit(exit_button, (width / 2 - 75 + after_but_yesno,
                                  height / 7 * 5.2 - 120 + after_but + const))
        screen.blit(placebutton1_2, (width / 2 - 316 + after_but_yesno,
                                     height / 7 * 5.2 - 21 - 120 + after_but + const))

        # Отрисовка настроек
        if okno == -2:
            screen.blit(setting_menu, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if getresol() == '1920':
                screen.blit(resolition1, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(resolition2, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if bk == 0:
                screen.blit(sett_background1, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 1:
                screen.blit(sett_background2, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 2:
                screen.blit(sett_background3, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif bk == 3:
                screen.blit(sett_background4, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(sett_background5, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if songs_id == 0:
                screen.blit(Forest_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            elif songs_id == 1:
                screen.blit(On_call_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))
            else:
                screen.blit(Fortress_songs, (1750 - 900 + after_but_yesno, height / 2 / 1.7 + const))

            if anima == 0:
                Back_background.paint(width / 7 * 3.21 + after_but_yesno,
                                      height / 1.98 + const, button_sound, 1, 0, 'back', action=back)
                Next_background.paint(width / 7 * 3.832 + after_but_yesno,
                                      height / 1.98 + const, button_sound, 1, 0, 'next', action=next)
                Back_songs.paint(width / 7 * 3.265 + after_but_yesno,
                                 height / 2.33 + const, button_sound, 2, 0, 'back', action=back)
                Next_songs.paint(width / 7 * 3.785 + after_but_yesno,
                                 height / 2.33 + const, button_sound, 2, 0, 'next', action=next)
                Back_resolition.paint(width / 7 * 3.265 + after_but_yesno,
                                      height / 2.64 + const, button_sound, 3, 0, 'back', action=back)
                Next_resolition.paint(width / 7 * 3.785 + after_but_yesno,
                                      height / 2.64 + const, button_sound, 3, 0, 'next', action=next)

                Back_sett.paint(width / 7 * 3.294 + after_but_yesno,
                                height / 1.7 + const, button_sound, 0, 0, 'back_setts', action=back_setts)

            # Иначе отрисовка обычной кнопки настроек
        else:
            screen.blit(placebutton2_2, (width / 2 - 132 + after_but_yesno,
                                         height / 7 * 3.6 - 26 - 120 + after_but + const))
            screen.blit(setting_button, (width / 2 - 75 + after_but_yesno,
                                         height / 7 * 3.6 - 120 + after_but + const))
            screen.blit(placebutton2_1, (width / 2 - 132 + after_but_yesno,
                                         height / 7 * 3.6 - 26 - 120 + after_but + const))

            if anima == 0:
                scroll_button.paint(width / 2 - 75 + after_but_yesno, height / 7 * 2 - 120 - after_but / 1.9 + const,
                                    button_sound, 1, 0, 'scroll', action=scroll)

                Exit_button.paint(width / 2 - 75 + after_but_yesno, height / 7 * 5.2 - 120 + after_but + const,
                                  button_sound, 0, 0, 'close_window', action=close_window)
                Setting_button.paint(width / 2 - 75 + after_but_yesno,
                                     height / 7 * 3.6 - 120 + const, button_sound, 0, 0, 'setts', action=setts)

    # Иначе отрисовка yes / no
    else:
        if clo == 1:
            yesno(zzmove_xy, True)
        elif clo == 3:
            yesno(zzmove_xy, False)


    # Включает игру
    if getSerb() == 1:
        okno = 5

    # Отрисовка поля боя
    if okno == 5 and clo != 1 and clo != 3:
        anima = 1
        if getresol() == '1920':
            screen.blit(place_image, [0, -30])
        else:
            screen.blit(place_image_1440, [240, 60])
        blit_place()

        if zzmove_xy <= math.pi * 15:
            zzmove_xy += 1
            # chose_anima(zzmove_xy, True)
        else:
            zzmove_xy = 0

        if zzzmove_xy <= math.pi * 15:
            zzzmove_xy += 1
            # check_anima(zzzmove_xy, True, 'white', 0)
        else:
            zzzmove_xy = 0

        # Подсветка
        if hod == 1:
            if getShah() == 0:
                for y1 in range(8):
                    for x1 in range(8):
                        if fig.coord() != [x1, y1]:
                            blik = con(fig, x1, y1, getClr(),phant)
                            stroke()

            elif getShah() == 1:
                for y1 in range(8):
                    for x1 in range(8):
                        if fig.coord() != [x1, y1]:
                            king_coord = getShahCoord()
                            blik = shahcon(getShahfig(), king_coord[0], king_coord[1], fig, x1, y1, getClr(),phant)
                            stroke()
        print_chess()

        if okno == 5 and zmove_xy <= math.pi * 6:
            zmove_xy += 1

            # screen.blit(go, (-(math.cos(zmove_xy / 12) * 2300) - 300, 0))

    if getChcd():
        if getChClr() == getClr():
            chose_anima(True, chX, chY, chKey)
        else:
            chose_anima(True, 0, 0, '0')

    if load == 1:
        fig.movement_pict()

    # Переход к залу ожидания
    if okno == 3 or okno == 4:
        if okno == 3 and zzzmove_xy <= math.pi * 6:
            zzzmove_xy += 1
            screen.blit(go, (-(math.sin(zzzmove_xy / 12) * 2300) + 1920, 0))
        else:
            screen.blit(go, (-300, 0))
            zzzmove_xy = 0
            okno = 4

    # Зал ожидания
    if okno == 4:
        if zzmove_xy == 0:
            createpotok()

        zzmove_xy += 1
        screen.blit(player_button, (width / 9 * 3.2, height / 2.5))
        screen.blit(pk_button, (width / 9 * 5.2, height / 2.5))
        for nums, i in enumerate([0, 1, 2]):
            screen.blit(runs[i - zzmove_xy // 4 % 3], (width / 9 * (4.03 + nums * 0.3), height / 2.5 + 17))

    # Кнопка звука
    if song_turn:
        screen.blit(Mini_song_off, (width - 295, 110))
        pass
    else:
        screen.blit(Mini_song_on, (width - 295, 110))
        pass
    turn_button.paint(width - 295, 110, button_sound, 0, 0, 'turn', action=turn_song)

    if okno < 1:
        if getresol() == '1920':
            screen.blit(Authorship, (width - 445, height - 55))
        else:
            screen.blit(Authorship, (width - width / 3, height - height / 6.5))

    if getPh() == 1:
        phant = getPhFig()
    else:
        phant = Pawn(-10000,-10000, 'NoColor')

    # Конец цикла
    clock.tick(60)
    pygame_widgets.update(events)
    pygame.display.update()
