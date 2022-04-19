import neopixel
from adafruit_circuitplayground import cp
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.sequence import AnimationSequence
import time

BLUE = (0, 0, 100)
RED = (100, 0 , 0)
GREEN = (0, 100, 0)


while True:
    cp.pixels.fill(BLUE)
    time.sleep(0.5)
    cp.pixels.fill(RED)
    time.sleep(0.5)
    cp.pixels.fill(GREEN)
    time.sleep(0.5)
