import time
from adafruit_circuitplayground.bluefruit import cpb
import math


yaw_f = 0
pitch_f = 0
s = 0.3

while True:
    x,y,z = cpb.acceleration
    yaw = math.atan2(y,z)*180/math.pi
    pitch = math.atan2(x,z)*180/math.pi
    yaw_f = (1-s)*yaw_f+s*yaw
    pitch_f = (1-s)*pitch_f+s*pitch
    if pitch_f > 90:
        pitch_f = 90
    if pitch_f < -90:
        pitch_f = -90
    if yaw_f > 90:
        yaw_f = 90
    if yaw_f < -90:
        yaw_f = -90
    yaw_servo = - yaw_f
    pitch_servo = - pitch_f
    print(x,y,z,yaw, pitch, yaw_f, pitch_f, yaw_servo,pitch_servo)
    time.sleep(.3)
