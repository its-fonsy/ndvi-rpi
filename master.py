#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Button

RX = Button(2)
TX = LED(3)
TX.on()

def init_sync():
    DELAY = 0.5
    """
    (MASTER)
    Three step init_sync:
    1. Receive RX from SLAVE
    2. Send TX to SLAVE
    3. Receive RX from SLAVE
    """
    print("Waiting for slave...")
    while(RX.is_released):
        pass
    print("Got RX, ensuring is active")
    TX.off()
    sleep(DELAY)
    TX.on()
    while(RX.is_released):
        pass
    print("slave is active")

init_sync()
