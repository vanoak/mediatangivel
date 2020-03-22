DEBUG = False

import RPi.GPIO as GPIO
import time
from omxplayer.player import OMXPlayer
from pathlib import Path

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

if not DEBUG:
    VIDEO_PATH = "/home/pi/Videos/Kulning.mp4"
    player = OMXPlayer(VIDEO_PATH, args =['--no-osd','--loop'])
    player.set_aspect_mode('stretch')
    time.sleep(1)
    player.pause()

while True:

    value = analog_read()
    
    if not DEBUG:
        if value < 100:
            if not player.is_playing():
                player.play()
        else:
            player.pause()

    if DEBUG:
        print(analog_read())
    
    time.sleep(1)
