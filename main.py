import LCD

LCD.init_screen()
LCD.set_color(0x80, 0x10, 0x10)
LCD.set_text("Cette ligne est treeees longue...")


# from pyjoycon import device, get_R_id, get_L_id
# from pyjoycon.joycon import JoyCon
# import pygame
# import time
# from SoundPlayer import playsound
# pygame.mixer.pre_init(buffer=16)#lowering buffer to reduce input lag
# pygame.mixer.init() #Initialisation of mixer
# pygame.mixer.set_num_channels(30) #Number of audio channel
#
# #First 3 sounds
# sound_a = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/bruh.ogg")
# sound_b = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/honteux.ogg")
# sound_x = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/oof.ogg")
# sound_y = pygame.mixer.Sound("/home/thomas/PycharmProjects/SonicBoard/oof.ogg")
#
# #joycon sound path
# """sound_a = pygame.mixer.Sound("/home/pi/SonicBoard/sounds/test.waw")
# sound_b = pygame.mixer.Sound("/home/pi/SonicBoard/sounds/bruh.ogg")
# sound_x = pygame.mixer.Sound("/home/pi/SonicBoard/sounds/honteux.ogg")
# sound_y = pygame.mixer.Sound("/home/pi/SonicBoard/sounds/oof.ogg")"""
#
# # Right JoyCon init
# joycon_id = get_R_id()
# joycon = JoyCon(*joycon_id)
#
# #initialisation of button previous state
# b = 0
# a = 0
# x = 0
# y = 0
# while True:
#
#     b_current = joycon.get_button_b()
#     a_current = joycon.get_button_a()
#     y_current = joycon.get_button_y()
#     x_current = joycon.get_button_x()
#     #check if button is pushed and if button is not already pressed
#
#     if b_current and b != 1 :
#         playsound(sound_b)
#     if a_current and a != 1 :
#         playsound(sound_a)
#     if y_current and y != 1 :
#         playsound(sound_y)
#
#
#     #registering previous joycon state for next loop
#     b = b_current
#     a = a_current
#     x = x_current
#     y = y_current
#     time.sleep(0.015) #joycon refresh rate
#
