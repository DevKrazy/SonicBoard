from enum import Enum, unique

SOUNDS_FOLDER_PATH = "../sound_assets/"


@unique  # ensures that two enum members cannot have the same value
class Profile(Enum):
    MEMES = SOUNDS_FOLDER_PATH + "memes/"
    DRUM = SOUNDS_FOLDER_PATH + "drum/"
    CAT = SOUNDS_FOLDER_PATH + "cat/"

    def get_path(self):
        """
        :return: the SoundProfile's folder path
        """
        return self.value
