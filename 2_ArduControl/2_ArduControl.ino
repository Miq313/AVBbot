#include <AFMotor.h>
#include <string.h>

//Stepper Motor Setup
AF_Stepper leftmotor(200, 2); //200 steps, M3&M4
AF_Stepper rightmotor(200, 1); //200 steps, M1&M2

//Ultra Sonic Sensor Setup
const int trigPin = 8;
const int echoPin = 7;
long duration;
int distance;
int stepsTraveled;

void setup() 
{
  Serial.begin(9600); // set up Serial library at 9600 bps
  
//Stepper Motor Setup
  leftmotor.setSpeed(50);  // 100 rpm   
  rightmotor.setSpeed(50);  // 100 rpm   

//Ultra Sonic Sensor Setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, OUTPUT); 
}

//Function to break down the string
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void loop() 
{
  //Waiting to recieve string from RPi
  if (Serial.available() > 0) {
    String instruction = Serial.readStringUntil('\n');

  //Breaking up the string and saving it into other strings
    String command = getValue(instruction,':',0);
    String value = getValue(instruction,':',1);
  //Converts string to int
    int steps = value.toInt();
  
    if(command == "F")    //Forward
    {
      for (int i=0;i<steps;i++)
      {
        //Stepper Motor
        leftmotor.step(1, FORWARD, SINGLE); 
        rightmotor.step(1, FORWARD, SINGLE);

        //Ultra Sonic Sensor
        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);
        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        duration = pulseIn(echoPin, HIGH);
        distance = duration*0.034/2;          //Measurement in cm

        //Collision
        //if (distance <= 10)
        //{
        //stepsTraveled = i;
        //i = steps;          
        //}
      }
      //Printing the amount of steps traveled 
      //char traveled[10];
      //sprintf(traveled, "F:%d", stepsTraveled);     
      //Serial.print(traveled);
    }
    else if (command == "B")    //Backward
    {
      for (int i=0;i<steps;i++)
      {
        //Stepper Motor
        leftmotor.step(1, BACKWARD, SINGLE); 
        rightmotor.step(1, BACKWARD, SINGLE); 

        //Ultra Sonic Sensor
        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        duration = pulseIn(echoPin, HIGH);
        distance = duration*0.034/2;          //Measurement in cm

        //Collision
        if (distance <= 10)
        {
        stepsTraveled = i;
        i = steps;          
        }
      } 
      //Printing the amount of steps traveled 
      char traveled[10];
      sprintf(traveled, "B:%d", stepsTraveled);     
      Serial.print(traveled);       
    }
    else if(command == "L")     //Left
    {
      for (int i=0;i<steps;i++)
      {
        //Stepper Motor
        leftmotor.step(1, BACKWARD, SINGLE); 
        rightmotor.step(1, FORWARD, SINGLE); 

        //Ultra Sonic Sensor
        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        duration = pulseIn(echoPin, HIGH);
        distance = duration*0.034/2;          //Measurement in cm

        //Collision
        if (distance <= 10)
        {
        stepsTraveled = i;
        i = steps;          
        }
      } 
      //Printing the amount of steps traveled 
      char traveled[10];
      sprintf(traveled, "L:%d", stepsTraveled);     
      Serial.print(traveled);           
    }
    else if(command == "R")     //Right
    {
      for (int i=0;i<steps;i++)
      {
        //Stepper Motor
        leftmotor.step(1, FORWARD, SINGLE); 
        rightmotor.step(1, BACKWARD, SINGLE); 

        //Ultra Sonic Sensor
        digitalWrite(trigPin, LOW);
        delayMicroseconds(2);

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

        duration = pulseIn(echoPin, HIGH);
        distance = duration*0.034/2;          //Measurement in cm

        //Collision
        if (distance <= 10)
        {
        stepsTraveled = i;
        i = steps;          
        }
      } 
      //Printing the amount of steps traveled 
      char traveled[10];
      sprintf(traveled, "R:%d", stepsTraveled);     
      Serial.print(traveled);           
    }
  } 
}
