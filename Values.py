from data import *

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

move_xy, zmove_xy, zzmove_xy, zzzmove_xy, move, after, \
    after_but, after_but2, after_but3, after_but4, after_yes, \
    after_no, after_but_yesno, after_buts, after_da, after_dev, after_place, after_dev2 = [0 for _ in range(18)]
okno, clo, leg, sc, game, hod, fig, load, key, bk, moment, \
    songs_id, song_turn, back_lobby, develz, anima = [0 for _ in range(16)]

const = 20

lobbyrect = lobby_image.get_rect()
lobbyrect = lobbyrect.move([-75, 3120 + lobbyrect[1]])

backgrounds = {'1920': [background11, background12, background13, background14, background15],
               '1440': [background21, background22, background23, background24, background25]}

songs = [forest_songs, on_call_songs, fortress_songs]

Checks = {'1920': {'white': [CheckWhite, CheckmateWhite], 'black': [CheckBlack, CheckmateBlack]},
          '1440': {'white': [CheckWhite_1440, CheckmateWhite_1440],
                   'black': [CheckBlack_1440, CheckmateBlack_1440]}}

Сhoses = {'1920': {'white': [Choice_white, Choice_black], 'black': [Choice_white, Choice_black]},
          '1440': {'white': [Choice_white_1440, Choice_black_1440],
                   'black': [Choice_white_1440, Choice_black_1440]}}