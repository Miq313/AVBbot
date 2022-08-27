import multiprocessing

import os, json, time
import serial

from scripts.cartography import create_map
from scripts.localization import get_cur_pos, update_cur_pos, reset_cur_pos
from scripts.navigation import navigate

config_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
with open(config_file_path, "r") as config_file:
    config = json.load(config_file)
    serial_port = config["communications"]["serialPort1"]

ser = serial.Serial(serial_port, 9600, timeout=1)
ser.flush()

def serial_write(command):
    command_bytes = bytes(command + ";", 'utf-8')
    ser.write(command_bytes)
    print("Sent " + command + " to  PicoControl")

# Subprocess for reading serial output & updating MPS
def process_serial_monitor():
    while True:
        if ser.in_waiting > 0:
            pico_output = ser.readline().decode('utf-8').rstrip().replace(";", "")
            print(pico_output)
            if pico_output == "Collision":
                time.sleep(1)
                serial_write("Reset")
            else:
                update_cur_pos(pico_output)

# Subprocess for controlling the robot
def process_main():
    # choose destination, find path, send commands to PicoControl
    serial_write("F:200")
    serial_write("B:200")

process1 = multiprocessing.Process(target=process_serial_monitor)
process2 = multiprocessing.Process(target=process_main)
process1.start()
process2.start()