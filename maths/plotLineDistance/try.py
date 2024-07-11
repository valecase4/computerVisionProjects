from shapely import Point, LineString
from cvProjects.maths.plotLineDistance.plot_line_distance_2 import PointLineDistance
import random

x1, y1 = random.randint(0, 20), random.randint(0,20)
x2, y2 = random.randint(0, 20), random.randint(0,20)
x,y = random.randint(0, 20), random.randint(0,20)

print(x1,y1)
print(x2,y2)
print(x,y)

point = Point(x,y)

line = LineString([[x1,x2], [y1,y2]])

print(round(line.distance(point), 2))

my_tool = PointLineDistance((x1,y1), (x2,y2), (x,y))
print(my_tool.calculate_distance())