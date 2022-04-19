import neopixel
from adafruit_circuitplayground import cp
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.sequence import AnimationSequence

BLUE = (0, 0, 100)

animations = AnimationSequence(
    Chase(cp.pixels, 0.1, size=3, spacing=2, color= BLUE),
)

while True:
    animations.animate()
