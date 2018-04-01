# RaspberryPi-Home-Monitoring

All data in string format.

- arduino_report.ino for Arduino
  - MQTT topic: home001/ar01/flame 
    * Msg format: {Flame: 0 (no fire) or 1 (fire!!), Timestamp: 2018-04-01 20:28:00}
  - MQTT topic: home001/ar01/gas
    * Msg format:{Gas: 0 (leak!!) or 1 (no leak), Timestamp: 2018-04-01 20:28:00}
           

- pi1_report.py for Pi01
  - MQTT topic: home001/pi01/temperature 
    * Msg format: {Temperature: XX , Timestamp: 2018-04-01 20:28:00}
  - MQTT topic: home001/ar01/humidity
    * Msg format:{Humidity: XX, Timestamp: 2018-04-01 20:28:00}


- pi2_report.py for Pi02
  - MQTT topic: home001/pi02/motion
    * Msg format: {Status: Start (hv motion) or End (motion ended) , Timestamp: 2018-04-01 20:28:00}
  - MQTT topic: home001/pi02/switch
    * Msg format:{Status: Open (door opened) or Closed (door closed), Timestamp: 2018-04-01 20:28:00}
