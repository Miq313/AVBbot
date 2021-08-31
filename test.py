from PkgMapping.MappingClasses import Point,Line
import matplotlib.pyplot as plt
import math

xMin = yMin = 0
xMax = yMax = 10
gridPoints = []
for xPoints in range(0,10):
    for yPoints in range(0,10):
        xPoint = math.floor(xMin)+1*xPoints
        yPoint = math.floor(yMin)+1*yPoints
        gridPoint = Point(xPoint, yPoint)
        gridPoint.plot("y")
        gridPoints.append(gridPoint)

wallLines = [
    Line(Point(0,0),Point(10,0)),
    Line(Point(10,0),Point(10,10)),
    Line(Point(10,10),Point(0,10)),
    Line(Point(0,10),Point(0,0)),
    Line(Point(0,10),Point(0,0))
]


print(set(wallLines))

plt.show()