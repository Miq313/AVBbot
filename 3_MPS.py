import math
import json
import os

#Reset position in the JSON file
def resetCurPos(x, y, dir):
    curPos = {
        "position": {
            "x": x,
            "y": y
        },
        "direction": dir
        }
    with open(os.getcwd()+"/CurPos.json", "w") as curPosFile:
        curPosFile.write(json.dumps(curPos, indent = 4))

#Initializing robot's parameters
wheelDiameter = float(67.4) #mm
stepAngle = math.radians(1.8) #rads
axelLength = float(100) #mm

#Calculating other robot parameters
wheelRadius = wheelDiameter/2
stepDistance = stepAngle*wheelRadius
axelRadius = axelLength/2

#NEEDS LOOP - reading input from arduino
arduinoInp = "R:300"
arduinoInp = arduinoInp.split(":")
travDir = str(arduinoInp[0])
travDist = float(arduinoInp[1])

#Reading current position from JSON
with open(os.getcwd()+"/CurPos.json", "r") as curPosFile:
    curPos = json.load(curPosFile)
    curPos["direction"] = float(curPos["direction"])
    curPos["position"]["x"] = float(curPos["position"]["x"])
    curPos["position"]["y"] = float(curPos["position"]["y"])

#Calculating change in position
if travDir == "F" or travDir == "B":
    deltaX = math.sin(math.radians(curPos["direction"]))*travDist*stepDistance
    deltaY = math.cos(math.radians(curPos["direction"]))*travDist*stepDistance
    if travDir == "B":
        deltaX = -deltaX
        deltaY = -deltaY
    #Updating new position
    curPos["position"]["x"] += deltaX
    curPos["position"]["y"] += deltaY
elif travDir == "R" or travDir == "L":
    deltaDir = math.degrees(math.atan(travDist/axelRadius))
    if travDir == "L":
        deltaDir = -deltaDir
    #Updating new position    
    curPos["direction"] += deltaDir

#Updating new position to JSON
with open(os.getcwd()+"/CurPos.json", "w") as curPosFile:
    curPosFile.write(json.dumps(curPos, indent = 4))

resetCurPos(0,0,90)