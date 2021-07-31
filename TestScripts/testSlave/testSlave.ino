#include <Wire.h>
int x = 0;

void setup() {
Serial.begin(9600);
pinMode (10, OUTPUT);

Wire.begin(9);
Wire.onReceive(receiveEvent);
}

void receiveEvent(int bytes){
  x = Wire.read();
  Serial.println(x);
}

void loop() {
if(x <= 10){
 digitalWrite(10, LOW);
 delay(100); 
}
else{
  digitalWrite(10, HIGH);
  delay(100);
  }
}
