import matplotlib.pyplot as plt
from MappingClasses import Point,Line

def onSegment(seg, point):
    if point.x <= max(seg.p1.x, seg.p2.x) and point.x >= min(seg.p1.x, seg.p2.x) and point.y <= max(seg.p1.y, seg.p2.y) and point.y >= min(seg.p1.y, seg.p2.y):
        return True
    return False

def orientation(seg, point):
    val = ((seg.p2.y - seg.p1.y) * (point.x - seg.p2.x)) - ((seg.p2.x - seg.p1.x) * (point.y - seg.p2.y))
    if val == 0 : 
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def intersects(seg1, seg2):
    o1 = orientation(seg1, seg2.p1)
    o2 = orientation(seg1, seg2.p2)
    o3 = orientation(seg2, seg1.p1)
    o4 = orientation(seg2, seg1.p2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(seg1, seg2.p1): 
        return True
    if o2 == 0 and onSegment(seg1, seg2.p2): 
        return True
    if o3 == 0 and onSegment(seg2, seg1.p1): 
        return True
    if o4 == 0 and onSegment(seg2, seg1.p2): 
        return True

    return False

#Raw data input (pulled from Arduino)
rawData = [
    ((8,4),(4,2)),
    ((10,4),(8,2)),
    ((11,4),(12,2)),
    ((12,4),(3,9)),
    ((7,4),(14,6)),
    ((5,4),(11,8)),
    ((4,4),(7,8)),
    ((4,5),(6,10))
]
#Parse raw data, convert to Point & Line objects, store data
spatialLines = []
wallPoints =[]
for line in rawData:
    spatialLines.append(Line(Point(line[0][0],line[0][1]),Point(line[1][0],line[1][1])))
    wallPoints.append(Point(line[1][0],line[1][1]))

#Plot spatialLines for visualization purposes
for spatialLine in spatialLines:
    plt.plot([spatialLine.p1.x, spatialLine.p2.x],[spatialLine.p1.y, spatialLine.p2.y], color='#000000')

#Creating wall parameters by connecting all wallpoints with each other and checking which don't intersect with spatialLines
wallLines = []
for wallPoint in wallPoints:
    for wallPointConnecting in wallPoints:
        if wallPoint != wallPointConnecting:
            proposedWallLine = Line(wallPoint,wallPointConnecting)
            isCorrect = True
            for spatialLine in spatialLines:
                if intersects(proposedWallLine,spatialLine) and len(set([proposedWallLine.p1, proposedWallLine.p2, spatialLine.p1, spatialLine.p2])) == 4: #If intersects, but not including when intersects by the two lines sharing an endpoint
                    isCorrect = False
                    plt.plot([proposedWallLine.p1.x,proposedWallLine.p2.x],[proposedWallLine.p1.y,proposedWallLine.p2.y], color='r', linewidth=0.5)
            if isCorrect:
                wallLines.append(proposedWallLine)
                plt.plot([proposedWallLine.p1.x,proposedWallLine.p2.x],[proposedWallLine.p1.y,proposedWallLine.p2.y], color='g')

plt.show()