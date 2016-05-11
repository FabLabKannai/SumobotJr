# Sumobot server with flask
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
from servo import TwinServo

# Flask start
app = Flask(__name__)
servo = TwinServo()

# server_run
def server_run(host, port, pin_left, pin_right):
    app.run(host=str(host), port=int(port))
    servo.setPin(int(pin_left), int(pin_right))

# route index
@app.route('/')
def show_index():
    return render_template('index.html')

# route action with post
@app.route('/action', methods=['POST'])
def action():
    if request.method == 'POST':
        c = str(request.form['command'])
        servo.command(c)
    return ''

# end of flask
