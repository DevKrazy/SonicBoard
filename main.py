from drivers import LCD
from utils import defcom
from sound import sound_profile
from time import sleep
from pythonosc import osc_message_builder, udp_client
from utils import xboxController
import pygame

# ports
BUTTON_LEFT = 7
BUTTON_RIGHT = 8
POT = 0

# initialisation
pygame.init()
controller_count = pygame.joystick.get_count()
pygame.display.set_mode((1, 1))

# LCD init
LCD.init_screen()
LCD.set_color(0xFF, 0x00, 0xFF)

# checks if the controller is connected
if controller_count == 0:
    LCD.set_text("Connectez la\nmanette :(")

while controller_count == 0:
    pygame.quit()
    sleep(2)
    pygame.init()
    controller_count = pygame.joystick.get_count()

controller = xboxController.Controller()
LCD.set_text("C'est bon :)")
sleep(2)

defcom.pinMode(BUTTON_LEFT, "INPUT")
defcom.pinMode(BUTTON_RIGHT, "INPUT")
defcom.pinMode(POT, "INPUT")

# variables
done = False
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
# previous buttons states
previous_left_button_state = defcom.digitalRead(BUTTON_LEFT)
previous_right_button_state = defcom.digitalRead(BUTTON_RIGHT)
prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left, prev_lt, prev_rt = (0, 0, 0, 0, 0, 0)

LCD.display_main_menu()

prev_left_x, prev_left_y, prev_right_x, prev_right_y = (False, False, False, False)


def leftJoystick(left_x, left_y, right_x, right_y, prev_left_x, prev_left_y):
    if left_x >= 0.7 and not prev_left_x:
        sender.send_message('/button', sound_profile.get_full_path() + "ljoy_right" + '.wav')
        prev_left_x = True

    if left_x <= -0.7 and not prev_left_x:
        sender.send_message('/button', sound_profile.get_full_path() + "ljoy_left" + '.wav')
        prev_left_x = True
    if left_y >= 0.7 and not prev_left_y:
        sender.send_message('/button', sound_profile.get_full_path() + "ljoy_up" + '.wav')
        prev_left_y = True
    if left_y <= -0.7 and not prev_left_y:
        sender.send_message('/button', sound_profile.get_full_path() + "ljoy_down" + '.wav')
        prev_left_y = True

    return [prev_left_x, prev_left_y]


prev_volume = defcom.analogRead(POT)
while not done:
    volume = defcom.analogRead(POT)
    if 5 <= abs(volume - prev_volume) <= 100:
        sender.send_message('/vol', volume / 1023)
        print(volume)
    # current buttons state
    current_left_button_state = defcom.digitalRead(BUTTON_LEFT)
    current_right_button_state = defcom.digitalRead(BUTTON_RIGHT)
    pad_up, pad_right, pad_down, pad_left = controller.get_pad()  # On récupère les croix directionnelles(1 si appuyé, 0 sinon)

    # joysticks current state
    left_x, left_y = controller.get_left_stick()
    right_x, right_y = controller.get_right_stick()
    [prev_left_x, prev_left_y] = leftJoystick(left_x, left_y, right_x, right_y, prev_left_x, prev_left_y)

    triggers = controller.get_triggers()  # Les valeurs analogiques des gachettes
    if triggers >= -0.5 and prev_lt:
        prev_lt = 0
    if triggers <= 0.5 and prev_rt:
        prev_rt = 0

    for event in pygame.event.get():  # On récupère les boutons avec un évènement pygame
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            # On récupère le numéro du bouton envoyé par pygame
            if event.button == xboxController.BACK:
                sender.send_message('/echo', 1)
            elif event.button == xboxController.START:
                sender.send_message('/rev', 1)
            else:
                sender.send_message('/button', sound_profile.get_full_path() + str(event.button) + '.wav')

    # triggers computing
    #triggers is only 1 value for both triggers (negative is left, positive is right)
    if triggers <= -0.8 and not prev_lt:
        sender.send_message('/button', sound_profile.get_full_path() + "lt" + '.wav')
        prev_lt = 1
    elif triggers >= 0.8 and not prev_rt:
        prev_rt = 1
        sender.send_message('/button', sound_profile.get_full_path() + "rt" + '.wav')


    # joystick management
    if right_x <= - 0.1 or right_x >= 0.1: #deadzone
        if right_x <= -0.5:
            sender.send_message('/rate', -1) #reverse sound
        # TODO joystick a droite
        prev_right_x = True
    elif prev_right_x:
        sender.send_message('/rate', 1) #normal rate (pitch) value
        prev_right_x = False

    if right_y <= - 0.1 or right_y >= 0.1:
        if right_y <= -0.1:
            sender.send_message('/rate', right_y * -3) #analog pitch value
        elif right_y <= 0.9:
            sender.send_message('/rate', 1 - right_y)
        else:
            sender.send_message('/rate', 0.1) #minimum pitch value
        prev_right_y = True
    elif prev_right_y:
        sender.send_message('/rate', 1)
        prev_right_y = False

    # pad computing
    if pad_up and not prev_pad_up:  # pour ne pas avoir deux fois l'input si on laisse appuyé
        sender.send_message('/button', sound_profile.get_full_path() + "up" + '.wav')
    if pad_down and not prev_pad_down:
        sender.send_message('/button', sound_profile.get_full_path() + "down" + '.wav')
    if pad_left and not prev_pad_left:
        sender.send_message('/button', sound_profile.get_full_path() + "left" + '.wav')
    if pad_right and not prev_pad_right:
        sender.send_message('/button', sound_profile.get_full_path() + "right" + '.wav')

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
    prev_volume = volume

    prev_pad_up, prev_pad_right, prev_pad_down, prev_pad_left = (
    pad_up, pad_right, pad_down, pad_left)  # on enregistre la valeur du dpad en fin de boucle
    if left_x >= -0.1 and left_x <= 0.1: #if left joystick not used, storing that they are not used
        prev_left_x = False
    if left_y >= -0.1 and left_y <= 0.1:
        prev_left_y = False

    sleep(0.01)  # refresh rate

pygame.quit()
