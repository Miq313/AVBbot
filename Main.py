import multiprocessing

import SerWrite as ModuleSerWrite
import SerRead as ModuleSerRead

#Subprocess for reading serial output
def serReadProcess():
    ModuleSerRead.serRead()

#Primary subprocess
def mainProcess():
    ModuleSerWrite.serWrite("F:200")
    ModuleSerWrite.serWrite("B:200")

process1 = multiprocessing.Process(target=serReadProcess)
process2 = multiprocessing.Process(target=mainProcess)
process1.start()
process2.start()