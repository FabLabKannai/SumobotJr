// Test for Sumobot
// 2016-04-20 K.OHWADA @ FabLab Kannai
// Behavior
//   reft turn <-> stop <-> right turn
#include <Servo.h> 
Servo servo_l, servo_r;
int PIN_L = 10;
int PIN_R = 11;
int INTERVAL = 100; // ms
int speed = 90;  // speed
int fadeAmount = 5;    // how many points to fade the speed
void setup() { 
    servo_l.attach(PIN_L);
    servo_l.write(speed);
    servo_r.attach(PIN_R);
    servo_r.write(speed);
} 
void loop() {
    servo_l.write(speed);
    servo_r.write(speed);
    speed = speed + fadeAmount;
    if (speed == 0 || speed == 180) {
        fadeAmount = -fadeAmount ;
    }
    delay(INTERVAL);
}
