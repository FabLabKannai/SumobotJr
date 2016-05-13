Sumobot Controller
===============

Web app to control Sumobot <br>
<img src="https://github.com/FabLabKannai/SumobotJr/blob/master/docs/raspi_ver.jpg" width="300" /> <br/>

### Requirements
- OS: Raspbian <br>
- Python 2.7 <br>
- python-dev <br>
$ sudo apt-get install python-dev <br>
- [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) <br>
$ sudo pip install virtualenv <br>

### Install
$ cd /tmp<br>
$ git clone https://github.com/FabLabKannai/SumobotJr.git <br>
$ mkdir ~/RaspiStudy/ <br>
$ mv SumobotJr/raspi/sumobot_daemon/SumobotSample/ ~/RaspiStudy/ <br>

$ cd ~/RaspiStudy <br>
$ virtualenv venv <br>
( You do not need to excute this command more than once, if you excuted this at once. ) <br>

$ source venv/bin/activate <br>
(venv) $ cd SumobotSample <br>
(venv) $ python setup.py install <br>
$ deactivate <br>

you can use service daemon <br>
$ sudo sh init.sh <br>

### Run
$ cd ~<br>
$ sudo RaspiStudy/venv/bin/sumobot_sample <br>

or service daemon <br>
$ sudo /etc/init.d/sumobot-sample start <br>

### Usage
Access using web browser. <br>
http://IP_ADDR:6010 <br>
