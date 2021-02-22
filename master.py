#!/usr/bin/env python3

import os
import serial
from utils import ser, PATH, gen_folder_name, send_message, receive_message
from time import sleep, time
from picamera import PiCamera


DELAY = 0.2


def create_folder():

    # get the folder name
    folder = gen_folder_name()

    # ask the SLAVE that the name of the folder is the same
    send_message(folder, 'Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH+folder


def shot(n):
    # MASTER send "n"
    print("Going to shot %d_rgb.png" % n)
    send_message(n, 'Photo name not synced')
    photo = "%d_ir.png" % n
    sleep(0.2)

    # MASTER say the SLAVE to shoot a photo
    send_message("shoot", 'Photo not shooted')
    print("shoot")

    # Wait the SLAVE to confirm
    receive_message("shooted", 'Photo not shooted')
    print("Shot %d_rgb.png\n" % n)


def main():

    # folder = create_folder()

    MAX = 100
    for n in range(MAX):
        sleep(1)
        shot(n+1)

    # camera = PiCamera()
    # camera.resolution = (1024, 768)
    # # Camera warm-up time
    # camera.start_preview()
    # sleep(2)
    # camera.capture('foo.jpg')

main()
