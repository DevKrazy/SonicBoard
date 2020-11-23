import pygame.mixer


def playsound(sound, channel_number=0):
    if pygame.mixer.Channel(channel_number).get_busy() and channel_number < 29:
        playsound(sound, channel_number + 1)
    else:
        pygame.mixer.Channel(channel_number).play(sound)
