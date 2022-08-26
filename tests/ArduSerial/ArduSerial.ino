//#include <AFMotor.h>

int led = 7;
//AF_Stepper motor1(200,1);

void setup() {
  Serial.begin(9600);
  //motor1.setSpeed(100);
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == "ON") {
      //motor1.step(200, FORWARD, SINGLE);
      digitalWrite(led, HIGH);
    } else {
      digitalWrite(led, LOW);
    }
  }  
}
