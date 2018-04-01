#include <Wire.h>
#include <UnoWiFiDevEd.h>
#include <DS3232RTC.h>

#define CONNECTOR "mqtt"
#define TOPIC1 "home001/ar01/flame"
#define TOPIC2 "home001/ar01/gas"

const int flameMin = 0;
const int flameMax = 1024;
int flame_val;
int flame = 0;

int gas_val;
int gas = 7;

void setup() {
  Ciao.begin();
  pinMode(A0,INPUT);
  pinMode(gas,INPUT);

  setSyncProvider(RTC.get);
}

void loop() {
  flame_val = analogRead(flame);
  int dist = map(flame_val, flameMin, flameMax, 0, 3);
  int fire = 0;
  if (dist != 2){
    fire = 1;
  }

  gas_val = digitalRead(gas);
  gas_val = 1 - gas_val;
  
  time_t t;
  t = now();
  String ts = String(year(t)) + "-";
  if (month(t) < 10) {ts += "0";}
  ts += String(month(t)) + "-";
  if (day(t) < 10) {ts += "0";}
  ts += String(day(t)) + " ";

  if (hour(t) < 10) {ts += "0";}
  ts += String(hour(t)) + ":";
  if (minute(t) < 10) {ts += "0";}
  ts += String(minute(t)) + ":";
  if (second(t) < 10) {ts += "0";}
  ts += String(second(t));
  
  Ciao.write(CONNECTOR, TOPIC1, String("{\"flame\":\"" + String(fire) + "\",\"timestamp\":\"" + ts + "\"}") );
  Ciao.write(CONNECTOR, TOPIC2, String("{\"gas\":\"" + String(gas_val) + "\",\"timestamp\":\"" + ts + "\"}") );

  delay(60000); //time interval to be determined
}

