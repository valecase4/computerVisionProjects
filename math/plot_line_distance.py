import matplotlib.pyplot as plt
import numpy as np
import math
from typing import Tuple

class PointLineDistance:
    def __init__(self, point1: Tuple[float, float], point2: Tuple[float, float], point: Tuple[float, float]) -> None:
        self.p1 = point1
        self.p2 = point2
        self.p = point

    def calculate_distance(self) -> float:
        """
        Computes the perpendicular distance from the point to the line
        """

        numerator = abs((self.p2[1] - self.p1[1]) * self.p[0] - (self.p2[0] - self.p1[0]) * self.p[1] + self.p2[0] * self.p[1] - self.p2[1] * self.p1[0])
        denominator = math.sqrt((self.p2[1] - self.p1[1])**2 + (self.p2[0] - self.p1[0])**2)

        distance = float(numerator / denominator)

        return distance
    
    def find_intersection(self) -> Tuple[float, float]:
        """
        Determines the intersection point between the perpendicular from the point to the line and the source line
        """

        ang_coeff = (self.p2[1] - self.p1[1]) / (self.p2[0] - self.p1[0])
        y_intercept = self.p1[1] - ang_coeff * self.p1[0]

        ang_coeff_2 = - (1 / ang_coeff)
        y_intercept_2 = self.p[1] - ang_coeff_2 * self.p[0]

        A = np.array([[ang_coeff, -1], [ang_coeff_2, -1]])
        B = np.array([-y_intercept, -y_intercept_2])

        intersection_point = tuple(np.linalg.solve(A, B))
        return intersection_point
    
    def plot(self):
        """Plotting source line, source point and the distance segment between them"""

        plt.figure()
        plt.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]], 'bo-', label='Line Segment')
        plt.plot(self.p[0], self.p[1], 'ro')

        intersection_point = self.find_intersection()
        distance = self.calculate_distance()

        plt.plot(intersection_point[0], intersection_point[1], 'go', label='Intersection Point')
        plt.plot([self.p[0], intersection_point[0]], [self.p1[1], intersection_point[1]], 'r--', label=f'Distance: {distance:.2f}')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xticks(range(0, max(self.p1[0], self.p2[0]) + 3))
        plt.yticks(range(0, max(self.p1[1], self.p2[1]) + 3))
        plt.grid(True)
        plt.legend()
        plt.show()