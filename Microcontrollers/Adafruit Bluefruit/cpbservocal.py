import time
import pwmio
import board

servo = pwmio.PWMOut(board.A3, frequency=50)
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

while True:
    for pulse_ms in [0.77,.8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3,2.33]:
        servo.duty_cycle = servo_duty_cycle(pulse_ms)
        print(pulse_ms)
        time.sleep(3)
