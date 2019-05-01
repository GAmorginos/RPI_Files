from time import sleep
import requests
import RPi.GPIO as GPIO
import spidev
import pyowm
import os


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 250000

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
#GPIO.output(15, GPIO.LOW)
garageOpen = False
count = 0
safe = True
#key used by openweathermap to enable to retrieve weather data
weatherObject = pyowm.OWM('6aedf1aa7d45610ac1e720360cf53274')
w = weatherObject.weather_at_place('Boone,US')
booneWeather = w.get_weather()
#using openweathermap gets the current status of the weather 
#in the Boone area
def getWeather():
    return booneWeather.get_status()
#this function opens the garage door a few inches, 
#adjusting the sleep time will coorespond to the amount
#the garage door will be open 
def openGarage():
    
    os.system('gpio write 16 1')
    os.system('gpio write 16 0')
    sleep(1)
    os.system('gpio write 16 1')
    os.system('gpio write 16 0')
    print('Garage is open')
    #safe = False
    return
#reads the signal comming from the ADC and returns a value that can be
#read as the level of water the sensor is reading
#channel 1 is the sensor, channel 0 is connected to a 10k ohm 
#potentiometer used for testing
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
        #will get information from the sensor
        channeldata = poll_sensor(1)
        #print(channeldata)
        voltage = round(((channeldata * 3300) / 1024), 0)
        #print('Voltage: {}'.format(voltage))
        #print('Data    :{}\n'.format(channeldata))
        if getWeather() == 'Rain':
            print('Weather says its raining')
            if voltage > 250:
                #GPIO.output(15, GPIO.HIGH)
                #print(voltage)
                print("The sensor has detected water.")
                count = count + 1
                if count > 5:
                    openGarage()
                    safe = False
            else:print(voltage)
        else:
            print("Weather calls for no rain.")
	    print(voltage)
            
        sleep(1)
        
finally:
    spi.close()
    #GPIO.cleanup()
    print ("\nThe Program has closed.") 

