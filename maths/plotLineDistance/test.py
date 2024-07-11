from shapely import Point, LineString
from cvProjects.maths.plotLineDistance.plot_line_distance_2 import PointLineDistance
import random as rng

def testing() -> None:
    for i in range(0, 50):
        point1 = (rng.randint(0, 20), rng.randint(0, 20))
        point2 = (rng.randint(0, 20), rng.randint(0, 20))
        point = (rng.randint(0, 20), rng.randint(0, 20))


        my_calculator = PointLineDistance(point1, point2, point)
        my_distance = my_calculator.plot()


if __name__ == '__main__':
    testing()