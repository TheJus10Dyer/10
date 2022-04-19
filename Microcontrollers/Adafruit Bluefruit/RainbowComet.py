import neopixel
import board
from adafruit_led_animation.animation.rainbowcomet import RainbowComet

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=4, bounce=True)

while True:
    rainbow_comet.animate()
