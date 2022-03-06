import pygame

pygame.init()

# изображения
stroke = pygame.image.load("Image/Blackout_place.png")
close_paint = pygame.image.load('Image/close(30x30).jpg')
lobby_image = pygame.image.load('Image/new_lobby2.png')
background11 = pygame.image.load('Image/background.png')
background12 = pygame.image.load('Image/background2.png')
background13 = pygame.image.load('Image/background3.png')
background21 = pygame.image.load('Image/background_1440.png')
background22 = pygame.image.load('Image/background2_1440.png')
background23 = pygame.image.load('Image/background3_1440.png')
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
run1 = pygame.image.load('Image/run1.png')
run2 = pygame.image.load('Image/run2.png')
run3 = pygame.image.load('Image/run3.png')
runs = [run1, run2, run3]

# звуки
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
place_sound = pygame.mixer.Sound('Sounds/place.mp3')

moment = 0
after_coord = 1