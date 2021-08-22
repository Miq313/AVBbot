import multiprocessing
import time

def p1():
    x=1
    while True:
        print(x)
        x+=1
        time.sleep(1)

def p2():
    x=100
    while True:
        print(x)
        x+=1
        time.sleep(1)

proc1 = multiprocessing.Process(target=p1)

proc2 = multiprocessing.Process(target=p2)

proc1.start()
proc2.start()