import cv2 as cv
import numpy as np
from typing import Tuple

given_rectangle = ((135, 160), (280, 300))

class IntegralImage:
    def __init__(self, source_img: np.ndarray, rectangle: Tuple[Tuple[int, int]]):
        self.source_img = source_img

        if len(self.source_img.shape) == 3:
            self.source_img_gray = cv.cvtColor(source_img, cv.COLOR_BGR2GRAY)

        # COORDINATES OF GIVEN RECTANGLE
        self.upper_left = rectangle[0]
        self.upper_right = (rectangle[1][0], rectangle[0][1])
        self.bottom_left = (rectangle[0][0], rectangle[1][1])
        self.bottom_right = rectangle[1]

        # DICTIONARY WITH INTEGRAL IMAGE FOR EACH POINT (STARTING FROM 0)
        self.integral_images = {
            self.upper_left: 0,
            self.upper_right: 0,
            self.bottom_left: 0,
            self.bottom_right: 0
        }

    def draw(self) -> None:
        cv.rectangle(self.source_img, self.upper_left, self.bottom_right, (0,0,255), 2)
        cv.rectangle(self.source_img, (0,0), (self.upper_right[0], self.upper_right[1] - 2), (255,0,0), 2)
        cv.rectangle(self.source_img, (0,0), (self.bottom_left[0] - 2, self.bottom_left[1]), (0,255,0), 2)

        for point in [self.upper_left, self.upper_right, self.bottom_left, self.bottom_right]:
            cv.circle(self.source_img, point, 8, (0,0,255), -1)

    def compute_sums(self) -> None:
        for point, _ in self.integral_images.items():
            for j in range(point[1]):
                for k in range(point[0]):
                    self.integral_images[point] += self.source_img_gray[j][k]

            cv.putText(self.source_img, f"{self.integral_images[point]}", (point[0]-80, point[1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,0), 2)

    def main(self) -> float:
        A = self.integral_images[self.upper_left]
        B = self.integral_images[self.upper_right]
        C = self.integral_images[self.bottom_left]
        D = self.integral_images[self.bottom_right]

        integral_image = float(D + A - (B + C))

        return integral_image
    
    def show(self) -> None:
        self.draw()
        self.compute_sums()

        cv.imshow("Integral Image", self.source_img)
        cv.waitKey()


file_path = "lena.jpg"
input_image = cv.imread(file_path)

if __name__ == '__main__':
    integral_image = IntegralImage(input_image, given_rectangle)
    integral_image.show()
    output = integral_image.main()
    
    print(f"Sum of pixels within the given rectangle: {output}")

            