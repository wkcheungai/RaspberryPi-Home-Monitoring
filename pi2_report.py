#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
import datetime
import pytz
from pytz import timezone


GPIO.setmode(GPIO.BCM)

PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)
pir_state = 0
pir_data = {"status": "", "timestamp": ""}

switch_PIN = 21
GPIO.setup(switch_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
switch_state = 0
switch_data = {"status": "", "timestamp": ""}

client = mqtt.Client()
client.connect("XXX.XXX.X.X", 1883, 60) #IP address of Home001

client.loop_start()

time.sleep(30) #for stabilization
try:
    while 1:
        if (GPIO.input(PIR_PIN)):
            if (pir_state == 0):
                pir_state = 1
                pir_data["status"] = "Start"
                timestamp_data = datetime.datetime.now(pytz.utc).astimezone(timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
                pir_data["timestamp"] = timestamp_data
                client.publish('home001/pi02/motion', json.dumps(pir_data))
        
		else:
            if (pir_state == 1):
                pir_state = 0
                pir_data["status"] = "End"
                timestamp_data = datetime.datetime.now(pytz.utc).astimezone(timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
                pir_data["timestamp"] = timestamp_data
                client.publish('home001/pi02/motion', json.dumps(pir_data))
        
		
        if (GPIO.input(switch_PIN)):
            if (switch_state == 0):
                switch_state = 1
                switch_data["status"] = "Open"
                timestamp_data = datetime.datetime.now(pytz.utc).astimezone(timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
                switch_data["timestamp"] = timestamp_data
                client.publish('home001/pi02/switch', json.dumps(switch_data))
        
		else:
            if (switch_state == 1):
                switch_state = 0
                switch_data["status"] = "Closed"
                timestamp_data = datetime.datetime.now(pytz.utc).astimezone(timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
                switch_data["timestamp"] = timestamp_data
                client.publish('home001/pi02/switch', json.dumps(switch_data))

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
	
finally:
    GPIO.cleanup()
