import smbus
import time

bus = smbus.SMBus(1)  # opens the I2C-1 bus

# LCD display addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e


def init_screen():
    """
    Initialises the LCD.
    """
    text_command(0x01)  # clear 00000001
    text_command(0x12)  # display/cursor/blink on/off control
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
    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, 0x12)  # turns cursor off


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
        elif i == 15 and crop:  # reached end of line and text needs to be cropped
            bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(character))
            text_command(0xc0)
            i = 0
        else:  # normal case, we write the character
            bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(character))
        i += 1

#  TODO: write more useful functions (set_line(line_number, text), set_char_at(x, y, char) etc...)
