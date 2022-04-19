from adafruit_led_animation.animation.rainbow import Rainbow
import neopixel
import board


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

rainbow = Rainbow(pixels, speed=0.01, period=5)

while True:
    rainbow.animate()
