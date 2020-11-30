import smbus
import time
import SoundProfile

bus = smbus.SMBus(1)  # opens the I2C-1 bus

# LCD display addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e


def init_screen():
    """
    Initialises the LCD.
    """
    text_command(0x01)  # clear 00000001
    text_command(0x0F)  # display/cursor/blink on/off control
    text_command(0x38)


def set_color(red, green, blue):
    """
    Changes the LCD backlight color according to the given RGB values.
    :param red: red byte value (hexadecimal)
    :param green: green byte value (hexadecimal)
    :param blue: blue byte value (hexadecimal)
    """
    # write_byte_data(address, register, byte)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x00, 0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x01, 0x00)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xAA)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x02, blue)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x03, green)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x04, red)


def text_command(byte):
    """
    Sends a given byte to the LCD text address (with a small delay to avoid problems).
    :param byte: the byte to send
    """
    time.sleep(0.1)
    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, byte)


def set_text(text, crop=True):
    """
    Displays text to the LCD.
    :param text: the text
    :param crop: doesn't display characters at indexes greater than 15 if True; displays them on the second line if False
    """
    init_screen()
    i = 0  # char numbers on the line
    for character in text:
        if character == '\n':  # case of line break
            text_command(0xc0)  # line return
            i = 0
        elif i == 15 and crop == False:  # reached end of line and text needs to be cropped
            bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(character))
            text_command(0xc0)
            i = 0
        else:  # normal case, we write the character
            bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(character))
        i += 1


def display_main_menu():
    set_text("Profil :\n" + "<profil>")  # TODO: display real profile


def display_volume_menu(volume):
    set_text("Volume :\n-     " + str(volume) + "      +")


def display_profile_menu(profile):
    profile_number = len(SoundProfile)
    profile_index = profile.ordinal()
    set_text(profile.value + "\n<     " + str(profile_index) + "/" + profile_number + "     >")


#  TODO: write more useful functions (set_line(line_number, text), set_char_at(x, y, char) etc...)
