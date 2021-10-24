from os import getcwd
import math
import json

from PkgMapping.MappingClasses import Point,Line,showPlot

#Spatial data input, read from csv
with open(getcwd()+"/CartoSpatialData.csv", "r") as spatialDataFile:
    next(spatialDataFile)
    spatialLines = []
    wallPoints =[]
    for row in spatialDataFile:
        row = row.split(",")
        spatialLines.append(Line(Point(float(row[0]),float(row[1])),Point(float(row[2]),float(row[3]))))
        wallPoints.append(Point(float(row[2]),float(row[3])))

#Plot spatialLines for visualization purposes
for spatialLine in spatialLines:
    spatialLine.plot(color='black')

#Creating wall parameters by connecting all wallpoints with each other and checking which don't intersect with spatialLines
wallLines = []
for wallPoint in wallPoints:
    for wallPointConnecting in wallPoints:
        if wallPoint != wallPointConnecting:
            proposedWallLine = Line(wallPoint,wallPointConnecting)
            isCorrect = True
            for spatialLine in spatialLines:
                if proposedWallLine.intersects(spatialLine) and len(set([proposedWallLine.p1, proposedWallLine.p2, spatialLine.p1, spatialLine.p2])) == 4: #If intersects, but not including when intersects by the two lines sharing an endpoint
                    isCorrect = False
                    proposedWallLine.plot(color='r', linewidth=0.5)
            if isCorrect:
                wallLines.append(proposedWallLine)
                proposedWallLine.plot(color='g', linewidth=2)

#Creating grid based on extrema points
xMax = xMin = wallLines[0].p1.x
yMax = yMin = wallLines[0].p1.y
for wallLine in wallLines:
    xMax = max([wallLine.p1.x,wallLine.p2.x,xMax])
    xMin = min([wallLine.p1.x,wallLine.p2.x,xMin])
    yMax = max([wallLine.p1.y,wallLine.p2.y,yMax])
    yMin = min([wallLine.p1.y,wallLine.p2.y,yMin])

with open(getcwd()+"/Config.json", "r") as configFile:
    config = json.load(configFile)
    wallBuffer = float(config["hardware"]["maxChassisRadius"])*1.5 #cm
intervalX = intervalY = 5
numXPoints = int((math.ceil(xMax) - math.floor(xMin))/intervalX)
numYPoints = int((math.ceil(yMax) - math.floor(yMin))/intervalY)
gridPoints = []
for xPoints in range(0,numXPoints+1):
    for yPoints in range(0,numYPoints+1):
        xPoint = math.floor(xMin)+intervalX*xPoints
        yPoint = math.floor(yMin)+intervalY*yPoints
        gridPoint = Point(xPoint, yPoint)
        for wallLine in wallLines:
            if gridPoint.distanceToLine(wallLine) < wallBuffer:
                gridPoints.append(gridPoint)
                gridPoint.plot("y")
                break

showPlot()