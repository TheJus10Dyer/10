#['__class__', '__init__', '__module__', '__qualname__', '__dict__',
#'temperature', '_audio_out', '_normalized_rms', 'sound_level',
#'loud_sound', 'play_mp3', '_sample', '_mic', '_samples', 'stop_tone',
#'_speaker_enable', 'light', 'detect_taps', '_default_tap_threshold',
#'configure_tap', 'tapped', 'acceleration', 'shake', '_touch', 'touch_A1',
#'touch_A2', 'touch_A3', 'touch_A4', 'touch_A5', 'touch_A6', 'touch_TX',
#'adjust_touch_threshold', 'pixels', 'button_a', 'button_b', 'switch',
#'red_led', '_sine_sample', '_generate_sample', 'play_tone', 'start_tone',
#'play_file', '_a', '_b', '_switch', '_led', '_pixels', '_temp', '_light',
#'_touches', '_touch_threshold_adjustment', '_i2c', '_int1', '_lis3dh',
#'_sine_wave', '_sine_wave_sample', '_detect_taps']

import time
import board
import pwmio
from adafruit_motor import servo
import digitalio
from adafruit_circuitplayground import cp
pwm = pwmio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)


while True:
    if cp.switch is True:
        my_servo.throttle = 0.0
        if cp.button_a is True:
            my_servo.throttle = 1.0
            time.sleep(.135)
            my_servo.throttle = 0.0
            time.sleep(.135)
            my_servo.throttle = -1.0
            time.sleep(.135)
            my_servo.throttle = 0.0
            time.sleep(.135)

    if cp.switch is False:
        pass
