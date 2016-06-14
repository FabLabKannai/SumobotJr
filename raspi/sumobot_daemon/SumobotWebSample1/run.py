#!/usr/bin/env python
# Sumobot run
# 2016-05-01 K.OHWADA @ FabLab Kannai

import os
import sys

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(basedir, "src"))

import sumobot_web_sample_1
sumobot_web_sample_1.main()
