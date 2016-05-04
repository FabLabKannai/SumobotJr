// Test for Continuous Rotation Servo
//   using digitalWrite
// 2016-04-20 K.OHWADA @ FabLab Kannai
// pulse width :  500 - 2500 us
//   500 - 1500 : clockwide
//   1500 : stop
//   1500 - 2500 : anticlockwide
// pulse interval : 20 ms 
int PIN = 13;
int width = 1500;  // us
void setup() {
 	pinMode(PIN, OUTPUT);
}
void loop() {
	digitalWrite(PIN, HIGH);
	delayMicroseconds(width);
	digitalWrite(PIN, LOW);
	delayMicroseconds(3000 - width);
	delay(17); // wait 17 ms
}
