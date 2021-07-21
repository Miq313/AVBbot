import serial
import os
import json

import MPS

with open(os.getcwd()+"/Config.json", "r") as configFile:
    config = json.load(configFile)
    serialPort = config["serial"]
    
ser = serial.Serial(serialPort, 9600, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        arduOutput = ser.readline().decode('utf-8').rstrip()
        MPS.updatePos(arduOutput)