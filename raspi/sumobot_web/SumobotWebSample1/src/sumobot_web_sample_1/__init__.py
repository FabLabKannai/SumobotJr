#!/usr/bin/env python
# Sumobot Web Sample main
# 2016-05-01 K.OHWADA @ FabLab Kannai

import sys
import argparse
from server import server_run

# constant
SERVER_HOST_DEFAULT = "0.0.0.0"
SERVER_PORT_DEFAULT = 6010
PIN_LED_DEFAULT = 17 # con-pin 11
PIN_BUTTON_DEFAULT = 27 # con-pin 13
PIN_SERVO_LEFT_DEFAULT = 12 # con-pin 32
PIN_SERVO_RIGHT_DEFAULT = 13 # con-pin 33

# main
def main():
    parser = argparse.ArgumentParser(prog="run")
    parser.add_argument("--host", action="store", type=str, dest="host",
        help="Specify the server hos")
    parser.add_argument("--port", action="store", type=int, dest="port",
        help="Specify the server port")  
    parser.add_argument("--pin_led", action="store", type=int, dest="pin_led",
        help="Specify the LED pin")
    parser.add_argument("--pin_button", action="store", type=int, dest="pin_button",
        help="Specify the Button pin")  
    parser.add_argument("--pin_left", action="store", type=int, dest="pin_left",
        help="Specify the servo left pin")
    parser.add_argument("--pin_right", action="store", type=int, dest="pin_right",
        help="Specify the servo right pin")
    args = parser.parse_args()
    host = initParam(args.host, SERVER_HOST_DEFAULT)
    port = initParam(args.port, SERVER_PORT_DEFAULT)
    pin_led = initParam(args.pin_led, PIN_LED_DEFAULT)
    pin_button = initParam(args.pin_button, PIN_BUTTON_DEFAULT)
    pin_left = initParam(args.pin_left, PIN_SERVO_LEFT_DEFAULT)
    pin_right = initParam(args.pin_right, PIN_SERVO_RIGHT_DEFAULT)
    server_run(host, port, pin_led, pin_button, pin_left, pin_right)

def initParam(param, default):
    if param is not None:
        val = param
    else:
        val = default
    return val

if __name__ == "__main__":
    main()
