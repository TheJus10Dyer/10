import board
import time
import digitalio
import adafruit_dotstar
import pwmio
import analogio

servo = pwmio.PWMOut(board.A2, frequency=50)
# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

potentio = analogio.AnalogIn(board.A4)

theta = 90

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = .1
print(dir(board))
while True:
    data = potentio.value*3.3 / 65536
    print(theta)
    theta = 54.54*data
    led[0] = (20,20,200)
    #theta = float(input('Degrees to rotate = '))
    if theta > 180:
        raise Exception('Sorry, no numbers greater than 180')
    if theta < 0:
        raise Exception('Sorry, no numbers less than zero')

    pulse_ms = 0.00979842*theta + 0.60521761
    #print('Milli Second Pulse = ',pulse_ms)
    servo.duty_cycle = servo_duty_cycle(pulse_ms)
    #time.sleep(.05)
