#include <Servo.h>

Servo servothumb;          
Servo servoindex;          
Servo servomiddle;
Servo servoring;
Servo servopinky;

char c;

int thumb, index, middle, ring, pinky; 

String serial_output; 

void setup() {

  Serial.begin(9600);
  servothumb.attach(10);  
  servoindex.attach(7);  
  servopinky.attach(8);
  servoring.attach(11);
  servomiddle.attach(9); 

  servothumb.write(0);  
  servoindex.write(0);  
  servopinky.write(0);
  servoring.write(0);
  servomiddle.write(0);

  
}

void loop() {
  
DataProcessing();

Serial.print("Angles: ");
Serial.print(thumb);
Serial.print(" ");
Serial.print(index);
Serial.print(" ");
Serial.print(middle);
Serial.print(" ");
Serial.print(ring);
Serial.print(" ");
Serial.print(pinky);


servothumb.write(thumb); 
servoindex.write(index); 
servomiddle.write(middle);
servoring.write(ring); 
servopinky.write(pinky); 
}


void DataProcessing() {
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
