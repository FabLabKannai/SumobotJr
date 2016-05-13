#!/bin/sh
# Sumobot init
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp scripts/sumobot-sample.init /etc/init.d/sumobot-sample
chmod 755 /etc/init.d/sumobot-sample
cp scripts/sumobot-sample.default /etc/default/sumobot-sample
chmod 644 /etc/default/sumobot-sample
insserv sumobot-sample
systemctl daemon-reload
