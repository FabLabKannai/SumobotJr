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

### Install sumobot wii
> $ cd /tmp <br/>
> $ git clone https://github.com/FabLabKannai/SumobotJr.git <br/> 
> $ mkdir ~/sumobot/ <br/>
> $ cp SumobotJr/raspi/sumobot_wii/sumobot_wii_remote.py ~/sumobot/ <br/>

### Usage

**Connnect** <br/>
RaspberryPi is bootted. <br/>
and after about three minutes, LED will be trun on. <br/>
push 1 and 2, when LED on. <br/>
come to light vibration, when connect wii remote to RaspberryPi. <br/>

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

### Start Automatically 1
Set to start this program, when the power is turned on. <br/>
Change /etc/rc.local <br/>
Add one line before "exit 0" <br/>
> $ sudo cp -p /etc/rc.local /etc/rc.local.orig <br/>
$ sudo nano /etc/rc.local <br/>
... <br/>
\# add <br/>
python /home/pi/sumobot/sumobot_wii_remote.py & <br/>
exit 0  <br/>

### Start Automatically 2
Alternative to change /etc/rc.local <br/>
> $ cd /tmp/SumobotJr/raspi/sumobot_wii/  <br/> 
$ sudo cp -p /etc/rc.local /etc/rc.local.orig   <br/>
$ sudo cp -f rc.local.sumobot_wii /etc/rc.local   <br/>
$ sudo chmod 755 /etc/rc.local   <br/>

### Hardwear setup
for sumobot_wii_remote_check.py <br/> 
Put a 10k resistor between P13(GPIO 27) and P20(GND).  <br/>
