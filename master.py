#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, Buttoh

RX = Button(2)
TX = LED(3)
TX.on()

input("Press any key to send a signal")
TX.off()
sleep(1)
TX.on()
print("TX sent, waiting for response")
while(not RX.is_pressed):
    pass
print("RX received!")
