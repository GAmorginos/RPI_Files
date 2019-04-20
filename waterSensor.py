from time import sleep
import requests
import RPi.GPIO as GPIO
import spidev
import pyowm


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 250000

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
garageOpen = False
count = 0
safe = True

weatherObject = pyowm.OWM('6aedf1aa7d45610ac1e720360cf53274')
w = weatherObject.weather_at_place('Boone,US')
booneWeather = w.get_weather()

def getWeather():
    return booneWeather.get_status()

def poll_sensor(channel):
    assert 0 <= channel <= 1, 'ADC channel must be 0 or 1.'
    cbyte = 0b11000000
    if channel:
        cbyte = 0b11000000
    else:
        cbyte = 0b10000000 
    r = spi.xfer2([1, cbyte, 0])
    #print("r =", r)
    return ((r[1] & 31) << 6) + (r[2] >> 2)

try:
    
    while safe:
        if count > 5:
            GPIO.output(15, GPIO.HIGH)
            garageOpen = True
            sleep(.5)
            GPIO.output(15, GPIO.LOW)
            
        if garageOpen:
            print("Garage is Open")
            sleep(5)
            safe = False
        #GPIO.output(15, GPIO.LOW)
        channeldata = poll_sensor(1)
        #print(channeldata)
        voltage = round(((channeldata * 3300) / 1024), 0)
        #print('Voltage: {}'.format(voltage))
        #print('Data    :{}\n'.format(channeldata))
        if getWeather() == 'Rain':
            print('Weather says its raining')
            if voltage > 250:
                #GPIO.output(15, GPIO.HIGH)
                print(voltage)
                print("The sensor has detected water.")
                count = count + 1
            else:
                print(voltage)
            
        sleep(1)
        
finally:
    spi.close()
    GPIO.cleanup()
    print ("\nThe Program has closed.") 

