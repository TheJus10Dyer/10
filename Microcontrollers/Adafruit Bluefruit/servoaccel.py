import time
import board
import pwmio
import analogio
from adafruit_circuitplayground.bluefruit import cpb
import math


# Initialize PWM output for the servo (on pin A2):
servo = pwmio.PWMOut(board.A3, frequency=50)
print(dir(pwmio.PWMOut))
# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def move(x,y):
    if x < y:
        output = x + 1
    if x > y:
        output = x - 1
    if x == y:
        output = x

    return output

theta = 90
theta_f = 0
s = 0.3
#z>=9.1
# Main loop will run forever moving between 1.0 and 2.0 mS long pulses:
while True:
    x,y,z = cpb.acceleration
    theta = math.atan2(x,z)*180/3.14159
    theta_f = (1-s)*theta_f+s*theta
    if theta_f > 90:
        theta_f = 90
    if theta_f < -90:
        theta_f = -90
    servo_angle = theta_f + 90
    #if z >= 9.1:
    #    theta = move(theta, 90)
    #if z < 9.1:
    #    if x > 1:
    #        theta = move(theta,180)
    #    if x < -1:
    #        theta = move(theta,0)
    #    else:
    #        pass
    #if theta > 180:
    #    theta = 180
    #if theta < 0:
    #    theta = 0
    #print(x,y,z)
    print(theta)
    #theta = float(input('Degrees to rotate = '))
    #if theta > 180:
    #    raise Exception('Sorry, no numbers greater than 180')
    #if theta < 0:
    #    raise Exception('Sorry, no numbers less than zero')



    pulse_ms = 0.00979842*servo_angle + 0.605216
    #print('Milli Second Pulse = ',pulse_ms)
    servo.duty_cycle = servo_duty_cycle(pulse_ms)
    time.sleep(.05)
