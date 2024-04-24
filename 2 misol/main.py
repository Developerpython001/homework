from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

point = Point(3, 4)

print("x :", point.x)
print("y :", point.y)
