#include <Servo.h>

Servo servothumb;          
Servo servoindex;          
Servo servomiddle;
Servo servoring;
Servo servopinky;

char c;

int thumb, index, middle, ring, pinky; 

void setup() {

  Serial.begin(9600);
  servothumb.attach(10);  
  servoindex.attach(7);  
  servopinky.attach(8);
  servoring.attach(11);
  servomiddle.attach(9); 

  
}

void loop() {
  
receiveData();
servothumb.write(thumb); 
servoindex.write(index); 
servomiddle.write(middle);
servoring.write(ring); 
servopinky.write(pinky); 
}


void receiveData() {
  while (Serial.available()) {

  char c = Serial.read(); 
  
    if (c == '$') {
      thumb = Serial.parseInt(); 
      index = Serial.parseInt();
      middle = Serial.parseInt();
      ring = Serial.parseInt();
      pinky = Serial.parseInt();
    }
  }
}
