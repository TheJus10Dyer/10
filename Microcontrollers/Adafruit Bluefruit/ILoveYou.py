import board
import digitalio
import time

red = digitalio.DigitalInOut(board.A2)
red.direction = digitalio.Direction.OUTPUT
red.value = False



while True:
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    print('I')
    time.sleep(1)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    print('L')
    time.sleep(1)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    print('O')
    time.sleep(1)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    print('V')
    time.sleep(1)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    print('E')
    time.sleep(1)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    print('Y')
    time.sleep(1)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    print('O')
    time.sleep(1)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(0.5)
    red.value = False
    time.sleep(0.5)
    red.value = True
    time.sleep(1)
    red.value = False
    time.sleep(0.5)
    print('U')
    time.sleep(0.5)
    print('I Love You')
    time.sleep(5)





