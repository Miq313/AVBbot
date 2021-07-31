import serial
import os
import json

with open(os.getcwd()+"/Config.json", "r") as configFile:
    config = json.load(configFile)
    serialPort = config["serial"]
    
ser = serial.Serial(serialPort, 9600, timeout=1)
ser.flush()

def serWrite(command):
    commandByt = bytes(command + ";", 'utf-8')
    ser.write(commandByt)
    print("Sent " + command + " to  ArduControl")