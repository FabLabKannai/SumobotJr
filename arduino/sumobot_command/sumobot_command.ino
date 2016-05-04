// Sumobot Command
// 2016-04-20 K.OHWADA @ FabLab Kannai

// Command specify forward, backward or etc
// Usage
// command format : one ASCII charactor
//   0 : LED off
//   1 : LED on
//   2 : LED bilnk
//    f : forward
//    b : backward
//    l : left turn
//    r : right turn
//   othes : stop

// Servo
// SpringRC SM-S4303R
// 0 : clokckwide full-speed
// 90 : stop
// 180 : anticlokckwide full-speed

// Bluetooth module
// Microchip RN-42 Bluetooth Evaluation Kit

// Note
// AltSoftSerial is be NOT used
// Because ISR (Interrupt Signal Register) are colliding with Servo class
// Error message : multiple definition of `__vector_11'

#include <SoftwareSerial.h>
#include <Servo.h> 

// Pin
#define P_BT_RST      2
#define P_BT_RX        8
#define P_BT_TX        9
#define P_SERVO_L  10 
#define P_SERVO_R  11
#define P_LED          13

// Serial
#define SERIAL_SPEED  9600 
#define BT_SPEED  115200

SoftwareSerial softSerial(P_BT_RX, P_BT_TX);
Servo servo_l, servo_r;

int cnt = 0;
boolean isRun = false;
boolean isLed = false;
boolean isBlink = true;

// setup
void setup() {
    // serial
    Serial.begin(SERIAL_SPEED);
    softSerial.begin(BT_SPEED);
    // servo
    servo_l.attach(P_SERVO_L);
    servo_r.attach(P_SERVO_R);
    stop();
    // make the Bluetooth Module reset
    pinMode(P_BT_RST, OUTPUT);
    digitalWrite(P_BT_RST, LOW);
    delay(100);
    digitalWrite(P_BT_RST, HIGH);
    delay(500);
}
// loop
void loop() { 
    // command recieve
    char c; 
    if( Serial.available() ) {
        c = Serial.read();
        command( c );
    }
    if( softSerial.available() ) {
        c = softSerial.read();
        command( c );
    }
    // LED
    cnt ++;
    if (cnt>10) {
        cnt = 0;
        if ( isBlink ) {
            digitalWrite(P_LED, isLed); 
            isLed = !isLed;
        }       
    }
    delay(100);
}
// command
void command( int c ) { 
    if ( c == '0' ) {
        // LED off
        isBlink = false;
        digitalWrite(P_LED, LOW); 
    } else if ( c == '1' ) {
        // LED on
        isBlink = false;
        digitalWrite(P_LED, HIGH); 
    } else if ( c == '2' ) {
        // LED blink
        isBlink = true;
    } else if ( c == 'f' ) {
        // forward
        servo_l.write(180);
        servo_r.write(0);
    }  else if ( c == 'b' ) {
        // backward
        servo_l.write(0);
        servo_r.write(180);
    }  else if ( c == 'r' ) {
        // right turn
        servo_l.write(180);
        servo_r.write(180);	
    } else if ( c == 'l' ) {
        // left turn
        servo_l.write(0);
        servo_r.write(0);	 	
    } else {
        stop();
    } 
}
// stop
void stop() { 
    servo_l.write(90);
    servo_r.write(90);
}
