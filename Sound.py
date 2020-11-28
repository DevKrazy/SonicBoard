from enum import Enum, unique

SOUND_EXTENSION = "mp3"


@unique  # ensures that two enum members cannot have the same value
class Sound(Enum):
    SOUND_A = "sound_a." + SOUND_EXTENSION
    SOUND_B = "sound_b." + SOUND_EXTENSION
    SOUND_X = "sound_x." + SOUND_EXTENSION
    SOUND_Y = "sound_y." + SOUND_EXTENSION
    SOUND_UP = "sound_up." + SOUND_EXTENSION
    SOUND_DOWN = "sound_down." + SOUND_EXTENSION
    SOUND_LEFT = "sound_left." + SOUND_EXTENSION
    SOUND_RIGHT = "sound_right." + SOUND_EXTENSION

    def get_sound_filename(self):
        """
        :return: the Sound's filename
        """
        return self.value
