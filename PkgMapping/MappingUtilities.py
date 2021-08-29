from PkgMapping.MappingClasses import Point,Line

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
