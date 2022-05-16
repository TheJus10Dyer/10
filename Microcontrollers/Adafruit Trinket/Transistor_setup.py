# Write your code here :-)
# Write your code here :-)
import digitalio
import board
import time

signal = digitalio.DigitalInOut(board.A1)
signal.direction = digitalio.Direction.OUTPUT


recieve = digitalio.DigitalInOut(board.A0)
recieve.direction = digitalio.Direction.INPUT
recieve.pull = digitalio.Pull.DOWN

count = 0

while True:
    signal.value = True
    time.sleep(1)
    print(signal.value, recieve.value)

