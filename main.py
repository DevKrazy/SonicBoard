from sound import sound_player, sound_profile, sounds
from pyjoycon import device
from pyjoycon.joycon import JoyCon
from time import sleep

joycon_R = JoyCon(*device.get_ids("R"))
joycon_L = JoyCon(*device.get_ids("L"))

# current profile's id
profile_id = 0

# right joycon buttons
a = 0
b = 0
x = 0
y = 0
# left joycon buttons
up = 0
down = 0
left = 0
right = 0

while True:

    # buttons update
    # TODO: use a dict or an array to store buttons
    # TODO: make a function to detect which button was pressed
    # TODO: play a sound according to this function's return value (tuple?)
    a_current = joycon_R.get_button_a()
    b_current = joycon_R.get_button_b()
    x_current = joycon_R.get_button_x()
    y_current = joycon_R.get_button_y()
    up_current = joycon_L.get_button_up()
    down_current = joycon_L.get_button_down()
    left_current = joycon_L.get_button_left()
    right_current = joycon_L.get_button_right()

    if a != a_current:
        sound_player.play_sound(sounds.SOUND_A, profile_id)


    sleep(0.015) # joycon refresh rate



