import pygame

pygame.init()

# изображения
close_paint = pygame.image.load('Image/close(30x30).jpg')
lobby_image = pygame.image.load('Image/new_lobby2.png')
fight_image = pygame.image.load('Image/background.png')
clo_window = pygame.image.load('Image/closeind.jpg')
place_image = pygame.image.load('Image/place.png')
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
run1 = pygame.image.load('Image/run1.png')
run2 = pygame.image.load('Image/run2.png')
run3 = pygame.image.load('Image/run3.png')
runs = [run1, run2, run3]

# звуки
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
place_sound = pygame.mixer.Sound('Sounds/place.mp3')
