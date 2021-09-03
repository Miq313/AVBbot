from PkgMapping.MappingClasses import Point,Line,showPlot

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

showPlot()