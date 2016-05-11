# Sumobot servo command
# 2016-05-01 K.OHWADA @ FabLab Kannai

import time
import RPi.GPIO as GPIO

#
# TwinServo class
#
# Usage
#    f : forward
#    b : backward
#    l : left turn
#    r : right turn
#   othes : stop
#
class TwinServo():
	OFFSET_L = -20.0
	OFFSET_R = -20.0	
	servo_l = None
	servo_r = None

	def __init__(self):
		self.servo_l = ServoSpeed()
		self.servo_r = ServoSpeed()
		self.servo_l.setOffset(self.OFFSET_L)
		self.servo_r.setOffset(self.OFFSET_R)

	def setPin(self, pin_l, pin_r):
		self.servo_l.setPinMode()
#		self.servo_r.setPinMode()
		self.servo_l.setPin(pin_l)
		self.servo_r.setPin(pin_r)		
		self.servo_l.start()
		self.servo_r.start()

	def change(self, speed_l, speed_r):
		self.servo_l.change(speed_l)
		self.servo_r.change(speed_r)

	def command(self, c):
		if c == 'f':
			print 'forward'
			self.change(100, -100)
		elif c == 'b':
			print 'backward'
			self.change(-100, 100)
		elif c == 'l':
			print 'left'
			self.change(-100, -100)
		elif c == 'r':
			print 'right'
			self.change(100, 100)
		else:
			print 'stop'
			self.change(0, 0)

	def stop(self):
		self.servo_l.stop()
		self.servo_r.stop()
		self.servo_l.cleanupGpio()
#		self.servo_r.cleanupGpio()
							
# end of class

#
# ServoSpeed class
#
# Servo: SpringRC SM-S4303R
#   -100 : clokckwide full-speed
#   0 : stop
#   100 : anticlokckwide full-speed
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

	def __init__(self):
		pass

	def setDebugPrint(self, debug):
		self.debugPrint = bool(debug)

	def setOffset(self, offset):
		self.dutyOffset = self.COEF * float(offset)

	def setPinMode(self):
		GPIO.setmode(GPIO.BOARD)

	def setPin(self, pin):
		self.pin = int(pin)
		GPIO.setup(self.pin, GPIO.OUT)

	def start(self):
		self.servo = GPIO.PWM(self.pin, self.FREQ)
		duty = self.calcDuty(0)
		self.servo.start(duty)

	def stop(self):
		self.servo.stop()

	def cleanupGpio(self):
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