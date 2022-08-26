#include <AFMotor.h>
#include <string.h>
#include <Wire.h>

//Stepper Motor Setup
AF_Stepper leftmotor(200, 2); //200 steps, M3&M4
AF_Stepper rightmotor(200, 1); //200 steps, M1&M2

//Ultrasonic Sensor (I2C)
int distance = 0;
int stepsTraveled = 0;

//Collision
bool collision = false;

void setup() 
{
  Wire.begin();
  Serial.begin(9600); // set up Serial library at 9600 bps
  
//Stepper Motor Setup
  leftmotor.setSpeed(50);  // 100 rpm   
  rightmotor.setSpeed(50);  // 100 rpm   

//Ultrasonic Sensor (I2C)
  Wire.begin(9);
  Wire.onReceive(recieveEvent);
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

//Function for "recieveEvent"
void recieveEvent(int bytes)
{
  distance = Wire.read();
}

void loop() 
{
  //Waiting to recieve string from RPi
  if (Serial.available() > 0) {
    String instruction = Serial.readStringUntil(';');
    if (collision == false) { 
      //Breaking up the string and saving it into other strings
        String command = getValue(instruction,':',0);
        String value = getValue(instruction,':',1);
      //Converts string to int
        int steps = value.toInt();
      
        if(command == "F")    //Forward
        {
          for (int i=1;i<=steps;i++)
          {
            //Stepper Motor
            leftmotor.step(1, FORWARD, SINGLE); 
            rightmotor.step(1, FORWARD, SINGLE);
    
            //Steps Traveled
            stepsTraveled = i;

            //Collision
            if (distance <= 10) {
              i = steps;
              collision = true;
            }
          }
          //Printing the amount of steps traveled 
          char traveled[10];
          sprintf(traveled, "F:%d;", stepsTraveled);     
          Serial.println(traveled);
          if (collision == true){
            Serial.println("Collision;");
          }
          delay(1000);
        }
        else if (command == "B")    //Backward
        {
          for (int i=1;i<=steps;i++)
          {
            //Stepper Motor
            leftmotor.step(1, BACKWARD, SINGLE); 
            rightmotor.step(1, BACKWARD, SINGLE); 
    
            //Steps Traveled
            stepsTraveled = i;              
          } 
          //Printing the amount of steps traveled 
          char traveled[10];
          sprintf(traveled, "B:%d;", stepsTraveled);     
          Serial.println(traveled);
          delay(1000);
        }
        else if(command == "L")     //Left
        {
          for (int i=1;i<=steps;i++)
          {
            //Stepper Motor
            leftmotor.step(1, BACKWARD, SINGLE); 
            rightmotor.step(1, FORWARD, SINGLE); 
    
            //Steps Traveled
            stepsTraveled = i;
            
            //Collision
            if (distance <= 10) {
              i = steps;
              collision = true;
            }
          } 
          //Printing the amount of steps traveled 
          char traveled[10];
          sprintf(traveled, "L:%d;", stepsTraveled);     
          Serial.println(traveled);
          if (collision == true){
            Serial.println("Collision;");
          }
          delay(1000);       
        }
        else if(command == "R")     //Right
        {
          for (int i=1;i<=steps;i++)
          {
            //Stepper Motor
            leftmotor.step(1, FORWARD, SINGLE); 
            rightmotor.step(1, BACKWARD, SINGLE); 
    
            //Steps Traveled
            stepsTraveled = i;
            
            //Collision
            if (distance <= 10) {
              i = steps;
              collision = true;
            }
          } 
          //Printing the amount of steps traveled 
          char traveled[10];
          sprintf(traveled, "R:%d;", stepsTraveled);     
          Serial.println(traveled);
          if (collision == true){
            Serial.println("Collision;");
          }
          delay(1000);          
        }
    } 
    else if (collision == true) {
      if (instruction == "Reset") {
        collision = false;
      }
    }
  }
}
