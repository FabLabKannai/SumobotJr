# sumobot turn - RasPi Program

Test for Sumobot using  continuous rotation servos <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi_ver.jpg" width="300" /> <br/>
Video [Sumobot with Raspberry Pi](https://www.youtube.com/watch?v=J9WRliGs7vI) <br/>

## Program
- sumobot turn <br/>
Sumobot run immediately, when the program is started. <br/>
- sumobot turn check <br/>
Program starts, and it checks the state of the P18.. <br/>
Sumobot run, if P18 is high. <br/>
Program stop, and Sumobot is stopped, if P18 is low. <br/>

### Behavior
clockwide <-> stop <-> anticlockwide <br/>

### Install
$ cd /tmp<br>
$ git clone https://github.com/FabLabKannai/SumobotJr.git <br>
$ mkdir ~/RaspiStudy/ <br>
$ mv SumobotJr/raspi/sumobot_turn/ ~/RaspiStudy/ <br>

Set to start this program, when the power is turned on. <br>
Change /etc/rc.local <br>
Add one line before "exit 0" <br>

> $ sudo nano /etc/rc.local <br>
... <br>
python /home/pi/RaspiStudy/sumobot_turn/sumobot_turn_check.py <br>
exit 0  <br>

### Hardwear setup
Put a 10k resistor between P18 and P17(3.3V).  <br>
Sumobot will run endless. <br>
Sumobot will be stopped, when connect to P20(GND) in place of the P17(3.3v).   <br>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi/raspi_circuit_p18.png" width="300" /> <br/>
