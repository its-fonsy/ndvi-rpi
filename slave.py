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
    1. Send TX to MASTER
    2. Receive RX to SLAVE
    3. Send TX to MASTER
    """
    # Step 1
    print("Sending TX to master")
    TX.off()

    # Step 2
    print("Waiting RX from master")
    RX.wait_for_press(5)

    if not RX.is_pressed:
        return False
    else:
        TX.on()

    print("RX from master received")

    # Step 3
    sleep(1)
    print("Send last TX to master")
    send_TX()
    return True

while(not init_sync()):
    pass
