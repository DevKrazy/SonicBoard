from pyjoycon import device, get_R_id, get_L_id
from pyjoycon.joycon import JoyCon
import pygame
import time

pygame.mixer.init()
pygame.mixer.set_num_channels(20)
channel_a = pygame.mixer.Channel(0)
channel_b = pygame.mixer.Channel(1)
channel_x = pygame.mixer.Channel(2)
channel_y = pygame.mixer.Channel(3)

sound_a = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/bruh.ogg")
sound_b = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/honteux.ogg")
sound_x = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/oof.ogg")
sound_y = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/oof.ogg")


# JoyCon
joycon_id = get_R_id()
joycon = JoyCon(*joycon_id)


b = 0
a = 0
y = 0
x = 0



#Play on sound on the appropriate stream




def playsound(path) :
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(0)

while True:
    print(joycon.get_button_a())
    b_current = joycon.get_button_b()
    a_current = joycon.get_button_a()
    y_current = joycon.get_button_y()
    x_current = joycon.get_button_x()
    print(a_current)

    if b_current and b != 1 :
        channel_b.play(sound_b)
    if a_current and a != 1 :
        channel_a.play(sound_a)
    if y_current and y != 1 :
        channel_y.play(sound_x)





    b = b_current
    a = a_current
    x = x_current
    y = y_current
    time.sleep(0.015)

