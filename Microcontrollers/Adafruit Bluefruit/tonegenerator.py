import board
import analogio
import time
import neopixel
import array
import math
import digitalio
from audiocore import RawSample
from audiopwmio import PWMAudioOut as AudioOut

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

audio = AudioOut(board.AUDIO)

potentio = analogio.AnalogIn(board.A1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

while True:
    data = potentio.value*3.3/ (65536*4)
    peak = potentio.value*(3.3/ 65536)*3.0303030303
    tone_volume = 0.2
    if data > 0.8:
        x = 5
    if 0.75 < data <= 0.8:
        x = 6
    if 0.70 < data <= 0.75:
        x = 7
    if 0.65 < data <= 0.70:
        x = 8
    if 0.60 < data <= 0.65:
        x = 9
    if 0.55 < data <= 0.60:
        x = 10
    if 0.50 < data <= 0.55:
        x = 11
    if 0.45 < data <= 0.50:
        x = 12
    if 0.40 < data <= 0.45:
        x = 13
    if 0.35 < data <= 0.40:
        x = 14
    if 0.30 < data <= 0.35:
        x = 15
    if 0.25 < data <= 0.30:
        x = 16
    if 0.20 < data <= 0.25:
        x = 17
    if 0.15 < data <= 0.20:
        x = 18
    if 0.10 < data <= 0.15:
        x = 19
    if data <= 0.1:
        x = 20
    wavelength = int(x)
    sine_wave = array.array("H", [0] * wavelength)
    sine_wave_sample = RawSample(sine_wave)
    for i in range(wavelength):
        sine_wave[i] = int((1 + math.sin(math.pi * 2 * i / wavelength)) * tone_volume * (2 ** 15 - 1))
    for i in range(10):
            if i <= peak:
                pixels[i] = (100, 0, 0)
            else:
                pixels[i] = (0, 0, 0)
    if switch.value == True:
        audio.play(sine_wave_sample, loop=True)
    if switch.value == False:
        audio.stop()
    pixels.show()
    print(wavelength)
    time.sleep(0.001)

