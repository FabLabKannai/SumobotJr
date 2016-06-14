# sumobot wii - RasPi Program

Sumobot controlled by Wii remote <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi_ver.jpg" width="300" /> <br/>

## Program
- sumobot wii remote <br/>
Sumobot run immediately, when the program is started. <br/>
- sumobot wii remote check <br/>
Program starts, and it checks the state of the P13 (GPIO 27). <br/>
Sumobot run, if pin is low. <br/>
Program stop, and Sumobot is stopped, if pin is high. <br/>

### Install libraly
> $ sudo apt-get install --no-install-recommends bluetooth <br/>
> $ sudo apt-get install python-cwiid <br/>

### Usage
**Connnect** <br/>
push 1 and 2, when LED on. <br/>

**Quit** <br/>
push +(plus) and -(minus) <br/>

**Control** <br/>
the arrow keys  <br/>
- up : forward <br/>
- down : backward <br/>
- left : turn left <br/>
- right : turn right <br/>

- -(minus) : LED off <br/>
- +(plus) : LED on <br/>
- 1 : LED blink <br/>
- others : nothing <br/>

### Start Automatically
Set to start this program, when the power is turned on. <br/>
Change /etc/rc.local <br/>
Add one line before "exit 0" <br/>
> $ sudo cp -p /etc/rc.local /etc/rc.local.orig <br/>
$ sudo nano /etc/rc.local <br/>
... <br/>
\# add <br/>
python /home/pi/sumobot/sumobot_wii_remote_check.py <br/>
exit 0  <br/>

### Hardwear setup
Put a 10k resistor between P13(GPIO 27) and P20(GND).  <br/>
