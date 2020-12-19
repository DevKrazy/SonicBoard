from sound import sound_player, sound_profile
from sound.sounds import Sound
from pyjoycon import JoyCon, get_R_id, get_L_id
from time import sleep

id_R = get_R_id()
id_L = get_L_id()
joycon_R = JoyCon(*id_R)
joycon_L = JoyCon(*id_L)

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

    if a != a_current and a_current == 1:
        #sound_player.play_sound(Sound.SOUND_A, profile_id)
        print("pressed a button")

    a = a_current
    b = b_current
    x = x_current
    y = y_current
    up = up_current
    down = down_current
    left = left_current
    right = right_current


    sleep(0.015) # joycon refresh rate



