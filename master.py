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

    # get the folder name
    folder = gen_folder_name()

    # ask the SLAVE that the name of the folder is the same
    send_message(folder, 'Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH + folder + '/'


def shot(n, folder):
    # MASTER send "n"
    if (n < 10):
        photo = "0%d_ir.jpg" % n
    else:
        photo = "%d_ir.jpg" % n

    print("Going to shot %s" % photo)
    send_message(str(n), 'Photo name not synced')

    # MASTER say the SLAVE to shoot a photo
    send_message("shoot", 'Photo not shooted')
    camera.capture(folder+photo)

    # Wait the SLAVE to confirm
    receive_message("shooted", 'Photo not shooted')
    print("Shot %d_rgb.png\n" % n)


def main():

    folder = create_folder()

    MAX = 10
    for n in range(MAX):
        sleep(3)
        shot(n+1, folder)


main()
