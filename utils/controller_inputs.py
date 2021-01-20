PAD_UP = "up"
PAD_DOWN = "down"
PAD_LEFT = "left"
PAD_RIGHT = "right"
A = "0"
B = "1"
X = "2"
Y = "3"




def get_buttons_status(controller):
    pad = controller.get_pad()
    buttons = controller.get_buttons()