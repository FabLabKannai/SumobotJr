#! /usr/bin/env python
# Test for Continuous Rotation Servo
# 2016-05-01 K.OHWADA @ FabLab Kannai
# command
#   duty : 5 - 7.5 - 10

import RPi.GPIO as GPIO

#
# ServoDuty
#
# duty
#   5.0 : clockwide full speed
#   7.5 : stop
#   1.0 : anticlockwide low speed
#
class ServoDuty():
	servo = None

	def __init__(self, pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)
		self.servo = GPIO.PWM(pin, 50) # 50 Hz (20 ms)
		self.servo.start(7.5)

	def stop(self):
		self.servo.stop()
		GPIO.cleanup()
		
	def change(self, duty):
		self.servo.ChangeDutyCycle(duty)

# end of class

# main
PIN =15
servo = ServoDuty(PIN)

try:
	# endless loop
	while True:
		# wait to enter command
		duty = input('> ')
		# exit the loop, if duty is invalid
		if duty > 10: break
		servo.change(duty)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.stop()	
# end of main
