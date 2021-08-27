import matplotlib.pyplot as plt


def on_segment(p, q, r):
    if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):
        return True
    return False

def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0 : 
        return 0
    if val > 0:
        return 1
    else:
        return -1

def intersects(seg1, seg2):
    p1, q1 = seg1
    p2, q2 = seg2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, q1, p2): 
        return True
    if o2 == 0 and on_segment(p1, q1, q2): 
        return True
    if o3 == 0 and on_segment(p2, q2, p1): 
        return True
    if o4 == 0 and on_segment(p2, q2, q1): 
        return True

    return False

def intersectsWall(proposedLine, wallData):
    for wallLine in wallData:
        if intersects(proposedLine, wallLine):
            return True
    return False

#HARDCODED TEST VALUES
wallData = [
    ((3,2),(14,2)),
    ((14,2),(14,8)),
    ((14,8),(6,8)),
    ((6,8),(6,14)),
    ((6,14),(3,14)),
    ((3,14),(3,2))

    # ((5,5),(7,5)),
    # ((7,5),(7,6)),
    # ((7,6),(5,6)),
    # ((5,6),(5,5))
]
navPoints = ((11,4),(4,12))
gridPoints = [
    (4,7),
    (5,7),
    (6,7),
    (7,7),
    (4,6),
    (5,6),
    (6,6),
    (7,6),
    (4,5),
    (5,5),
    (6,5),
    (7,5),
]

def connectToGridPoints(pointA, gridPoints):
    potentialSegments = []
    for gridPoint in gridPoints:
        potentialSegment = (pointA,gridPoint)
        if intersectsWall(potentialSegment, wallData) == False:
            potentialSegments.append(potentialSegment)
    return potentialSegments
        

numLineSegments = 1
if intersectsWall(navPoints,wallData):
    pathFailed = True
else:
    pathFailed = False


while pathFailed:
    numLineSegments += 1
    potentialPaths = []
    for lineSegment in range(1,numLineSegments+1):
        if lineSegment == 1: #First segment
            pointA = navPoints[0]
            potentialSegments = connectToGridPoints(pointA,gridPoints)
            for pointA,pointB in potentialSegments:
                if intersectsWall((pointB,navPoints[1]),wallData) == False:
                    potentialPaths.append((pointA,pointB,navPoints[1]))
            if len(potentialPaths) > 0:
                pathFailed = False

for wallLine in wallData:
    plt.plot([wallLine[0][0],wallLine[1][0]],[wallLine[0][1],wallLine[1][1]])
for pathSegment in potentialPaths:
    plt.plot([pathSegment[0][0],pathSegment[1][0],pathSegment[2][0]],[pathSegment[0][1],pathSegment[1][1],pathSegment[2][1]])

plt.show()


# while pathFailed:
#     numLineSegments += 1
#     potentialPaths = []
#     for lineSegment in range(1,numLineSegments+1):
#         if lineSegment == 1: #First segment
#             pointA = navPoints[0]
#             potentialSegments = connectToGridPoints(pointA,gridPoints)
#             potentialSegmentsStored = potentialSegments
#         else:
#             for potentialSegment in potentialSegmentsStored:
#                 pointA = potentialSegment[1] #Successful gridPoint
#                 if lineSegment == numLineSegments: #Last segment
#                     pass
#                 else:
#                     gridPointsWithoutA = gridPoints
#                     gridPointsWithoutA.remove(pointA)
#                     potentialSegments = connectToGridPoints(pointA,gridPointsWithoutA)