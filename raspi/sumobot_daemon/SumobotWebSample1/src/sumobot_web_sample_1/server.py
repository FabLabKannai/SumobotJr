# Sumobot server with flask
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
from gpio import GpioController

# Flask start
app = Flask(__name__)
gpio = GpioController()

# server_run
def server_run(host, port, pin_led, pin_button, pin_left, pin_right):
	# MUST execute before app.run
	gpio.setPin(pin_led, pin_button, pin_left, pin_right)
	# always last
	app.run(host=str(host), port=int(port))

# route index
@app.route('/')
def show_index():
    return render_template('index.html')

# route action with post
@app.route('/action', methods=['POST'])
def action():
    if request.method == 'POST':
        do_post()
    return ''

# route status with get
@app.route('/status', methods=['GET'])
def status():
	ret = ''
	if request.method == 'GET':
		ret = do_get()
	return ret

# do post method
# get parameter, and control LED or Servo
def do_post():
	type = str(request.form['type'])
	val = str(request.form['value'])
    	if type == 'gpio':
    		gpio.command(val)

# do get method
# return button status
def do_get():
	status = gpio.getButtonStatus()
	json = "{\"status\":%d}" %(status)
	return json

# end of flask
