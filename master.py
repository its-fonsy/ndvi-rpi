#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Button

RX = Button(2)
TX = LED(3)
TX.on()


def send_TX():
    TX.off()
    sleep(DELAY)
    TX.on()


def init_sync():
    DELAY = 0.2
    """
    (MASTER)
    Three step init_sync:
    1. Receive RX from SLAVE
    2. Send TX to SLAVE
    3. Receive RX from SLAVE
    """
    # Step 1
    print("Waiting for slave RX")
    RX.wait_for_press()
    print("Received RX")

    # Step 2
    sleep(1)
    print("Sending TX to slave")
    TX.off()

    # Step 3
    RX.wait_for_press()
    print("Received final RX")

init_sync()
