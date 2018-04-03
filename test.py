import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    if msg.payload.decode() == "00":
        client.publish("home001/light", "t + 00");
    elif msg.payload.decode() == "01":
        client.publish("home001/light", "t + 01");
    elif msg.payload.decode() =="02":
        client.publish("home001/status", "On/Off");
        
client = mqtt.Client();
client.connect("192.168.4.1", 1883, 60)

client.subscribe("home001/action")

client.on_message = on_message
client.loop_forever()