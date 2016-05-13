#! /usr/bin/env python
# Test for Continuous Rotation Servo
# 2016-05-01 K.OHWADA @ FabLab Kannai
# Behavior
#   clockwide <-> stop <-> anticlockwide

import time
import RPi.GPIO as GPIO

#
# ServoSpeed
#
class ServoSpeed():
	FREQ = 50 # 50 Hz (20 ms)
	DUTY_STOP = 7.5 # 1.5ms / 20ms
	COEF = 0.025 # 2.5 / 100
	MIN_SPEED = -100
	STOP_SPEED = 0
	MAX_SPEED = 100	
	servo = None
	pin = 0
	debugPrint = False
	dutyOffset = 0

	def __init__(self, pin):
		self.pin = int(pin)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)

	def setDebugPrint(self, debug):
		self.debugPrint = bool(debug)

	def setOffset(self, offset):
		self.dutyOffset = self.COEF * float(offset)

	def start(self):
		self.servo = GPIO.PWM(self.pin, self.FREQ)
		duty = self.calcDuty(0)
		self.servo.start(duty)

	def stop(self):
		self.servo.stop()
		GPIO.cleanup()

	def change(self, speed):
		duty = self.calcDuty(speed)
		self.servo.ChangeDutyCycle(duty)

	def calcDuty(self, speed):
		# -100 -> 5.0
		# 0 -> 7.5
		# 100 -> 10.0
		speed = float(speed)
		if speed < self.MIN_SPEED: speed = self.MIN_SPEED
		if speed > self.MAX_SPEED: speed = self.MAX_SPEED
		duty = self.DUTY_STOP + self.dutyOffset + self.COEF * speed
		if self.debugPrint: print duty
		return duty
		
# end of class

# main
PIN = 15
OFFSET = -18.0	
speed = 0
amount = 5
servo = ServoSpeed(PIN)
servo.setOffset(OFFSET)
servo.start()

try:
	# endless loop
	while True:
		servo.change(speed)
		speed = speed + amount;
		if speed <= -100 or speed >= 100:
			amount = -amount
		time.sleep(0.1)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.stop()
# end of main
