import time
import board
import busio
import digitalio
import adafruit_gps
print(dir(board))

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)

switch = digitalio.DigitalInOut(board.A2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if switch.value == False:
    file = open('CPB_Datalog.txt','w')
    FILEOPEN = True
else:
    print('Not opening file for writing')
    FILEOPEN = False


gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
if switch.value == False:
    file = open('CPB_Datalog.txt','w')
    FILEOPEN = True
else:
    print('Not opening file for writing')
    FILEOPEN = False
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        if switch.value == False:
            #PRINT TO A FILE
            output = str(time.monotonic()) + ' ' + str('\n')
            file.write(output)
            file.flush()
        else:
            if FILEOPEN == False:
                print('Not taking data...')
            if FILEOPEN == True:
                print('FILE CLOSED!!!')
                file.close()
                FILEOPEN = False
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
        print("Latitude: {0:.6f} degrees".format(gps.latitude))
        print("Longitude: {0:.6f} degrees".format(gps.longitude))

