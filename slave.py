#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Button

RX = Button(2)
TX = LED(3)
TX.on()

def init_sync():
    DELAY = 0.5
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
    sleep(DELAY)
    TX.on()

    # Step 2
    while(RX.is_released):
        pass

    # Step 3
    print("Got RX from master, confirm active slave")
    TX.off()
    sleep(DELAY)
    TX.on()

init_sync()
