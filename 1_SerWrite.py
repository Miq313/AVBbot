import serial
import time

with open(os.getcwd()+"/Config.json", "r") as configFile:
    config = json.load(configFile)
    serialPort = config["serial"]
    
ser = serial.Serial(serialPort, 9600, timeout=1)
ser.flush()

#place all inside loop
#how to receive commands without calling entire file each time?
#x = bytes("F:10\n", 'utf-8')
ser.write(b"F:10\n")
print("F:10\n")

