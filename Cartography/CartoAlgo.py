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

print(intersects((),())

# spatialData = [
#     ((8,4),(4,2)),
#     ((10,4),(8,2)),
#     ((11,4),(12,2)),
#     ((12,4),(3,9)),
#     ((14,6),(7,4)),
#     ((11,8),(5,4)),
#     ((7,8),(4,4)),
#     ((6,10),(4,5))
# ]
# wallPoints = []
# for line in spatialData:
#     wallPoints.append(line[1])
# for p,q in spatialData:
#     a,b = p
#     x,y = q
#     plt.plot([a,x],[b,y], color='#000000')

# wall = []
# for point1 in wallPoints:
#     print(point1)
#     for point2 in wallPoints:
#         if point1 != point2:
#             wallLine = (point1,point2)
#             isCorrect = True
#             for spaceLine in spatialData:
#                 if intersects(wallLine,spaceLine):
#                     isCorrect = False
#                     plt.plot([point1[0],point2[0]],[point1[1],point2[1]], color='r', linewidth=0.5)
#             if isCorrect:
#                 wall.append(wallLine)

# for line in set(wall):
#     print(line)

# plt.show()