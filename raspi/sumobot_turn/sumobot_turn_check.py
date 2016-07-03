#!/usr/bin/python
# Test for Sumobot
# 2016-06-01 K.OHWADA @ FabLab Kannai
# Behavior
#   reft turn <-> stop <-> right turn

import threading
import time
import wiringpi

#
# GpioController
#
# Usage
#    w : wakeup
#    q : quit
#    0 : LED Off
#    1 : LED On
#    2 : LED Blink
#    f : forward
#    b : backward
#    l : left turn
#    r : right turn
#   othes : stop
#
#    speed : -100 - 0 - 100
#
class GpioController():
	TIME_QUIT = 0.5  # 0.5 sec
	BUTTON_NONE = -1
	BUTTON_OFF = 0
	BUTTON_ON = 1	
	ledThread = None
	servoLeft = None
	servoRight = None		
	pinLed = 0
	pinButton = 0
	isRun = False
	isFirst = True
	isRunServo = False
	
	def __init__(self):
		pass

	def setPin(self, pin_led, pin_button, pin_servo_left, pin_servo_right):
		self.pinLed = int(pin_led)
		self.pinButton = int(pin_button)
		self.servoLeft = ServoSpeed(pin_servo_left)
		self.servoRight = ServoSpeed(pin_servo_right)
		
	def setDebugPrint(self, flag):
		self.servo.setDebugPrint(flag)

	def wakeup(self):
		if self.isFirst:
			# setup, if first
			self.isFirst = False
			wiringpi.wiringPiSetupGpio()
			wiringpi.pinMode(self.pinLed, wiringpi.OUTPUT)
			wiringpi.pinMode(self.pinButton, wiringpi.INPUT)
		self.quitLed()
		self.ledThread = LedThread(self.pinLed)
		self.ledThread.startRun()
		self.ledThread.startBlink()
#		self.wakeupServo()

	def wakeupServo(self):
		self.isRunServo = True
		self.servoLeft.setPinMode()
		self.servoRight.setPinMode()
		self.servoLeft.setPwm()
#		self.servoRight.setPwm()
		self.servoLeft.stop()
		self.servoRight.stop()
		
	def quit(self):
		self.quitLed()
		self.quitSrervo()

	def quitLed(self):
		if self.ledThread:
			# remove LED Thread
			self.ledThread.stopBlink()
			self.ledThread.stopRun()
			time.sleep(self.TIME_QUIT)	
			self.ledThread = None
		wiringpi.digitalWrite(self.pinLed, wiringpi.LOW) 

	def quitSrervo(self):
		if self.isRunServo:
			self.isRunServo = False
			self.servoLeft.quit()
			self.servoRight.quit()

	def command(self, c):
		if c == 'w':
			if not self.isRun: 
				# Wakeup, if not run
				print 'Wakeup'
				self.isRun = True
				self.wakeup()
		elif not self.isRun:
			# nothing to do, if not run
			return
		elif c == 'q':
			# Qiut
			print 'Qiut'
			self.isRun = False
			self.quit()
		elif c == '0':
			# LED off
			print 'LED off'
			self.stopBlink()
			wiringpi.digitalWrite(self.pinLed, wiringpi.LOW) 
		elif c == '1':			
			# LED on
			print 'LED on'
			self.stopBlink()
			wiringpi.digitalWrite(self.pinLed, wiringpi.HIGH) 
		elif c == '2':
			# LED blink
			print 'LED blink'
			self.startBlink()
		elif c == 'f':
			# forward
			print 'forward'
			self.changeSpeed(100, -100)
		elif c == 'b':
			# backward
			print 'backward'
			self.changeSpeed(-100, 100)
		elif c == 'l':
			# left turn
			print 'left turn'
			self.changeSpeed(-100, -100)
		elif c == 'r':
			# right turn
			print 'righ turn'
			self.changeSpeed(100, 100)
		else:
			# stop
			print 'stop'
			self.changeSpeed(0, 0)

	def startBlink(self):
		if self.ledThread:
			self.ledThread.startBlink()

	def stopBlink(self):
		if self.ledThread:
			self.ledThread.stopBlink()

	def changeSpeed(self, speed_left, speed_right):
		if self.isRun and self.isRunServo:
			# excute, if run
			self.servoLeft.change(speed_left)
			self.servoRight.change(speed_right)

	def getButtonStatus(self):
		ret = self.BUTTON_NONE
		if self.isRun:
			# excute, if run
			val = wiringpi.digitalRead(self.pinButton)
			ret = self.BUTTON_ON if val == wiringpi.HIGH else self.BUTTON_OFF
		return ret		
		
