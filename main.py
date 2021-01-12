from sound import sound_player, sound_profile
from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('162.38.110.65', 4560)

# TEST

# current profile's id
profile_id = 0


while True:

    sender.send_message('/button', '/home/pi/Desktop/SonicThomas/sound_assets/memes/' + 'a' + '.wav')
    print("aa")
    sleep(2)  # joycon refresh rate
