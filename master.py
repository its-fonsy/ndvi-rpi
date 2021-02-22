#!/usr/bin/env python3

import os
import serial
from utils import PATH, gen_folder_name
from time import sleep, time
from picamera import PiCamera


DELAY = 0.2
ANS = False
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 )


def create_folder():

    global ANS

    # create the folder name
    folder = gen_folder_name()

    # ask the slave that the name of the folder is the same
    msg = f"{folder}\n"
    while(not ANS):
        ser.write(msg.encode())
        ans = ser.readline()
        if ans != b"":
            if ans.decode() == "1":
                ANS = True
            if ans.decode() == "0":
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
