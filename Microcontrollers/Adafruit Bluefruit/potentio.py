import board
import analogio
import time
import neopixel

def scale_range(value):

    return round(value)


potentio = analogio.AnalogIn(board.A1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)



while True:
    data = potentio.value*3.3 / 65536
    peak = data*3.0303030303
    for i in range(10):
            if i <= peak:
                pixels[i] = (100, 0, 0)
            else:
                pixels[i] = (0, 0, 0)
    pixels.show()
    print(((peak), ))
    print(((data), ))
    time.sleep(.1)