# end of class

#
# LED Thread class for blink
# 
class LedThread(threading.Thread):
	TIME_BLINK = 1.0  # 1 sec
	TIME_SLEEP = 0.1 # 0.1 sec
	MAX_CNT = int( TIME_BLINK / TIME_SLEEP )
	pin = 0
	isRun = False
	isBlink = False
	isStatus = False

	def __init__(self, pin):
		super(LedThread, self).__init__()
		self.pin = pin

	def startRun(self):
		self.isRun = True
		self.start()

	def stopRun(self):
		self.isRun = False
		
	def startBlink(self):
		self.isBlink = True

	def stopBlink(self):
		self.isBlink = False

	# run when isRun is true
	def run(self):
		cnt = 0
		while self.isRun:
			cnt += 1
			if cnt >= self.MAX_CNT:
				# every one second
				cnt = 0
				self.blink()
			time.sleep(self.TIME_SLEEP)

	# blink LED when isBlink is true
	def blink(self):
		if self.isBlink:
			self.isStatus = not self.isStatus
			wiringpi.digitalWrite(self.pin, self.isStatus)

# end of class

#
# ServoSpeed
#
# speed
#   -100 : clockwide full speed
#   0 : stop
#   100 : anticlockwide full speed
#
class ServoSpeed():
	# PWM base clock 19.2 MHz
	# PWM clock 200 KHz
	CLOCK = 96 # 96 = 19.2 MHz / 200 KHz
	RANGE = 4000 # 20ms * 200 KHz
	PULSE_STOP = 300 # 1.5ms  * 200 KHz
	COEF = 1.0 # 0.5ms  * 200 KHz / 100
	MIN_SPEED = -100
	STOP_SPEED = 0
	MAX_SPEED = 100
	pin = 0
	isDebugPrint = False
	pulseOffset = 0

	def __init__(self, pin):
		self.pin = int(pin)

	def setDebugPrint(self, debug):
		self.isDebugPrint = bool(debug)

	def setOffset(self, offset):
		self.pulseOffset = self.COEF * float(offset)
		if self.isDebugPrint: 
			print "offset; " + str(offset) + " -> " + str(self.pulseOffset)

	def setupGpio(self):
		wiringpi.wiringPiSetupGpio()

	def setPinMode(self):
		wiringpi.pinMode(self.pin, wiringpi.PWM_OUTPUT)
	
	def setPwm(self):
		wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
		wiringpi.pwmSetClock(self.CLOCK)
		wiringpi.pwmSetRange(self.RANGE)

	def stop(self):
		self.change(0) # stop
		
	def quit(self):
		wiringpi.pwmWrite(self.pin, 0) # no pluse

	def change(self, speed):
		pulse = self.calcPulse(speed)
		wiringpi.pwmWrite(self.pin, pulse)

	def calcPulse(self, speed):
		# -100 -> 200
		# 0 -> 300
		# 100 -> 400
		speed = float(speed)
		if speed < self.MIN_SPEED: speed = self.MIN_SPEED
		if speed > self.MAX_SPEED: speed = self.MAX_SPEED
		pulse = int( self.PULSE_STOP + self.pulseOffset + self.COEF * speed )
		if self.isDebugPrint: 
			print str(speed) + " -> " + str(pulse)
		return pulse

# end of class

# main
print "start sumobot turn"
PIN_LED = 17 # con-pin 11
PIN_BUTTON = 27 # con-pin 13
PIN_LEFT = 12 # con-pin 32
PIN_RIGHT = 13 # con-pin 33
TIME_CHECK = 3 # 3 sec 
TIME_INTERVAL = 0.1 # 0.1 sec
MIN_SPEED = -100
MAX_SPEED = 100

gpio = GpioController()
gpio.setPin(PIN_LED, PIN_BUTTON, PIN_LEFT, PIN_RIGHT)
gpio.command("w")

# check 
time.sleep(TIME_CHECK) # wait to check
if gpio.getButtonStatus() != GpioController.BUTTON_ON:
	# exit this program, if pin is off
	print "exit sumobot turn"
	gpio.quit()
	exit()

speed = 0
amount = 5
gpio.wakeupServo()
gpio.command("2")

try:
	# endless loop
	while True:
		gpio.changeSpeed(speed, speed)
		speed = speed + amount;
		if speed <= MIN_SPEED:
			speed = MIN_SPEED 	
			amount = -amount
		elif speed >= MAX_SPEED:
			speed = MAX_SPEED 	
			amount = -amount
		time.sleep(TIME_INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

gpio.quit()
# end of main
