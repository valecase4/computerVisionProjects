import cv2 as cv
import numpy as np

cv.namedWindow("Color Picker")

def nothing(x) -> None:
    """
    Callback function: called when a trackbar is adjusted by the user
    It gets current value of red, green and blue trackbars and displays new color
    """

    r = cv.getTrackbarPos('R','Color Picker')
    g = cv.getTrackbarPos('G','Color Picker')
    b = cv.getTrackbarPos('B','Color Picker')
    
    blank[:, :] = (b, g, r)
    cv.imshow("Color Picker", blank)

blank = np.zeros((300, 500, 3), dtype='uint8')
blank[:, :] = (255, 255, 255)

cv.createTrackbar('R', "Color Picker", 0, 255, nothing)
cv.createTrackbar('G', "Color Picker", 0, 255, nothing)
cv.createTrackbar('B', "Color Picker", 0, 255, nothing)

cv.imshow("Color Picker", blank)

cv.waitKey(0)
 
