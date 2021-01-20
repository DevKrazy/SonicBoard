from sound import sound_player, sound_profile
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client
from utils import xboxController
import pygame

SOUND_ASSETS_PATH = '/home/pi/Desktop/SonicThomas/sound_assets/'
pygame.init()
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
controller = xboxController.Controller()
# TEST

# current profile's id
profile_id = 0
profile_folder = "drum/" #TODO remplacer par la gestion de profil

done = False
prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left, prev_lt,prev_rt = (0,0,0,0,0,0) #Utile pour ne pas enregistrer plusieurs inputs quand on laisse appuyé

prev_left_x, prev_left_y, prev_right_x, prev_right_y = (False, False, False, False)


def leftJoystick(left_x, left_y, right_x, right_y, prev_left_x, prev_left_y):
    if left_x >= 0.7 and not prev_left_x:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "ljoy_right" + '.wav')
        prev_left_x = True
        print("dd")
    if left_x <= -0.7 and not prev_left_x:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "ljoy_left" + '.wav')
        prev_left_x = True
    if left_y >= 0.7 and not prev_left_y:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "ljoy_up" + '.wav')
        prev_left_y = True
    if left_y <= -0.7 and not prev_left_y:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "ljoy_down" + '.wav')
        prev_left_y = True

    return [prev_left_x, prev_left_y]


while not done:
    pad_up, pad_right, pad_down, pad_left = controller.get_pad() #On récupère les croix directionnelles(1 si appuyé, 0 sinon)
    triggers = controller.get_triggers() #Les valeurs analogiques des gachettes
    left_x, left_y = controller.get_left_stick() #Les valeurs analogiques des joysticks
    right_x, right_y = controller.get_right_stick()

    if triggers >= -0.5 and prev_lt :
        prev_lt = 0
    if triggers <= 0.5 and prev_rt :
        prev_rt = 0
    for event in pygame.event.get(): #On récupère les boutons avec un évènement pygame
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == xboxController.BACK:
                sender.send_message('/echo', 1)
            else:
                sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + str(event.button) + '.wav')

    if triggers <= -0.8 and not prev_lt:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "lt" + '.wav')
        prev_lt = 1
    elif triggers >= 0.8 and not prev_rt:
        prev_rt = 1
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "rt" + '.wav')


    [prev_left_x, prev_left_y] = leftJoystick(left_x, left_y, right_x, right_y, prev_left_x, prev_left_y)

    if right_x <= - 0.1 or right_x >= 0.1:
        if right_x <= -0.5:
            sender.send_message('/rate', -1)
        # TODO joystick a droite
        prev_right_x = True
    elif prev_right_x :
        sender.send_message('/rate', 1)
        prev_right_x = False

    if right_y <= - 0.1 or right_y >= 0.1:
        if right_y <= -0.1:
            sender.send_message('/rate', right_y * -5)
        elif right_y <= 0.9:
            sender.send_message('/rate', 1 - right_y)
        else :
            sender.send_message('/rate', 0.1)

        prev_right_y = True
    elif prev_right_y :
        sender.send_message('/rate', 1)
        prev_right_y = False

    if pad_up and not prev_pad_up: #pour ne pas avoir deux fois l'input si on laisse appuyé
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "up" + '.wav')
    if pad_down and not prev_pad_down:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "down" + '.wav')
    if pad_left and not prev_pad_left:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "left" + '.wav')
    if pad_right and not prev_pad_right:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "right" + '.wav')

    prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left = (pad_up, pad_right, pad_down, pad_left) #on enregistre la valeur du dpad en fin de boucle
    if left_x >= -0.1 and left_x <= 0.1 :
        prev_left_x = False
    if left_y >= -0.1 and left_y <= 0.1 :
        prev_left_y = False

    sleep(0.01)  #refresh rate



pygame.quit()