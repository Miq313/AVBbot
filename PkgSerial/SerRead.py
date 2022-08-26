import serial
import os
import json
import time

from PkgSerial.SerWrite import serWrite
from ..scripts.localization import update_cur_pos

with open(os.getcwd()+"/Config.json", "r") as configFile:
    config = json.load(configFile)
    serialPort = config["communications"]["serialPort1"]
    
ser = serial.Serial(serialPort, 9600, timeout=1)
ser.flush()

def serReadAndUpdateMPS():
    while True:
        if ser.in_waiting > 0:
            arduOutput = ser.readline().decode('utf-8').rstrip().replace(";", "")
            print(arduOutput)
            if arduOutput == "Collision":
                time.sleep(1)
                serWrite("Reset")
            else:
                update_cur_pos(arduOutput)