#!/bin/sh
# Sumobot init
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp scripts/sumobot-web-sample-1.init /etc/init.d/sumobot-web-sample-1
chmod 755 /etc/init.d/sumobot-web-sample-1
cp scripts/sumobot-web-sample-1.default /etc/default/sumobot-web-sample-1
chmod 644 /etc/default/sumobot-web-sample-1
insserv sumobot-web-sample-1
systemctl daemon-reload
