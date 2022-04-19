"""
Justin Dyer
Instrumentation project: House Alarm

"""

#Import modules
import board
import time
import digitalio
import analogio
import neopixel
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile
import Timestamp



#enabling the speaker on the board
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

#Setting toggle switch as an output to toggle armed and disarmed
toggle = digitalio.DigitalInOut(board.A4)
toggle.direction = digitalio.Direction.INPUT
toggle.pull = digitalio.Pull.DOWN

#Setting board slide switch as an input to toggle data logging system
switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

#Setting the magnetic door switch as trip as an input
trip = digitalio.DigitalInOut(board.A5)
trip.direction = digitalio.Direction.INPUT
trip.pull = digitalio.Pull.DOWN

#Setting the D13 on the board as an output to indicate settings (may remove)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
led.value = False

#Setting neopixels on the board as an output to indicate settings
pixels = neopixel.NeoPixel(board.TX, 8)
pixels2 = neopixel.NeoPixel(board.NEOPIXEL, 10)

#Creating a function to output audio wav file
def play_file(filename):
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.AUDIO) as audio:
            audio.play(wave)
            while audio.playing:
                pass

#making a count of the loop
count = 0

#boot up time
btime = time.monotonic()

#if in data logging mode, create TimeStamp file
if switch.value == False:
    file = open("\TimeStamp.txt","w")
else:
    print("Not opening file")

#Initial set time for time function to run off of
starttime = [3,29,2022,7,39,'PM']

#take data from start time
minutes = starttime[4]
hour = starttime[3]
year = starttime[2]
day = starttime[1]
month = starttime[0]
period = starttime[5]

#defining days in the month of interest
January = 31
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31

##Try function of timestamp to develop stamp in loop


#Loop for program
while True:
    if toggle.value is True:
        ##Armed loop
        led.value = True
        if trip.value is False:
            doorvalue = 'Open'
            while True:
                print('Intruder')
                pixels2.fill((100, 0, 0))
                pixels.fill((100, 0, 0))
                play_file("purge.wav")
                if toggle.value is False:
                    break
        if trip.value is True:
            doorvalue = 'Closed'
            print('Safe')
            pixels2.fill((0, 0, 0))
            pixels.fill((0, 0, 0))
    if toggle.value is False:
        ##Disarmed loop
        led.value = False
        if trip.value is False:
            doorvalue = 'Open'
            print('Door Opened')
            pixels2.fill((0, 100, 0))
            pixels.fill((0, 100, 0))
            if count == 0:
                play_file("ALERT.wav")
                count = count + 1
        if trip.value is True:
            doorvalue = 'Closed'
            print('Door Closed')
            pixels2.fill((0, 0, 0))
            pixels.fill((0, 0, 0))
            if count == 1:
                count = count - 1
    pixels.show()
    ##Check if it is a leap year and assign days of Feb.
    if year%400 == 0 or year%4 == 0 and year%100 !=0:
        February = 29
    else:
        February = 28
    timestamp = [month,day,year,hour,minutes,period]
    #The time in seconds since boot
    runtime = (time.monotonic() - btime)

    ##Calendar addition
    if runtime > 60:
        minutes = minutes + 1
        btime = time.monotonic()
    if hour < 12:
        x = 1
    if minutes > 59:
        minutes = 0
        hour = hour + 1
        if hour == 12 and x == 1:
            x = 0
            if period == 'AM':
                period = 'PM'
                pass
            if period == 'PM':
                period = 'AM'
            if hour == 12 and period == 'AM':
                day = day + 1
        if hour == 13:
            hour = 1
    if month == 1:
        length = January
    if month == 2:
        length = February
    if month == 3:
        length = March
    if month == 4:
        length = April
    if month == 5:
        length = May
    if month == 6:
        length = June
    if month == 7:
        length = July
    if month == 8:
        length = August
    if month == 9:
        length = September
    if month == 10:
        length = October
    if month == 11:
        length = November
    if month == 12:
        length = December
    if day > length:
        day = 1
        month = month + 1
    if month == 13:
        month = 1
        year = year + 1

    ##if in data logging setting, write in the file
    ##Must have switch = false upon boot
    if switch.value == False:
        output = str(str(doorvalue) + '    ' + str('Time-stamp: ' + str(month) + '/' + str(day) + '/' + str(year) + '  ' + str(hour) + ':' + str(minutes) + str(period))  + str('\n'))
        file.write(output)
        file.flush()
    if switch.value == True:
        output = "Not writing data to file"
    print(output)
    #print((int(trip.value), ))
    #print(count)
    #print(time.monotonic())
    time.sleep(0.1)


