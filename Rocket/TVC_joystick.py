import board
import time
import digitalio
import adafruit_dotstar
import pwmio
import analogio
import math

# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

yaw_servo = pwmio.PWMOut(board.A4, frequency=50)
pitch_servo = pwmio.PWMOut(board.A3, frequency=50)


togglelr = analogio.AnalogIn(board.A1)
toggleud = analogio.AnalogIn(board.A2)


led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = .1

print(dir(board))
while True:
    updown = toggleud.value*3.3 / 65536
    leftright = togglelr.value*3.3 / 65536
    yaw = 24.24*updown+60
    pitch = 12.12*leftright+60
    if yaw >= 128:
        yaw = 128
    if yaw <= 70:
        yaw = 70
    if pitch >= 180:
        pitch = 180
    if pitch <= 0:
        pitch = 0
    yaw_pulse_ms = 0.00979842*yaw + 0.60521761
    pitch_pulse_ms = 0.01004491*pitch + 0.78714457
    yaw_servo.duty_cycle = servo_duty_cycle(yaw_pulse_ms)
    pitch_servo.duty_cycle = servo_duty_cycle(pitch_pulse_ms)
    print(updown,leftright,yaw,pitch)
    time.sleep(0.1)

