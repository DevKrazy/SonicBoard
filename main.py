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
profile_folder = "memes/" #TODO remplacer par la gestion de profil

done = False
prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left = (0,0,0,0) #Utile pour ne pas enregistrer plusieurs inputs quand on laisse appuyé

while not done:
    pad_up, pad_right, pad_down, pad_left = controller.get_pad() #On récupère les croix directionnelles(1 si appuyé, 0 sinon)
    triggers = controller.get_triggers() #Les valeurs analogiques des gachettes
    left_x, left_y = controller.get_left_stick() #Les valeurs analogiques des joysticks
    right_x, right_y = controller.get_right_stick()
    #print(controller.get_right_stick())
    #print(controller.get_left_stick())
    #print(triggers)

    for event in pygame.event.get(): #On récupère les boutons avec un évènement pygame
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.JOYBUTTONDOWN:
            #if event.button == xboxController.A:
                #print("a")

            #print(event.button)

            #On récupère le numéro du bouton envoyé par pygame
            sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + str(event.button) + '.wav')
            #print('/button', SOUND_ASSETS_PATH + profile_folder + str(event.button) + '.wav')

    if pad_up and not prev_pad_up: #pour ne pas avoir deux fois l'input si on laisse appuyé
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "up" + '.wav')
    if pad_down and not prev_pad_down:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "down" + '.wav')
    if pad_left and not prev_pad_left:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "left" + '.wav')
    if pad_right and not prev_pad_right:
        sender.send_message('/button', SOUND_ASSETS_PATH + profile_folder + "right" + '.wav')

    prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left = (pad_up, pad_right, pad_down, pad_left) #on enregistre la valeur du dpad en fin de boucle
    sleep(0.2)  # joycon refresh rate
