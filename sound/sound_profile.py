SOUNDS_FOLDER_PATH = "/home/pi/Desktop/SonicBoard/sound_assets/"

# Profiles format: [[name0, path0], [name1, path1], ...]
PROFILES = [["memes", "memes/"], ["drum", "drum/"], ["cat", "cat/"]]

profile_id = 0


def get_name():
    """
    :return: the profile's name
    """
    return PROFILES[profile_id][0]


def get_path():
    """
    :return: the profile's path
    """
    return PROFILES[profile_id][1]


def get_full_path():
    """
    :return: the profile's complete path
    """
    return SOUNDS_FOLDER_PATH + get_path()


def next_profile():
    """
    Increments and returns the profile_id.
    :return: the incremented profile_id
    """
    global profile_id

    if profile_id < len(PROFILES) - 1:  # we apply -1 otherwise the profile_id could go out of bound
        profile_id += 1
    else:
        profile_id = 0

    return profile_id


def previous_profile():
    """
    Decrements and returns the profile_id.
    :return: the decremented profile_id
    """
    global profile_id

    if profile_id > 0:
        profile_id -= 1
    else:
        profile_id = len(PROFILES) - 1

    return profile_id

