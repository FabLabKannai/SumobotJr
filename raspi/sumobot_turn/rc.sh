#!/bin/sh
# change /etc/rc.local
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp -p /etc/rc.local /etc/rc.local.orig
cp -f sumobot_turn.rc.local /etc/rc.local
chmod 755 /etc/rc.local
