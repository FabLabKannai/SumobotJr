# sumobot turn - RasPi Program

Test for Sumobot using  continuous rotation servos <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi_ver.jpg" width="300" /> <br/>
Video [Sumobot with Raspberry Pi](https://www.youtube.com/watch?v=J9WRliGs7vI) <br/>

## Program
- sumobot turn <br/>
Sumobot run immediately, when the program is started. <br/>
- sumobot turn check <br/>
Program starts, and it checks the state of the P13(GPIO 27). <br/>
Sumobot run, if pin is high. <br/>
Program stop, and Sumobot is stopped, if pin is low. <br/>

### Behavior
clockwide <-> stop <-> anticlockwide <br/>

### Install
> $ cd /tmp<br/>
$ git clone https://github.com/FabLabKannai/SumobotJr.git <br/>
$ mkdir ~/sumobot/ <br/>
$ cp SumobotJr/raspi/sumobot_turn/sumobot_turn_check.py ~/sumobot/ <br/>

### Start Automatically 1
Set to start this program, when the power is turned on. <br/>
Change /etc/rc.local <br/>
Add one line before "exit 0" <br/>
> $ sudo cp -p /etc/rc.local /etc/rc.local.orig <br/>
$ sudo nano /etc/rc.local <br/>
... <br/>
\# add <br/>
python /home/pi/sumobot/sumobot_turn_check.py <br/>
exit 0  <br/>

### Start Automatically 2
Alternative to change /etc/rc.local <br/>
> $ cd /tmp/SumobotJr/raspi/sumobot_turn/ <br/>
$ sudo cp -p /etc/rc.local /etc/rc.local.orig <br/>
$ sudo cp -f rc.local.sumobot_turn /etc/rc.local <br/>
$ sudo chmod 755 /etc/rc.local <br/>

### Quit to start automatically
Revert to the original /etc/rc.local
> $ sudo cp /etc/rc.local.orig /etc/rc.local

### Hardwear setup
Put a 10k resistor between P13(GPIO 27) and P17(3.3V).  <br/>
Sumobot will run endless. <br/>
Sumobot will be stopped, when connect to P20(GND) in place of the P17(3.3v).   <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi/raspi_circuit_p13.png" width="300" /> <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6819
