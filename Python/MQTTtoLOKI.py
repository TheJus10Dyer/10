# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 06:49:23 2022

@author: Justin
"""

import paho.mqtt.client as mqttClient
import time
import json
import logging
import logging_loki
import numpy as np

logging_loki.emitter.LokiEmitter.level_tag = "level"
# assign to a variable named handler 

handler = logging_loki.LokiHandler(
    url="https://logs-prod3.grafana.net/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("229052", "eyJrIjoiYjMwMGNhMmQ3NzMxMDVkMjMwOTY3ZGIyYzZkZTYzZTI4ZDE1ZWIwNiIsIm4iOiJ0ZXN0IiwiaWQiOjY2MDg1Mn0="),
    version="1",
)

logging.addLevelName(15, "TRACE")

def trace(self, message, *args, **kws):
   if self.isEnabledFor(15):
   # Yes, logger takes its '*args' as 'args'.
       self._log(15, message, args, **kws)

logging.Logger.trace = trace


  
def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")
  
def on_message(client, userdata, message):
    #print('Message: ' , message.payload)
    message = json.loads(message.payload)
    ids = message["end_device_ids"]
    payload = message["uplink_message"]
    decoded_payload = payload["decoded_payload"]
    info = decoded_payload["gps"]
    eui = ids["dev_eui"]
    voltage = info["batV"]
    lat = info["latitudeDeg"]
    long = info["longitudeDeg"]
    print("ID: " + str(eui) + '\n' + "Battery Voltage: " + str(voltage) + "V" + '\n' + 'Latitude: ' + str(lat) + '\n' + 'Longitude: ' + str(long))
    logger = logging.getLogger("my-logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.info(
       str(json.dumps(message)),
      
       extra={"tags": {"level": "Lat"}},
    )
    
Connected = False   #global variable for the state of the connection
  
broker_address= "nam1.cloud.thethings.industries"  #Broker address
port = 1883                         #Broker port
user = "aker-gps@aker"                    #Connection username
password = "NNSXS.MB7DQ6XGDZP7CMVSKB5O5YAHO762NOXFK2FRDRY.TC7UMKR3NVE66HB72KTLJYO5Q5AF4JGM65FNWYNCEEXVWDQ4Z4LA"            #Connection password
  
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("#")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()