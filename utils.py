#!/usr/bin/env python3

import os
import datetime


HOME = os.getenv("HOME")
PATH = HOME + "/flights/"


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
