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
    Line(Point(0,10),Point(0,0))    
]

a = Point(5,5)
a.plot()

b = [Point(1,1),Point(2,2)]
connect = a.connectToGrid(gridPoints, wallLines, b)
for line in connect:
    line.plot()

plt.show()