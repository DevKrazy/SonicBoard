from pyjoycon import JoyCon, get_R_id

# joycons
id_R = get_R_id()
#id_L = get_L_id()
joycon_R = JoyCon(*id_R)
#joycon_L = JoyCon(*id_L)

# buttons names as given in the joycon status
BUTTON_A = 'a'
BUTTON_B = 'b'
BUTTON_X = 'x'
BUTTON_Y = 'y'
BUTTON_UP = 'up'
BUTTON_DOWN = 'down'
BUTTON_LEFT = 'left'
BUTTON_RIGHT = 'right'


def get_buttons_state():
    """
    Extracts the inputs which will be used by SonicBoard.
    :param joycon_left: a reference to the left joycon
    :param joycon_right: a reference to the right joycon
    :return: a dictionary of {String: int} containing the joycons' input
    """
    return {
        BUTTON_A: joycon_R.get_button_a(),
        BUTTON_B: joycon_R.get_button_b(),
        BUTTON_X: joycon_R.get_button_x(),
        BUTTON_Y: joycon_R.get_button_y()
        # BUTTON_UP: joycon_left.get_button_up(),
        # BUTTON_DOWN: joycon_left.get_button_down(),
        # BUTTON_LEFT: joycon_left.get_button_left(),
        # BUTTON_RIGHT: joycon_left.get_button_right()
    }


def get_pressed_buttons(previous_state, current_state):
    """
    Compares the previous state and current state of the buttons to see which were pressed.
    :param previous_state: the dictionary containing the previous state of the buttons
    :param current_state: the dictionary containing the current state of the buttons
    :return: a list of String containing the buttons name which have been pressed.
    """
    pressed_buttons = []  # the list of the buttons which have been pressed

    for key, value in previous_state.items():
        if current_state[key] != value and current_state[key] == 1:
            # if the button's state changed, adds it to the pressed_buttons list
            pressed_buttons.append(key)

    return pressed_buttons
