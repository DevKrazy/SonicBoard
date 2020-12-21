from enum import Enum, unique

SOUNDS_FOLDER_PATH = "../sound_assets/"

# Profiles format:
# [[name0, path0], [name1, path1], ...]
PROFILES = [["memes", "memes/"], ["drum", "drum/"], ["cat", "cat/"]]


def get_name(profile_id):
    """
    :param profile_id: the id of the profile (0, 1, ...)
    :return: the profile's name
    """
    return PROFILES[profile_id[0]]


def get_path(profile_id):
    """
    :param profile_id: the id of the profile (0, 1, ...)
    :return: the profile's path
    """
    return PROFILES[profile_id][1]


def get_full_path(profile_id):
    """
    :param profile_id: the id of the profile (0, 1, ...)
    :return: the profile's complete path
    """
    return SOUNDS_FOLDER_PATH + get_path(profile_id)





