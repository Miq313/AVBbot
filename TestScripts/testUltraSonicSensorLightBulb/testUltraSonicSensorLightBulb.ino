#include <Servo.h>
#define trigPin 8
#define echoPin 7
Servo servo;
int sound = 250;
void setup() {
  pinMode(9, OUTPUT);
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
  if (distance < 5) {
  digitalWrite(9,LOW);
  }
  else {
  digitalWrite(9,HIGH);
  }
  delay(500);
}
