#! /usr/bin/python3

import time
import sys
import pyautogui

referenceUnit = -395
limit = 115

import RPi.GPIO as GPIO
from hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()
hx.tare()

print("Tare done!")

while True:
    try:
        force = round(hx.get_weight(5))
        #print(force)
        
        if force >= limit:
            print("Click hit at " + str(force) + " lbs")
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')

        #time.sleep(0.01)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
