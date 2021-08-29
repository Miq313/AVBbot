import math

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
        coordinates = str(((self.p1.x,self.p1.y),(self.p2.x,self.p2.y)))
        return coordinates

    #Note that the same line backwards will return False. Lines are treated as vectors (with direction)
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def __hash__(self):
        return hash(self.p1,self.p2)

    def length(self):
        return  math.sqrt(abs(self.delX)**2 + abs(self.delY)**2)
	
    def direction(self):
        directionOfLine = math.degrees(math.atan2(self.delY,self.delX))
        if directionOfLine < 0:
            directionOfLine = directionOfLine + 360.0
        return directionOfLine

    def slope(self):
        return self.delY/self.delX