#!/usr/bin/env python3

from gpiozero import LED, Button
from time import sleep

RX = Button(2)
TX = LED(3)
TX.on()

print("Waiting for RX")
while(not RX.is_pressed):
	pass
print("RX received!")

input("Press any key to send a signal")
TX.off()
sleep(1)
TX.on()
