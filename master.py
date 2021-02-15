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
    """
    (MASTER)
    Three step init_sync:
    1. Send TX to SLAVE
    2. Receive RX from SLAVE
    3. Send TX to SLAVE
    """

    DELAY = 0.2

    # Step 1
    print("Sending TX to slave")
    TX.off()

    # Step 2
    print("Waiting for slave TX")
    RX.wait_for_press(5)
    if not RX.is_pressed:
        return False
    else:
        print("Received TX")
        TX.on()

    # Step 3
    sleep(1)
    print("Sending final TX to slave")
    TX.off()

    return True


while(not init_sync()):
    pass
