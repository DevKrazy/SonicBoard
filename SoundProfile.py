from enum import Enum, unique

SOUNDS_FOLDER_PATH = "./sounds/"


@unique  # ensures that two enum members cannot have the same value
class SoundProfile(Enum):
    MEMES = SOUNDS_FOLDER_PATH + "memes/"
    DRUM = SOUNDS_FOLDER_PATH + "drum/"
    CAT = SOUNDS_FOLDER_PATH + "cat/"

    def get_path(self):
        """
        :return: the SoundProfile's folder path
        """
        return self.value
