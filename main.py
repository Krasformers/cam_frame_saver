#!/usr/bin/python3

# -*- coding:utf-8 -*-

import os
import time
from cam import Cam

TIME_SLEEP = os.environ['TIME_SLEEP']
LOGIN = os.environ['LOGIN']
PASSW = os.environ['PASSW']
ROOT_FOLDER = os.environ['ROOT_FOLDER']
IP_CAM_1 = os.environ['IP_CAM_1']
IP_CAM_2 = os.environ['IP_CAM_2']
IP_CAM_3 = os.environ['IP_CAM_3']

if not os.path.isdir(ROOT_FOLDER):
    os.system(f'mkdir {ROOT_FOLDER}')

CAMS = [
    Cam(LOGIN, PASSW, IP_CAM_1, ROOT_FOLDER),
    Cam(LOGIN, PASSW, IP_CAM_2, ROOT_FOLDER),
    Cam(LOGIN, PASSW, IP_CAM_3, ROOT_FOLDER),
]

if __name__ == "__main__":
    while True:
        for c in CAMS:
            c.save()
        time.sleep(TIME_SLEEP)

