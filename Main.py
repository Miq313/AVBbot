import SerWrite

#Run SerRead.py in a seperate thread
x = 0
while x!=10000:
    SerWrite.serWrite("F:200")
    SerWrite.serWrite("B:200")
    SerWrite.serWrite("R:200")
    SerWrite.serWrite("L:200")
    x+=1