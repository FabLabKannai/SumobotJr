// Test for Continuous Rotation Servo
// 2016-04-20 K.OHWADA @ FabLab Kannai
// Behavior
//   clockwide <-> stop <-> anticlockwide
//   base on https://www.arduino.cc/en/Tutorial/Fade
#include <Servo.h> 
Servo myservo;
int PIN = 13;
int INTERVAL = 100; // ms
int speed = 90;  // speed
int fadeAmount = 5;    // how many points to fade the speed
void setup() { 
    myservo.attach(PIN);
    myservo.write(90);
} 
void loop() {
    myservo.write(speed);
    // change the speed for next time through the loop:
    speed = speed + fadeAmount;
    // reverse the direction of the fading at the ends of the fade:
    if (speed == 0 || speed == 180) {
        fadeAmount = -fadeAmount ;
    }
    // wait for 100 milliseconds
    delay(INTERVAL);
}
