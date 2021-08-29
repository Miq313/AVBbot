import math
import matplotlib.pyplot as plt

from PkgMapping.MappingClasses import Point,Line
from PkgMapping.MappingUtilities import intersects

#HARDCODED TEST VALUES
wallData = [
    Line(Point(30,20),Point(140,20)),
    Line(Point(140,20),Point(140,80)),
    Line(Point(140,80),Point(60,80)),
    Line(Point(60,80),Point(60,140)),
    Line(Point(60,140),Point(30,140)),
    Line(Point(30,140),Point(30,20)),

    Line(Point(40,50),Point(70,50)),
    Line(Point(70,50),Point(70,60)),
    Line(Point(70,60),Point(40,60)),
    Line(Point(40,60),Point(40,50))
]
navPointA = Point(9,4)
navPointB = Point(4,12)

#Creating grid based on extrema points
xMax = xMin = wallData[0].p1.x
yMax = yMin = wallData[0].p1.y
for wallLine in wallData:
    xMax = max([wallLine.p1.x,wallLine.p2.x,xMax])
    xMin = min([wallLine.p1.x,wallLine.p2.x,xMin])
    yMax = max([wallLine.p1.y,wallLine.p2.y,yMax])
    yMin = min([wallLine.p1.y,wallLine.p2.y,yMin])
    plt.plot([wallLine.p1.x,wallLine.p2.x],[wallLine.p1.y,wallLine.p2.y], color="g")

numXPoints = int((math.ceil(xMax) - math.floor(xMin))/10)
numYPoints = int((math.ceil(yMax) - math.floor(yMin))/10)
gridPoints = []
for xPoints in range(0,numXPoints):
    for yPoints in range(0,numYPoints):
        gridPoints.append(Point(math.floor(xMin)+10*xPoints, math.floor(yMin)+10*yPoints))

for gridPoint in gridPoints:
    plt.scatter(gridPoint.x, gridPoint.y, color="y")

plt.show()
