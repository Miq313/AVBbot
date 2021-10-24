import RPi.GPIO as GPIO
import time
 
#Initialize GPIO
GPIO.setmode(GPIO.BCM)

GPIOtrig = 18
GPIO.setup(GPIOtrig, GPIO.OUT)
GPIOecho = 24
GPIO.setup(GPIOecho, GPIO.IN)
 
def distance():
    GPIO.output(GPIOtrig, True)
    time.sleep(0.00001)
    GPIO.output(GPIOtrig, False)
 
    startTime = time.time()
    stopTime = time.time()
    while GPIO.input(GPIOecho) == 0:
        startTime = time.time()
    while GPIO.input(GPIOecho) == 1:
        stopTime = time.time()
 
    TimeElapsed = stopTime - startTime
    distance = (TimeElapsed * 34300) / 2 # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
 
    return distance