from sound import sound_player, sound_profile
from utils import joycon_utils
from pyjoycon import JoyCon, get_R_id, get_L_id
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

# TEST
id_R = get_R_id()
id_L = get_L_id()
joycon_R = JoyCon(*id_R)
joycon_L = JoyCon(*id_L)

# current profile's id
profile_id = 0

previous_buttons_state = joycon_utils.extract_useful_inputs(joycon_L, joycon_R)

while True:
    current_buttons_state = joycon_utils.extract_useful_inputs(joycon_L, joycon_R)
    pressed_buttons = joycon_utils.get_pressed_buttons(previous_buttons_state, current_buttons_state)

    for button in pressed_buttons:
        print(button)
        sender.send_message('/button', '/home/thomas/PycharmProjects/SonicBoard/sound_assets/memes/' + button + '.wav')

    previous_buttons_state = joycon_utils.extract_useful_inputs(joycon_L, joycon_R)

    sleep(0.015)  # joycon refresh rate
