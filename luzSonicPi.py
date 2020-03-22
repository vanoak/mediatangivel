DEBUG = True

import RPi.GPIO as GPIO
import time
from pathlib import Path
from psonic import *

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count + 1
    return count

def analog_read():
    discharge()
    return charge_time()

while True:
    value = analog_read()
    if value > 40 and value < 100:
        play(value)
        time.sleep(1)
