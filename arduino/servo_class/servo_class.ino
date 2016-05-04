// Test for Continuous Rotation Servo
//   using Servo class
// 2016-04-20 K.OHWADA @ FabLab Kannai
// https://www.arduino.cc/en/Reference/ServoWrite
// On a continuous rotation servo,
// this will set the speed of the servo
// with 0 being full-speed in one direction, 
// 180 being full speed in the other, 
// and a value near 90 being no movement
#include <Servo.h>
Servo myservo;
int PIN = 13;
int speed = 180;
void setup() { 
	myservo.attach(PIN);
	myservo.write(speed);
} 
void loop() {
	// dummy
} 
