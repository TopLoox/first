import pygame

pygame.init()

# изображения
stroke = pygame.image.load("Image/Blackout_place.png")
stroke2 = pygame.image.load("Image/Blackout_place2.png")
stroke3 = pygame.image.load("Image/Blackout_place3.png")
stroke4 = pygame.image.load("Image/Blackout_button.png")
stroke5 = pygame.image.load("Image/Blackout_button2.png")
stroke_1440 = pygame.image.load("Image/Blackout_place_1440.png")
stroke2_1440 = pygame.image.load("Image/Blackout_place2_1440.png")
stroke3_1440 = pygame.image.load("Image/Blackout_place3_1440.png")
Mini_stroke = pygame.image.load('Image/Mini_blackout.png')
lobby_image = pygame.image.load('Image/new_lobby2.png')
background11 = pygame.image.load('Image/background.png')
background12 = pygame.image.load('Image/background2.png')
background13 = pygame.image.load('Image/background3.png')
background14 = pygame.image.load('Image/background4.png')
background15 = pygame.image.load('Image/background5.png')
background21 = pygame.image.load('Image/background_1440.png')
background22 = pygame.image.load('Image/background2_1440.png')
background23 = pygame.image.load('Image/background3_1440.png')
background24 = pygame.image.load('Image/background4_1440.png')
background25 = pygame.image.load('Image/background5_1440.png')
place_image = pygame.image.load('Image/place.png')
place_image_1440 = pygame.image.load('Image/place_1440.png')
placebutton1_1 = pygame.image.load('Image/placebutton1-1.png')
placebutton1_2 = pygame.image.load('Image/placebutton1-2.png')
placebutton2_1 = pygame.image.load('Image/placebutton2-1.png')
placebutton2_2 = pygame.image.load('Image/placebutton2-2.png')
placebutton3_1 = pygame.image.load('Image/placebutton3-1.png')
placebutton3_2 = pygame.image.load('Image/placebutton3-2.png')
play_button = pygame.image.load('Image/play.png')
exit_button = pygame.image.load('Image/Exit.png')
server_button = pygame.image.load('Image/server.png')
single_button = pygame.image.load('Image/single.png')
setting_button = pygame.image.load('Image/settings.png')
da_screen = pygame.image.load('Image/da3.png')
da2_screen = pygame.image.load('Image/da2.png')
go = pygame.image.load('Image/go.png')
player_button = pygame.image.load('Image/player.png')
pk_button = pygame.image.load('Image/pk.png')
resolition1 = pygame.image.load('Image/1920_1080.png')
resolition2 = pygame.image.load('Image/1440_900.png')
setting_menu = pygame.image.load('Image/settings_menu.png')
sett_background1 = pygame.image.load('Image/setting_background1.png')
sett_background2 = pygame.image.load('Image/setting_background2.png')
sett_background3 = pygame.image.load('Image/setting_background3.png')
sett_background4 = pygame.image.load('Image/setting_background4.png')
sett_background5 = pygame.image.load('Image/setting_background5.png')
Choice_place = pygame.image.load('Image/Choice_place.png')
Choice_white = pygame.image.load('Image/Choice_white.png')
Choice_black = pygame.image.load('Image/Choice_black.png')
CheckBlack = pygame.image.load('Image/CheckBlack.png')
CheckmateBlack = pygame.image.load('Image/CheckmateBlack.png')
CheckWhite = pygame.image.load('Image/CheckWhite.png')
CheckmateWhite = pygame.image.load('Image/CheckmateWhite.png')
Choice_place_1440 = pygame.image.load('Image/Choice_place_1440.png')
Choice_white_1440 = pygame.image.load('Image/Choice_white_1440.png')
Choice_black_1440 = pygame.image.load('Image/Choice_black_1440.png')
CheckBlack_1440 = pygame.image.load('Image/CheckBlack_1440.png')
CheckmateBlack_1440 = pygame.image.load('Image/CheckmateBlack_1440.png')
CheckWhite_1440 = pygame.image.load('Image/CheckWhite_1440.png')
CheckmateWhite_1440 = pygame.image.load('Image/CheckmateWhite_1440.png')
choice = pygame.image.load('Image/Choice.png')
Authorship = pygame.image.load('Image/Authorship.png')
Yes = pygame.image.load('Image/Yes.png')
No = pygame.image.load('Image/No.png')
Mini_back = pygame.image.load('Image/Mini_back.PNG')
Mini_exit = pygame.image.load('Image/Mini_exit.PNG')
Mini_song_off = pygame.image.load('Image/Mini_song_off.PNG')
Mini_song_on = pygame.image.load('Image/Mini_song_on.png')
Fortress_songs = pygame.image.load('Image/fortress_songs.png')
Forest_songs = pygame.image.load('Image/forest_songs.png')
On_call_songs = pygame.image.load('Image/on_call_songs.png')
Development = pygame.image.load('Image/Development.png')
Finish = pygame.image.load('Image/finish.png')
Black_finish = pygame.image.load('Image/black_finish.png')
White_finish = pygame.image.load('Image/white_finish.png')

