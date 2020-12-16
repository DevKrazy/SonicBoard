import LCD
import sound.sound_profile as sprofile
import sound.sound_player as splay
from sound.sounds import Sound
from time import sleep

LCD.init_screen()
LCD.set_color(0x80, 0x80, 0x80)
LCD.display_profile_menu(sprofile.get_name(0))

# events loop
#while True:

   # sleep(0.015) # joycon refresh rate



