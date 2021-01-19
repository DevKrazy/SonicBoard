from drivers import LCD
from utils import defcom
from sound import sound_profile
from time import sleep
from sound import sound_player, sound_profile
from pythonosc import osc_message_builder, udp_client
from utils import xboxController
import pygame

# ports
BUTTON_LEFT = 7
BUTTON_RIGHT = 8
POT = 0

# initialisation
pygame.init()
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
controller = xboxController.Controller()

defcom.pinMode(BUTTON_LEFT, "INPUT")
defcom.pinMode(BUTTON_RIGHT, "INPUT")
defcom.pinMode(POT, "INPUT")

# current profile's id
profile_id = 0
done = False

########## TEST #########
LCD.init_screen()
LCD.set_color(0xFF, 0x00, 0xFF)
#LCD.display_main_menu()
SOUND_ASSETS_PATH = '/home/pi/Desktop/SonicThomas/sound_assets/'
profile_folder = "drum/" #TODO remplacer par la gestion de profil

######### END ###########


# previous buttons states
previous_left_button_state = defcom.digitalRead(BUTTON_LEFT)
previous_right_button_state = defcom.digitalRead(BUTTON_RIGHT)
prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left, prev_lt, prev_rt = (0, 0, 0, 0, 0, 0)

while not done:

    # current buttons states
    current_left_button_state = defcom.digitalRead(BUTTON_LEFT)
    current_right_button_state = defcom.digitalRead(BUTTON_RIGHT)
    pad_up, pad_right, pad_down, pad_left = controller.get_pad()  # On récupère les croix directionnelles(1 si appuyé, 0 sinon)
    triggers = controller.get_triggers()  # Les valeurs analogiques des gachettes
    # Les valeurs analogiques des joysticks
    left_x, left_y = controller.get_left_stick()
    right_x, right_y = controller.get_right_stick()

    for event in pygame.event.get(): #On récupère les boutons avec un évènement pygame
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            # On récupère le numéro du bouton envoyé par pygame
            sender.send_message('/button', sound_profile.get_full_path() + str(event.button) + '.wav')

    if triggers <= -0.8 and not prev_lt:
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')
        prev_lt = 1
    elif triggers >= 0.8 and not prev_rt:
        prev_rt = 1
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')
    if pad_up and not prev_pad_up:
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')
    if pad_down and not prev_pad_down:
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')
    if pad_left and not prev_pad_left:
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')
    if pad_right and not prev_pad_right:
        sender.send_message('/button', sound_profile.get_full_path() + '.wav')

    # profile buttons computing
    if previous_left_button_state != current_left_button_state and current_left_button_state == 1:
        # left button was pressed
        sound_profile.previous_profile()
        LCD.display_main_menu()
    elif previous_right_button_state != current_right_button_state and current_right_button_state == 1:
        # right button was pressed
        sound_profile.next_profile()
        LCD.display_main_menu()

    # current buttons state becomes the previous state for the next loop iteration
    previous_left_button_state = current_left_button_state
    previous_right_button_state = current_right_button_state
    prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left = (pad_up, pad_right, pad_down, pad_left)
    # TODO gestion des autres inputs (joysticks etc...)

    sleep(0.05)  #refresh rate

