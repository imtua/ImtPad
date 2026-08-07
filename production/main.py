import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()
encoder = EncoderHandler()

# Pin Definitions
keyboard.matrix = KeysScanner( pins=[board.D0, board.D1, board.D2, board.D3, board.D4, board.D5] )
encoder.pins = ((board.D8,board.D7,board.D9),)

# Key Definitions
keyboard.keymap = [[KC.Z, KC.W, KC.X, KC.A, KC.S, KC.D],]
encoder.map = ( ( (KC.VOLD, KC.VOLU, KC.MUTE), ), )

keyboard.modules = [encoder]

if __name__ == "__main__":
    keyboard.go()