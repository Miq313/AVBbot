from PkgMapping.MappingClasses import Point,Line
from PkgMapping.MappingUtilities import intersects

#HARDCODED TEST VALUES
wallData = [
    Line(Point(3,2),Point(14,2)),
    Line(Point(14,2),Point(14,8)),
    Line(Point(14,8),Point(6,8)),
    Line(Point(6,8),Point(6,14)),
    Line(Point(6,14),Point(3,14)),
    Line(Point(3,14),Point(3,2)),

    Line(Point(4,5),Point(7,5)),
    Line(Point(7,5),Point(7,6)),
    Line(Point(7,6),Point(4,6)),
    Line(Point(4,6),Point(4,5))
]
navPointA = Point(9,4)
navPointB = Point(4,12)

#
