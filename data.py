import pygame

pygame.init()

# изображения
stroke = pygame.image.load("Image/Blackout_place.png")
stroke2 = pygame.image.load("Image/Blackout_place2.png")
stroke3 = pygame.image.load("Image/Blackout_place3.png")
stroke4 = pygame.image.load("Image/Blackout_button.png")
stroke5 = pygame.image.load("Image/Blackout_button2.png")
close_paint = pygame.image.load('Image/close(30x30).jpg')
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
clo_window = pygame.image.load('Image/closeind.jpg')
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
choice_place = pygame.image.load('Image/Choice_place.png')
Choice_white = pygame.image.load('Image/Choice_white.png')
Choice_black = pygame.image.load('Image/Choice_black.png')
CheckBlack = pygame.image.load('Image/CheckBlack.png')
CheckmateBlack = pygame.image.load('Image/CheckmateBlack.png')
CheckWhite = pygame.image.load('Image/CheckWhite.png')
CheckmateWhite = pygame.image.load('Image/CheckmateWhite.png')
choice = pygame.image.load('Image/Choice.png')
Authorship = pygame.image.load('Image/Authorship.png')

run1 = pygame.image.load('Image/run1.png')
run2 = pygame.image.load('Image/run2.png')
run3 = pygame.image.load('Image/run3.png')
runs = [run1, run2, run3]

white_pawn = pygame.image.load('Image/White_Pawn.png')
black_pawn = pygame.image.load('Image/Black_Pawn.png')
white_horse = pygame.image.load('Image/White_Horse.png') 
black_horse = pygame.image.load('Image/Black_Horse.png')
white_elephant = pygame.image.load('Image/White_Elephant.png') 
black_elephant = pygame.image.load('Image/Black_Elephant.png')
white_castle = pygame.image.load('Image/White_Castle.png') 
black_castle = pygame.image.load('Image/Black_Castle.png')
white_queen = pygame.image.load('Image/White_Queen.png') 
black_queen = pygame.image.load('Image/Black_Queen.png')
white_king = pygame.image.load('Image/White_King.png') 
black_king = pygame.image.load('Image/Black_King.png')



# звуки
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
place_sound = pygame.mixer.Sound('Sounds/place.mp3')

moment = 0
after_coord = {'lower': {1: (137, 544), 2: (247, 544), 3: (357, 544), 4: (137, 654), 5: (247, 654)},
               'upper': {1: (137, 160), 2: (247, 160), 3: (357, 160), 4: (137, 270), 5: (247, 270)}}

def setmoment():
    global moment
    moment += 1

def getmoment():
    global moment
    print(moment)
    return moment