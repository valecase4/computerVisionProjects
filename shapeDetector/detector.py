from tkinter import *
import customtkinter as ctk
from PIL import Image

def callback(x):
    print(slider.get())

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("550x550")
root.resizable(False, False)

my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\Vale\OneDrive\Desktop\valerio\computerVisionPython\photos\HappyFish.jpg"), 
                        dark_image=Image.open(r"C:\Users\Vale\OneDrive\Desktop\valerio\computerVisionPython\photos\HappyFish.jpg"),
                        size=(300,300)
                        )

image_label = ctk.CTkLabel(root, image=my_image, text="")

slider = ctk.CTkSlider(root, from_=0, to=100, orientation='vertical', command=callback)
slider.pack()

image_label.pack(pady=20)

root.mainloop()