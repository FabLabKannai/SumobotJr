// Command for Continuous Rotation Servo
// 2016-04-20 K.OHWADA @ FabLab Kannai
// Command to specify the rotation direction and speed
// Usage
//   s + three digits
//   s000 : clockwide full speed
//   s090 : stop
//   s180 : anticlockwide full speed
#include <Servo.h>
#define ERR -1       // Error
Servo myservo;
int PIN = 13;
void setup() { 
    Serial.begin(9600);  
    Serial.println("Start servo test"); 
    Serial.println("s + three digits, for example s090"); 
    myservo.attach(PIN);
    myservo.write(90); 
}
void loop() {
    char c; 
    if( Serial.available() ) {
        c = Serial.read();
        command( c );
    }
} 
void command( int c ) { 
    if ( c == 's' ) {
	int speed = readThreeDigit(180);
	Serial.println(speed);
	myservo.write(speed);
    }
}
// Read ASCII three digits
int readThreeDigit(int maximum) {
    int buf, digit;
    buf = readOneDigit();
    if(buf != ERR) { // first
        digit = buf * 100;
        buf = readOneDigit();
        if(buf != ERR) { // second
            digit += buf * 10;
            buf = readOneDigit();
            if(buf != ERR) { // third
                digit += buf;
                if(digit <= maximum) {
                    buf = digit;
                } else {
                    buf = ERR;
                }   
            } // third
        } // second
    } // first
    return buf;
}
// Read ASCII one digit
int readOneDigit() {
    int buf;
    while(!Serial.available()) {}
        buf = Serial.read() - 48;
        if(buf < 0 || 9 < buf){
            buf = ERR;
    }
    return buf;
}
