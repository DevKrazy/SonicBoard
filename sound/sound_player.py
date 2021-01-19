import pygame.mixer
from sound import sound_profile

MAX_CHANNEL_NUMBER = 30


def play_soundPYGAME(sound, profile_id, channel_number=0, extension="wav"):
def play_sound(sound, profile_id, channel_number=0, extension="wav"):
    if pygame.mixer.Channel(channel_number).get_busy():  # if the channel is busy
        if channel_number <= MAX_CHANNEL_NUMBER:  # if we have free channels left
            play_soundPYGAME(sound, profile_id, channel_number + 1)  # we recursively calls the play_sound on the next channel
        else:
            print("Maximum channel number reached (" + str(MAX_CHANNEL_NUMBER) + ")")  # displays a warning
            # TODO: print warning on LCD
    else:  # channel is free we play the sound
        print("Playing " + str(sound_profile.get_full_path() + sound.get_sound_filename() + "." + extension) + " in channel " + str(channel_number))
        pygame.mixer.Channel(channel_number).play(sound_profile.get_full_path() + sound.get_sound_filename() + "." + extension)
