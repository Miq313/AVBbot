import math

class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
	
    def __repr__(self):
        coordinates = (self.x,self.y)
        return coordinates
	
    def __str__(self):
        pointStr = "(%f,%f)" % (self.x, self.y)
        return pointStr
	
class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.delX = self.p2.x - self.p1.x
        self.delY = self.p2.y - self.p1.y
	
    def __repr__(self):
        coordinates = ((self.p1.x,self.p1.y),(self.p2.x,self.p2.y))
        return coordinates

    def __str__(self):
        x1,y1 = self.p1.x,self.p1.y
        x2,y2 = self.p2.x,self.p2.y
        lineStr = "((%f,%f),(%f,%f))" % (x1,y1,x2,y2)
        return lineStr

    def length(self):
        return  math.sqrt(abs(self.delX)**2 + abs(self.delY)**2)
	
    def direction(self):
        directionOfLine = math.degrees(math.atan2(self.delY,self.delX))
        if directionOfLine < 0:
            directionOfLine = directionOfLine + 360.0
        return directionOfLine

    def slope(self):
        return self.delY/self.delX