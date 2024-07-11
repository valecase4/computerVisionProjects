import matplotlib.pyplot as plt
import numpy as np
import math
from typing import Tuple

class PointLineDistance:
    def __init__(self, point1: Tuple[float, float], point2: Tuple[float, float], point: Tuple[float, float]) -> None:
        self.p1 = point1 if point1[0] <= point2[0] else point2
        self.p2 = point2 if point2[0] >= point1[0] else point1
        self.p = point

        self.perp_ang_coeff = None
        self.perp_y_intercept = None
        self.int_point = None

        if self.p1[0] == self.p2[0]:
            self.ang_coeff = None
            self.y_intercept = None
            self.upper_point = self.p2 if self.p2[1] >= self.p1[1] else self.p1
            self.lower_point = self.p1 if self.p1[1] >= self.p2[1] else self.p2

        elif self.p1[1] == self.p2[1]:
            self.ang_coeff = 0
            self.y_intercept = self.p1[1]

        else:
            self.ang_coeff = (self.p2[1] - self.p1[1]) / (self.p2[0] - self.p1[0])
            self.y_intercept = self.p2[1] - self.ang_coeff * self.p2[0]
        

    def calculate_distance(self) -> float:
        if self.p1[0] == self.p2[0]:
            distance = abs(self.p[0] - self.p1[0])
        elif self.p1[1] == self.p2[1]:
            distance = abs(self.p[1] - self.p1[1])
        else:
            numerator = abs(self.ang_coeff * self.p[0] - self.p[1] + self.y_intercept)
            denominator = math.sqrt((self.ang_coeff)**2 + 1)

            distance = numerator / denominator

        return round(distance, 2)

    def plot(self) -> None:
        if self.ang_coeff and self.ang_coeff != 0:

            self.perp_ang_coeff = - (1 / self.ang_coeff)
            self.perp_y_intercept = self.p[1] - self.perp_ang_coeff * self.p[0]

            # FINDING INTERSECTION POINT

            A = np.array([[self.ang_coeff, -1], [self.perp_ang_coeff, -1]])
            B = np.array([-self.y_intercept, -self.perp_y_intercept])

            self.int_point = np.linalg.solve(A, B)

            if self.int_point[0] > self.p2[0]:
                x_values = list(np.arange(self.p1[0] - 3, self.int_point[0] + 3, 0.01))
                x_values_2 = list(np.arange(self.p1[0] - 3, self.p[0] + 3, 0.01))
            elif self.int_point[0] < self.p1[0]:
                x_values = list(np.arange(self.int_point[0] - 3, self.p2[0] + 3, 0.01))
                x_values_2 = list(np.arange(self.p[0] - 3, self.p2[0] + 3, 0.01))
            else:
                x_values = list(np.arange(self.p1[0] - 3, self.p2[0] + 3, 0.01))
                x_values_2 = x_values
            
            y_values = []

            for x in x_values:
                y = self.ang_coeff * x + self.y_intercept
                y_values.append(y)
                
            y_values_2 = []

            for x in x_values_2:
                y = self.perp_ang_coeff * x + self.perp_y_intercept
                y_values_2.append(y)
                
            plt.figure(figsize=(7,7))

            plt.plot(x_values, y_values, 'r--')
            plt.plot(x_values_2, y_values_2, 'b--')
            
        elif self.ang_coeff == 0:
            if self.p1[1] < self.p[1]:
                y_values = np.array(np.arange(self.p1[1] - 3, self.p[1] + 3, 0.01))
            else:
                y_values = np.array(np.arange(self.p[1] - 3, self.p1[1] + 3, 0.01))
            x_values = np.full(y_values.shape[0], self.p[0])

            self.perp_ang_coeff = 1
            self.int_point = (self.p[0], self.p1[1])

            plt.figure(figsize=(7,7))

            if self.p[0] > self.p2[0]:
                plt.plot([self.p1[0], self.p2[0] + self.p[0] + 3], [self.p1[1], self.p2[1]], 'r--')
            elif self.p[0] < self.p1[0]:
                plt.plot([self.p[0] - 3, self.p2[0]], [self.p1[1], self.p2[1]], 'r--')
            plt.plot(x_values, y_values, 'b--')
        
        else:
            if self.p[0] > self.p1[0]:
                x_values = np.arange(self.p1[0] - 3, self.p[0] + 3, 0.01)
            else: 
                x_values = np.arange(self.p[0] - 3, self.p1[0] + 3, 0.01)
            y_values = np.full(x_values.shape[0], self.p[1])

            self.int_point = (self.p1[0], self.p[1])

            plt.figure(figsize=(7,7))

            upper_point = self.p2 if self.p2[1] > self.p1[1] else self.p1

            if self.p[1] > self.upper_point[1]:
                plt.plot([self.p1[0], self.p1[0]], [self.upper_point[1], self.p[1] + 3], 'r--')
            elif self.p[1] < self.lower_point[1]:
                plt.plot([self.p1[0], self.p1[0]], [self.lower_point[1] - 3, self.p[1]], 'r--')
            plt.plot(x_values, y_values, 'b--')
            
        plt.plot([self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]], 'ro-', label='Source Line')
        plt.plot(self.p[0], self.p[1], 'bo', label='Point')
        plt.plot([self.int_point[0], self.p[0]], [self.int_point[1], self.p[1]], 'k', label=f'Distance: {self.calculate_distance()}', linewidth = 3)
        plt.plot(self.int_point[0], self.int_point[1], 'go', label='Intersection Point')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend(loc='upper right', fontsize='x-small')

        plt.gca().set_aspect('equal', adjustable='box')
            
        plt.show()

if __name__ == '__main__':
    points = [[None, None], [None, None], [None, None]]

    for point in points:
        for i in range(0, 2):
            user_input = input("Enter coordinate for this point: ")
            
            try:
                coord = float(user_input)
                point[i] = coord
            except:
                raise ValueError("Coordinates of each point must be of type integer or float")
    
    point_line_distance = PointLineDistance(tuple(points[0]), tuple(points[1]), tuple(points[2]))
    point_line_distance.plot()