# sumobot scrach - RasPi Program

Sumobot controlled by Scrach <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi/raspi_sumobot_scrach.png" width="500" /> <br/>

## Program
Scratch :send broadcast message, when click the image <br/>
Python : receive broadcast message, and move sumobot <br/>

Correspondence of image and message.
- forward : "f"
- backward : "b"
- left : "l"
- right : "r"
- stop : "s"

### Requrement
- [py-scratch](https://code.google.com/archive/p/py-scratch/)

### setup
copy "sumobot.sb" under directory /home/pi/Scrach/ <br/>
copy "sumobot_scrach.py" under directory /home/pi/sumobot/ <br/>

### Usage
(1) connect to Raspberry Pi (Sumobot) using VNC <br/>

(2) start Scrach <br/>
(3) open file <br/>
file -> open -> sumobot.sb <br/>

(4) start terminal <br/> 
(5) excute python code <br/> 
> cd ~/sumobot/ <br/> 
sudo python sumobot_scrach.py <br/> 

(6) click image on Scrach
