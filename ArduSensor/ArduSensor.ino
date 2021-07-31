#include <Wire.h>

const int trigPin = 8;
const int echoPin = 7;
long duration;
int distance;

void setup() {
Wire.begin();
Serial.begin(9600);

pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
}

void loop() {
 digitalWrite(trigPin, LOW);
 delayMicroseconds(2);
 digitalWrite(trigPin, HIGH);
 delayMicroseconds(10);
 digitalWrite(trigPin, LOW);
 duration = pulseIn(echoPin, HIGH);
 distance = (duration/2) / 29.1;

  Wire.beginTransmission(9);
  Wire.write(distance);
  Wire.endTransmission();
  delay(100);
}
