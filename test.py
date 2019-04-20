#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)


    GPIO.output(15, GPIO.HIGH)
    sleep(.5)
    GPIO.output(15, GPIO.LOW)
    sleep(.5)
    
