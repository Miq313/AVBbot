import RPi.GPIO as GPIO
import time
 
# Initialize GPIO
GPIO.setmode(GPIO.BCM)

GPIO_trig = 18
GPIO.setup(GPIO_trig, GPIO.OUT)
GPIO_echo = 24
GPIO.setup(GPIO_echo, GPIO.IN)
 
def get_distance():
    GPIO.output(GPIO_trig, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_trig, False)
 
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(GPIO_echo) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_echo) == 1:
        stop_time = time.time()
 
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2 # Multiply with the sonic speed (34300 cm/s) and divide by 2, because the wave travels there and back
 
    return distance