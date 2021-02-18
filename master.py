#!/usr/bin/env python3

import serial
from time import sleep, time
from picamera import PiCamera

DELAY = 0.2
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 )


def main():

    camera = PiCamera()
    camera.resolution = (1024, 768)

    # Camera warm-up time
    camera.start_preview()
    sleep(2)

    camera.capture('foo.jpg')


counter = 1
while 1:
    msg = f"Counter is at: {counter}\n"
    sec = time()
    ser.write(msg.encode())

    msg += 'at: ' + str(sec)
    print(msg)
    sleep(1)
    counter += 1
