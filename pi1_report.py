#!/usr/bin/python
import time
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json
import datetime
import pytz
from pytz import timezone

temp_data = {"temperature": 0, "timestamp": ""}
hum_data = {"humidity": 0, "timestamp": ""}

client = mqtt.Client()
client.connect("XXX.XXX.X.X", 1883, 60) #IP address of Home001

client.loop_start()

try:
    while True:
        sensor = 22
        pin = 5
        humidity,temperature = dht.read_retry(sensor, pin)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
		
		timestamp_data = datetime.datetime.now(pytz.utc).astimezone(timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
		
        temp_data["temperature"] = temperature
        temp_data["timestamp"] = timestamp_data
        hum_data["humidity"] = humidity
        hum_data["timestamp"] = timestamp_data

        client.publish('home001/pi01/temperature', json.dumps(temp_data))
        client.publish('home001/pi01/humidity', json.dumps(hum_data))

        time.sleep(60) #time interval to be determined
		
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
