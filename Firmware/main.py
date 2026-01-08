# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
import board
from kmk.extensions.RGB import RGB



# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.UP, KC.LCTL(KC.Z), KC.DOWN, KC.LCTL(KC.Y),]
]

# TODO: Do the OLED and LEDs later

# LED control
rgb = RGB(pixel_pin=board.GP26, num_pixels=4, brightness=0.2, animation_type=KC.RGB_ANIMATION_RAINBOW)
keyboard.extensions.append(rgb)

# OLED Display


# display = SSD1306(i2c=board.I2C(), width=128, height=64)
# keyboard.extensions.append(display)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()