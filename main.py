import LCD
from utils import defcom
from inputs import joycon_inputs
from sound import sound_profile

from time import sleep

# ports
BUTTON_LEFT = 7
BUTTON_RIGHT = 8
POT = 0

# pin modes
defcom.pinMode(BUTTON_LEFT, "INPUT")
defcom.pinMode(BUTTON_RIGHT, "INPUT")
defcom.pinMode(POT, "INPUT")

########## TEST #########
LCD.init_screen()
LCD.set_color(0xFF, 0x00, 0x00)
LCD.display_main_menu()
######### END ###########

# previous buttons states
previous_joycon_buttons_state = joycon_inputs.get_buttons_state()
previous_left_button_state = defcom.digitalRead(BUTTON_LEFT)
previous_right_button_state = defcom.digitalRead(BUTTON_RIGHT)

while True:
    # current buttons states
    current_joycon_buttons_state = joycon_inputs.get_buttons_state()
    current_left_button_state = defcom.digitalRead(BUTTON_LEFT)
    current_right_button_state = defcom.digitalRead(BUTTON_RIGHT)

    # joycon buttons computing
    pressed_joycon_buttons = joycon_inputs.get_pressed_buttons(previous_joycon_buttons_state, current_joycon_buttons_state)

    for button in pressed_joycon_buttons:
        # TODO: play sound
        print(button)

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
    previous_joycon_buttons_state = joycon_inputs.get_buttons_state()

    sleep(0.015)  # joycon refresh rate
