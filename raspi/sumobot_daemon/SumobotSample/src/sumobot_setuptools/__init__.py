# Sumobot setuptools
# 2016-05-01 K.OHWADA @ FabLab Kannai

from __future__ import absolute_import

__author__ = "Kenichi Ohwada"

import os
import shutil
import glob
from setuptools import Command

# package_data_dirs
def package_data_dirs(source, sub_folders):
    import os
    dirs = []
    for d in sub_folders:
        folder = os.path.join(source, d)
        if not os.path.exists(folder):
            continue
        for dirname, _, files in os.walk(folder):
            dirname = os.path.relpath(dirname, source)
            for f in files:
                dirs.append(os.path.join(dirname, f))
    return dirs
