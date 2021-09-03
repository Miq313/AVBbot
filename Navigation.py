import math
from datetime import datetime

from PkgMapping.MappingClasses import Point,Line,showPlot

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
    #wallLine.plot("g")

numXPoints = int((math.ceil(xMax) - math.floor(xMin))/2)
numYPoints = int((math.ceil(yMax) - math.floor(yMin))/4)
gridPoints = []
for xPoints in range(0,numXPoints+1):
    for yPoints in range(0,numYPoints+1):
        xPoint = math.floor(xMin)+2*xPoints
        yPoint = math.floor(yMin)+4*yPoints
        gridPoint = Point(xPoint, yPoint)
        #gridPoint.plot("y")
        gridPoints.append(gridPoint)

#
time1 = datetime.now()
lastPoints = [navPointA]
navPaths = []
segmentCount = 0
allSegments = []
while len(navPaths) == 0:
    segmentCount += 1
    segments = []
    for lastPoint in lastPoints:
        proposedLine = Line(lastPoint, navPointB)
        if proposedLine.intersectsWall(wallLines) == False:
            navPaths.append(proposedLine)
            segments.append(proposedLine)
            #proposedLine.plot("green")
    lastPoints2 = lastPoints
    lastPoints = []
    if len(navPaths) == 0:
        for lastPoint in lastPoints2:
            proposedLines = lastPoint.connectToGrid(gridPoints, wallLines, lastPoints2)
            for proposedLine in proposedLines:
                lastPoints.append(proposedLine.p2)
                segments.append(proposedLine)
                # if segmentCount == 1:
                #     proposedLine.plot("blue")
                # elif segmentCount == 2:
                #     proposedLine.plot("orange")
                # elif segmentCount == 3:
                #     proposedLine.plot("purple")
                # elif segmentCount == 4:
                #     proposedLine.plot("grey")
    allSegments.append(segments)

# for segment in allSegments:
#     print(set(segment))
#     print("\n")

delta = datetime.now() - time1
print(delta.seconds)
# navPointA.plot("r")
# navPointB.plot("r")
# showPlot()