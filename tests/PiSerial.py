#!/usr/bin/env python3

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

while True:
    #x = bytes("RUN", 'utf-8')
    ser.write(b"ON\n")
    print("ran")
    time.sleep(1)
