#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Button

DELAY = 0.2
RX = Button(2)
TX = LED(3)
TX.on()


def send_TX():
    TX.off()
    sleep(DELAY)
    TX.on()


def init_sync():
    """
    (SLAVE)
    Three step init_sync:
    1. Wait TX from MASTER
    2. Send TX to MASTER
    3. Wait TX from MASTER
    """
    # Step 1
    print("Waiting for master TX")
    RX.wait_for_press()
    print("Received TX")

    # Step 2
    sleep(1)
    print("Sending TX to slave")
    TX.off()

    # Step 3
    RX.wait_for_press()
    print("Received final TX")
    TX.on()

    return True


init_sync()
