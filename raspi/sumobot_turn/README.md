# sumobot turn - RasPi Program

Test for Sumobot using  continuous rotation servos <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/images/raspi_completion.jpg" width="300" /> <br/>
  Video [20160501 Sumobot Jr](https://www.youtube.com/watch?v=J9WRliGs7vI) <br/>

## Program
- sumobot turn <br/>
Sumobot run immediately, when the program is started. <br/>
- sumobot turn auto <br/>
Sumobot run, after check the state of the switch pin, when the program is started. <br/>

### Behavior
clockwide <-> stop <-> anticlockwide <br/>

### Install
$ cd /tmp<br>
$ git clone https://github.com/FabLabKannai/SumobotJr.git <br>
$ mkdir ~/RaspiStudy/ <br>
$ mv SumobotJr/raspi/sumobot_turn/ ~/RaspiStudy/ <br>

Set to start this program, when the power is turned on. <br>
Change /etc/rc.local <br>
$ sudo nano /etc/rc.local <br>
insert "python /home/pi/SumobotJr/raspi/sumobot_turn/sumobot_turn_auto.py" before "exit 0" <br>
