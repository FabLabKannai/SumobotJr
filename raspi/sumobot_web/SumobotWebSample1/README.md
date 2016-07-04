Sumobot Web Sample 1
===============

Web app to control Sumobot <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi/raspi_sumobot_web_sample_1.png" width="300" /> <br/>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi_ver.jpg" width="200" /> <br/>

### Requirements
- OS: Raspbian <br/>
- Python 2.7 <br/>
- python-dev <br/>
$ sudo apt-get install python-dev <br/>
- [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) <br/>
$ sudo pip install virtualenv <br/>

### Install
> $ cd /tmp<br/>
$ git clone https://github.com/FabLabKannai/SumobotJr.git <br/>
$ mkdir ~/sumobot/ <br/>
$ mv SumobotJr/raspi/sumobot_web/SumobotWebSample1/ ~/sumobot/ <br/>

> $ cd ~/sumobot <br/>
$ virtualenv venv <br/>
( You do not need to excute this command more than once, if you excuted this at once. ) <br/>

> $ source venv/bin/activate <br/>
(venv) $ cd SumobotWebSample1 <br/>
(venv) $ python setup.py install <br/>
(venv) $ deactivate <br/>

you can use service daemon <br/>
> $ sudo sh init.sh <br/>

### Run
> $ cd ~<br/>
$ sudo sumobot/venv/bin/sumobot_web_sample_1 <br/>

or service daemon <br/>
> $ sudo /etc/init.d/sumobot-web-sample-1 start <br/>

### Quite service daemon
> $ sudo insserv -r sumobot-web-sample-1

### Usage
Access using web browser. <br/>
http://raspberrypi.local:6010/ <br/>

Firstly, click "wakeup" button. <br/>
Sumobot go forward or backward, when click arrow icon. <br/>
Finally, quit controller, when click "quit" button. <br/>
