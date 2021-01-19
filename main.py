from drivers import LCD
from utils import defcom
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
LCD.set_color(0xFF, 0x00, 0xFF)
#LCD.display_main_menu()
######### END ###########



# previous buttons states
previous_left_button_state = defcom.digitalRead(BUTTON_LEFT)
previous_right_button_state = defcom.digitalRead(BUTTON_RIGHT)

while True:
    # current buttons states
    current_left_button_state = defcom.digitalRead(BUTTON_LEFT)
    current_right_button_state = defcom.digitalRead(BUTTON_RIGHT)

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
    sleep(2)
