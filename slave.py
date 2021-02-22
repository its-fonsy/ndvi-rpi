#!/usr/bin/env python3

import os
import serial
from utils import ser, PATH, gen_folder_name, send_message, receive_message
from time import sleep, time
from picamera import PiCamera


DELAY = 0.2


def create_folder():

    # create the folder
    folder = gen_folder_name()

    # check if the folder of MASTER is the same
    receive_message(folder, 'Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH+folder


def shot(n):
    # wait "n" from MASTER
    print("Going to shot %d_rgb.png" % n)
    receive_message(str(n), 'Photo name not synced')
    photo = "%d_rgb.png" % n

    # wait MASTER to shoot the photo
    receive_message("shoot", 'Photo not shooted')
    print("shoot")

    # confirm to MASTER to have shooted
    send_message("shooted", 'Photo not shooted')
    print("Shot %d_rgb.png\n" % n)


def main():

    # folder = create_folder()

    MAX = 100
    for n in range(MAX):
        shot(n+1)

    # camera = PiCamera()
    # camera.resolution = (1024, 768)
    # # Camera warm-up time
    # camera.start_preview()
    # sleep(2)
    # camera.capture('foo.jpg')


main()
