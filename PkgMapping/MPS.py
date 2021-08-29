import math
import json
import os

#Initializing robot's parameters
with open(os.getcwd()+"/Config.json", "r") as configFile:
    # If it needs to get CurPos.json from parent dir:
    ## "/".join(os.getcwd().split("/")[0:-1])+"/CurPos.json"
    config = json.load(configFile)
    wheelDiameter = float(config["hardware"]["wheelDiameter"]) #mm
    stepAngle = math.radians(float(config["hardware"]["stepAngle"])) #rads
    axelLength = float(config["hardware"]["axelLength"]) #mm

#Calculating other robot parameters
wheelRadius = wheelDiameter/2
stepDistance = stepAngle*wheelRadius
axelRadius = axelLength/2

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

def updateCurPos(arduResponse):
    #Reading input from arduino
    arduinoInp = arduResponse
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
        deltaX = math.cos(math.radians(curPos["direction"]))*travDist*stepDistance
        deltaY = math.sin(math.radians(curPos["direction"]))*travDist*stepDistance
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