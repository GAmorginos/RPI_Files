from time import sleep
import requests
import RPi.GPIO as GPIO
import spidev
#import pyowm
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)


while 1:
    GPIO.output(15, GPIO.HIGH)
    sleep(1)
    GPIO.output(15, GPIO.LOW)
    sleep(1)
