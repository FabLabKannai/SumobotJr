#!/bin/sh
# Sumobot init
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp scripts/sumobot-web-sample.init /etc/init.d/sumobot-web-sample
chmod 755 /etc/init.d/sumobot-web-sample
cp scripts/sumobot-web-sample.default /etc/default/sumobot-web-sample
chmod 644 /etc/default/sumobot-web-sample
insserv sumobot-web-sample
systemctl daemon-reload
