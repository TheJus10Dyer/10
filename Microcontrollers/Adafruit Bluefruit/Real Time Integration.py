import board
from adafruit_circuitplayground import cp
import time
from array import array
import analogio
import digitalio
import math

##['__class__', '__init__', '__module__', '__qualname__', '__dict__',
##'temperature', '_audio_out', '_normalized_rms', 'sound_level', 'loud_sound',
##'play_mp3', '_sample', '_mic', '_samples', 'stop_tone', '_speaker_enable', 'light',
##'detect_taps', '_default_tap_threshold', 'configure_tap', 'tapped', 'acceleration', 'shake',
##'_touch', 'touch_A1', 'touch_A2', 'touch_A3', 'touch_A4', 'touch_A5', 'touch_A6', 'touch_TX',
##'adjust_touch_threshold', 'pixels', 'button_a', 'button_b', 'switch', 'red_led', '_sine_sample',
##'_generate_sample', 'play_tone', 'start_tone', 'play_file', '_a', '_b', '_switch', '_led', '_pixels',
##'_temp', '_light', '_touches', '_touch_threshold_adjustment', '_i2c', '_int1', '_lis3dh', '_sine_wave', '_sine_wave_sample', '_detect_taps']


gearth = 9.81
while True:
    ax1,ay1,az1 = cp.acceleration
    t1 = time.monotonic()
    time.sleep(0.1)
    ax2,ay2,az2 = cp.acceleration
    t2 = time.monotonic()
    vx1 = (ax2-ax1)*(t2-t1)
    vy1 = (ay2-ay1)*(t2-t1)
    vz1 = (az2-az1)*(t2-t1)
    speed1 = math.sqrt(vx1**2+vy1**2+vz1**2)
    ax3,ay3,az3 = cp.acceleration
    t3 = time.monotonic()
    time.sleep(0.1)
    ax4,ay4,az4 = cp.acceleration
    t4 = time.monotonic()
    vx2 = (ax4-ax3)*(t4-t3)
    vy2 = (ay4-ay3)*(t4-t3)
    vz2 = (az4-az3)*(t4-t3)
    speed2 = math.sqrt(vx2**2+vy2**2+vz2**2)
    speed = (speed1+speed2)/2
    pos = (speed2-speed1)*(t4-t1)
    ax,ay,az = cp.acceleration
    ar = math.sqrt(ax**2+ay**2+az**2) - gearth
    print((ar,speed,pos))


