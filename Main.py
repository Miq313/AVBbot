import multiprocessing

from PkgSerial.SerWrite import serWrite
from PkgSerial.SerRead import serReadAndUpdateMPS

#Subprocess for reading serial output & updating MPS
def processSerRead():
    serReadAndUpdateMPS()

#Primary subprocess
def processMain():
    serWrite("F:200")
    serWrite("B:200")

process1 = multiprocessing.Process(target=processSerRead)
process2 = multiprocessing.Process(target=processMain)
process1.start()
process2.start()