# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
import busio
import time
import ssl
import socketpool
import wifi
import adafruit_gps
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import json


import neopixel

print(dir(MQTT))
#print(dir(board))

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')
gps.send_command(b"PMTK220,1000")

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])
### Feeds ###

# Setup a feed named 'photocell' for publishing to a feed
longlat_feed = secrets["aio_username"] + "/feeds/gpslatlong"
speed_feed = secrets["aio_username"] + "/feeds/gpsspeed"
status = secrets["aio_username"] + "/feeds/status"

# Setup a feed named 'onoff' for subscribing to changes
onoff_feed = secrets["aio_username"] + "/feeds/onoff"

### Code ###

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to Adafruit IO! Listening for topic changes on %s" % onoff_feed)
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(onoff_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=secrets["port"],
    username=secrets["aio_username"],
    password=secrets["aio_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to Adafruit IO...")
mqtt_client.connect()
last_print = time.monotonic()
photocell_val = 0
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    pixels.fill((0,0,0))
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    # Poll the message queue
    mqtt_client.loop()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            mqtt_client.publish(status,"Waiting for fix")
            pixels.fill((255,0,0))
            continue
        pixels.fill((0,0,255))
        x = gps.speed_knots
        if x is None:
            x = 0
        y = gps.latitude
        z = gps.longitude
        a = gps.altitude_m
        if a is None:
            a = 0
        dic = {"value": x, "lat": y, "lon": z, "ele": a}
        # Send a new message
        print(gps.altitude_m,gps.speed_knots)
        print("{},{}, {},{}".format(x,y,z,a))
        print(json.dumps(dic))
        mqtt_client.publish(longlat_feed, json.dumps(dic))
        mqtt_client.publish(status,"Recieved Long Lat")
        mqtt_client.publish(speed_feed,x*1.15078)
        print("Sent!")
        time.sleep(10)
        photocell_val += 1

