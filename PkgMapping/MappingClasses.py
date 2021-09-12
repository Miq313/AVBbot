import math
import matplotlib.pyplot as plt
class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
	
    def __repr__(self):
        coordinates = str((self.x,self.y))
        return coordinates
	
    def __str__(self):
        coordinates = str((self.x,self.y))
        return coordinates

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))

    def plot(self, color="black"):
        plt.scatter(self.x, self.y, color=color)

    def connectToGrid(self, gridPoints, wallLines, omittedPoints = []):
        proposedSegments = []
        for omittedPoint in omittedPoints:
            if omittedPoint in gridPoints:
                gridPoints.remove(omittedPoint)
        for gridPoint in gridPoints:
            if Line(self,gridPoint).intersectsWall(wallLines) == False:
                proposedSegments.append(Line(self,gridPoint))
        return proposedSegments

    def distanceToLine(self, line):
        a = line.slope()
        if a != None:
            c = line.p1.y - a*line.p1.x
            b = -1
            return abs((a*self.x + b*self.y + c)/math.sqrt(a**2+b**2))
        return abs(line.p1.x - self.x)

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.delX = self.p2.x - self.p1.x
        self.delY = self.p2.y - self.p1.y
	
    def __repr__(self):
        coordinates = str(((self.p1.x,self.p1.y),(self.p2.x,self.p2.y)))
        return coordinates

    def __str__(self):
        coordinates = f"({self.p1.x}, {self.p1.y}) -> ({self.p2.x}, {self.p2.y})"
        return coordinates

    #Note that the same line backwards will return False. Lines are treated as vectors (with direction)
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def __hash__(self):
        return hash((self.p1,self.p2))

    def plot(self, color="black", linewidth=1):
        plt.plot([self.p1.x,self.p2.x],[self.p1.y,self.p2.y], color=color, linewidth=linewidth)

    def length(self):
        return  math.sqrt(abs(self.delX)**2 + abs(self.delY)**2)
	
    def direction(self):
        directionOfLine = math.degrees(math.atan2(self.delY,self.delX))
        if directionOfLine < 0:
            directionOfLine = directionOfLine + 360.0
        return directionOfLine

    def slope(self):
        if self.delX == 0:
            return None
        return self.delY/self.delX

    def onSegment(self, point):
        if point.x <= max(self.p1.x, self.p2.x) and point.x >= min(self.p1.x, self.p2.x) and point.y <= max(self.p1.y, self.p2.y) and point.y >= min(self.p1.y, self.p2.y):
            return True
        return False

    def orientation(self, point):
        val = ((self.p2.y - self.p1.y) * (point.x - self.p2.x)) - ((self.p2.x - self.p1.x) * (point.y - self.p2.y))
        if val == 0 : 
            return 0
        elif val > 0:
            return 1
        else:
            return -1

    def intersects(self, other):
        o1 = self.orientation(other.p1)
        o2 = self.orientation(other.p2)
        o3 = other.orientation(self.p1)
        o4 = other.orientation(self.p2)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and self.onSegment(other.p1): 
            return True
        if o2 == 0 and self.onSegment(other.p2): 
            return True
        if o3 == 0 and other.onSegment(self.p1): 
            return True
        if o4 == 0 and other.onSegment(self.p2): 
            return True

        return False

    def intersectsWall(self, wallLines):
        for wallLine in wallLines:
            if self.intersects(wallLine):
                return True
        return False

    def connectsTo(self, other):
        if self.p1 == other.p1 or self.p1 == other.p2 or self.p2 == other.p1 or self.p2 == other.p2:
            return True
        return False

def showPlot():
    plt.show()