#!/usr/bin/env python3

import os
import datetime
import serial


HOME = os.getenv("HOME")
PATH = HOME + "/flights/"
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1 )


def receive_message(expectation, error):
    while( True ):
        ans = ser.readline()
        if ans != b"":
            message = ans.decode().strip()
            print("DEBUG: The message is: ", message)
            print("DEBUG: Expected: ", expectation)
            if message == expectation:
                ser.write("1\n".encode())
                return None
            else:
                ser.write("0\n".encode())
                raise RuntimeError(error)


def send_message(message, error):
    msg = f"{message}\n"
    while( True ):
        ser.write(msg.encode())
        print("DEBUG: The message is: ", msg)
        ans = ser.readline()
        if ans != b"":
            answer= ans.decode().strip()
            print("DEBUG: answer: ", answer)
            if answer == "1":
                return None
            if answer == "0":
                raise RuntimeError(error)


def gen_folder_name():

    # date of the folder
    now = datetime.datetime.now()

    if now.day < 10:
        day = "0" + str(now.day)
    else:
        day = str(now.day)

    if now.month < 10:
        month = "0" + str(now.month)
    else:
        month = str(now.month)

    folder_date = str(now.year) + "-" + month + "-" + day

    # separate multiple flight done on the same day
    n = 1
    for folder in os.listdir(PATH):
        if folder_date in folder:
            n += 1

    folder = folder_date + "_flight_" + str(n)
    return folder
