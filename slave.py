#!/usr/bin/env python3

import os
import serial
from utils import PATH, gen_folder_name
from time import sleep, time
from picamera import PiCamera


ANS = False
DELAY = 0.2
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 )


def create_folder():
    global ANS

    # create the folder
    folder = gen_folder_name()

    while(not ANS):
        ans = ser.readline()
        if ans != b"":
            master_folder = ans.decode().strip()
            ANS = True
            if master_folder == folder:
                ser.write("1".encode())
            else:
                ser.write("0".encode())
                raise RuntimeError('Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH+folder


def main():

    folder = create_folder()
    print(folder)

    # camera = PiCamera()
    # camera.resolution = (1024, 768)
    # # Camera warm-up time
    # camera.start_preview()
    # sleep(2)
    # camera.capture('foo.jpg')


main()