run1 = pygame.image.load('Image/run1.png')
run2 = pygame.image.load('Image/run2.png')
run3 = pygame.image.load('Image/run3.png')
runs = [run1, run2, run3]

white_pawn = pygame.image.load('Image/White_Pawn.png')
white_pawn_1440 = pygame.image.load('Image/White_Pawn_1440.png')
black_pawn = pygame.image.load('Image/Black_Pawn.png')
black_pawn_1440 = pygame.image.load('Image/Black_Pawn_1440.png')
white_horse = pygame.image.load('Image/White_Horse.png')
white_horse_1440 = pygame.image.load('Image/White_Horse_1440.png')
black_horse = pygame.image.load('Image/Black_Horse.png')
black_horse_1440 = pygame.image.load('Image/Black_Horse_1440.png')
white_elephant = pygame.image.load('Image/White_Elephant.png')
white_elephant_1440 = pygame.image.load('Image/White_Elephant_1440.png')
black_elephant = pygame.image.load('Image/Black_Elephant.png')
black_elephant_1440 = pygame.image.load('Image/Black_Elephant_1440.png')
white_castle = pygame.image.load('Image/White_Castle.png')
white_castle_1440 = pygame.image.load('Image/White_Castle_1440.png')
black_castle = pygame.image.load('Image/Black_Castle.png')
black_castle_1440 = pygame.image.load('Image/Black_Castle_1440.png')
white_queen = pygame.image.load('Image/White_Queen.png')
white_queen_1440 = pygame.image.load('Image/White_Queen_1440.png')
black_queen = pygame.image.load('Image/Black_Queen.png')
black_queen_1440 = pygame.image.load('Image/Black_Queen_1440.png')
white_king = pygame.image.load('Image/White_King.png')
white_king_1440 = pygame.image.load('Image/White_King_1440.png')
black_king = pygame.image.load('Image/Black_King.png')
black_king_1440 = pygame.image.load('Image/Black_King_1440.png')


# звуки и музыка
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
place_sound = pygame.mixer.Sound('Sounds/place.mp3')
forest_songs = pygame.mixer.Sound('Sounds/forest.mp3')
fortress_songs = pygame.mixer.Sound('Sounds/fortress.mp3')
on_call_songs = pygame.mixer.Sound('Sounds/on_call.mp3')

# корректировка размеры доски / длины / ширины
moment, poss = 0, [0, 0, 0]
resolition = '1920'
after_coord = {'lower': {1: (137, 544), 2: (247, 544), 3: (357, 544), 4: (137, 654), 5: (247, 654)},
               'upper': {1: (137, 160), 2: (247, 160), 3: (357, 160), 4: (137, 270), 5: (247, 270)}}


def getposs():
    global poss
    return poss


def setresol():
    global resolition, poss
    if resolition == '1920':
        resolition, poss = '1440', [22.5, -97, -90]
    else:
        resolition, poss = '1920', [0, 0, 0]


def getresol():
    global resolition
    return resolition


def setmoment():
    global moment
    moment += 1


def getmoment():
    global moment
    return moment
