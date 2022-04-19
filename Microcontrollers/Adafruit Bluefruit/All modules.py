from adafruit_circuitplayground.bluefruit import cpb
import time
print(dir(cpb))
starttime = time.monotonic()
while time.monotonic()-starttime < 100:
    t = time.monotonic()-starttime
    x,y,z = cpb.acceleration
    #light = cpb.light
    #sound_level = cpb.sound_level
    #temperature = cpb.temperature
    cpb.red_led = True
    print((t,x,y,z))
    time.sleep(0.5)
    cpb.red_led = False
    time.sleep(0.1)
