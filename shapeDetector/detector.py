from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np
import random as rng

def callback(x):

    global src

    val = slider.get()

    current_thresh.set(int(round(val, 0)))

    threshold = val

    canny = cv.Canny(src, threshold, threshold * 2)

    contours, _ = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype='uint8')

    for i in range(len(contours)):
        color = (255,0,0)
        cv.drawContours(drawing, contours_poly, i, color)
        x, y, w, h = boundRect[i][0], boundRect[i][1], boundRect[i][2], boundRect[i][3]

        cv.rectangle(drawing, (x, y), (x+w, y+h), color, 2)




    updated_canny = Image.fromarray(drawing)

    updated_canny = ctk.CTkImage(light_image=updated_canny, 
                                 dark_image=updated_canny,
                                 size=(400,400)
                                )

    image_label.configure(image=updated_canny)


   

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("550x550")
root.resizable(False, False)

src = cv.imread(r"C:\Users\Vale\OneDrive\Desktop\valerio\computerVisionPython\photos\coins.jpg")

src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src = cv.blur(src, (3,3))

canny = cv.Canny(src, 125, 250)

canny_img = Image.fromarray(canny)


slider = ctk.CTkSlider(root, from_=125, to=255, command=callback)
slider.set(125)
slider.pack(pady=30)

current_thresh = StringVar(root, value=slider.get())
current_thresh_lbl = ctk.CTkLabel(root, text="Current Threshold", textvariable=current_thresh)
current_thresh_lbl.pack()

my_image = ctk.CTkImage(light_image=canny_img, 
                        dark_image=canny_img,
                        size=(400, 400)
                        )

image_label = ctk.CTkLabel(root, image=my_image, text="")

image_label.pack(pady=20)

root.mainloop()