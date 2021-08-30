import math
import matplotlib.pyplot as plt #Only used for p/t.show() at the end. all other commands can be used as Point/Line methods
import time

from PkgMapping.MappingClasses import Point,Line

#HARDCODED TEST VALUES
wallLines = [
    Line(Point(30,20),Point(140,20)),
    Line(Point(140,20),Point(140,80)),
    Line(Point(140,80),Point(60,80)),
    Line(Point(60,80),Point(60,120)),
    Line(Point(60,120),Point(120,120)),
    Line(Point(120,120),Point(120,140)),
    Line(Point(120,140),Point(30,140)),
    Line(Point(30,140),Point(30,20)),

    Line(Point(40,50),Point(70,50)),
    Line(Point(70,50),Point(70,60)),
    Line(Point(70,60),Point(40,60)),
    Line(Point(40,60),Point(40,50))
]
navPointA = Point(47,47)
navPointB = Point(105,125)

#Creating grid based on extrema points
xMax = xMin = wallLines[0].p1.x
yMax = yMin = wallLines[0].p1.y
for wallLine in wallLines:
    xMax = max([wallLine.p1.x,wallLine.p2.x,xMax])
    xMin = min([wallLine.p1.x,wallLine.p2.x,xMin])
    yMax = max([wallLine.p1.y,wallLine.p2.y,yMax])
    yMin = min([wallLine.p1.y,wallLine.p2.y,yMin])
    wallLine.plot("g")

numXPoints = int((math.ceil(xMax) - math.floor(xMin))/10)
numYPoints = int((math.ceil(yMax) - math.floor(yMin))/10)
gridPoints = []
for xPoints in range(0,numXPoints):
    for yPoints in range(0,numYPoints):
        xPoint = math.floor(xMin)+10*xPoints
        yPoint = math.floor(yMin)+10*yPoints
        gridPoint = Point(xPoint, yPoint)
        gridPoint.plot("y")
        gridPoints.append(gridPoint)

#
lastPoints = [navPointA]
navPaths = []
segmentCount = 0
while len(navPaths) == 0:
    segmentCount += 1
    for lastPoint in lastPoints:
        proposedLine = Line(lastPoint, navPointB)
        if proposedLine.intersectsWall(wallLines) == False:
            navPaths.append(proposedLine)
            proposedLine.plot("green")
    lastPoints2 = lastPoints
    lastPoints = []
    if len(navPaths) == 0:
        for lastPoint in lastPoints2:
            proposedLines = lastPoint.connectToGrid(gridPoints, wallLines, lastPoints2)
            for proposedLine in proposedLines:
                lastPoints.append(proposedLine.p2)
                if segmentCount == 1:
                    proposedLine.plot("blue")
                elif segmentCount == 2:
                    proposedLine.plot("orange")
                elif segmentCount == 3:
                    proposedLine.plot("purple")
                elif segmentCount == 1:
                    proposedLine.plot("green")
print(segmentCount)

navPointA.plot("r")
navPointB.plot("r")
plt.show()