import pygame.mixer

MAX_CHANNEL_NUMBER = 30


def playsound(sound, channel_number=0):
    if pygame.mixer.Channel(channel_number).get_busy() and channel_number < 29:
        playsound(sound, channel_number + 1)
    else:
        pygame.mixer.Channel(channel_number).play(sound)


def play_sound(sound, profile, channel_number=0, extension="wav"):
    if pygame.mixer.Channel(channel_number).get_busy():
        if channel_number <= MAX_CHANNEL_NUMBER:
            play_sound(sound, profile, channel_number + 1)
        else:
            print("Maximum channel number reached (" + str(MAX_CHANNEL_NUMBER) + ")")
            # TODO: print warning on LCD
    else:
        # TODO: throw error and print on LCD
        pygame.mixer.Channel(channel_number).play(profile.get_path + sound.get_sound_filename() + "." + extension)
