#include <Servo.h>
#define trigPin 8
#define echoPin 7
Servo servo;
int sound = 250;
void setup() {
  pinMode(10, OUTPUT);
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
  if (distance < 10) {
  digitalWrite(10,LOW);
  }
  else {
  digitalWrite(10,HIGH);
  }
  delay(500);
}
