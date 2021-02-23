#!/usr/bin/env python3

import os
import serial
from utils import ser, PATH, gen_folder_name, send_message, receive_message
from time import sleep, time
from picamera import PiCamera


# Initiate the Pi camera
camera = PiCamera()
camera.resolution = (3280, 2464)
# Camera warm-up time
camera.start_preview()
sleep(2)


def create_folder():

    # create the folder
    folder = gen_folder_name()

    # check if the folder of MASTER is the same
    receive_message(folder, 'Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH + folder + '/'


def shot(n, folder):
    # wait "n" from MASTER
    if (n < 10):
        photo = "0%d_rgb.jpg" % n
    else:
        photo = "%d_rgb.jpg" % n

    print("Going to shot %s" % photo)
    receive_message(str(n), 'Photo name not synced')

    # wait MASTER to shoot the photo
    receive_message("shoot", 'Photo not shooted')
    camera.capture(folder+photo)

    # confirm to MASTER to have shooted
    send_message("shooted", 'Photo not shooted')
    print("Shot %d_rgb.png\n" % n)


def main():

    folder = create_folder()

    MAX = 10
    for n in range(MAX):
        shot(n+1, folder)


main()
