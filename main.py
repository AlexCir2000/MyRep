from images import show_images
import images
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Captcha import get_captcha

root = tkinter.Tk()
a = {}
b = {}
a, b = show_images(5)
"""for j in range(1,6,2):
    for i in range(0,10):
        lbl = Label(root, text=chars[i,j], font=("Arial Bold", 20))
        lbl.grid(row=i, column=j+1)
        canvas = tkinter.Canvas(root, width=len*25, height=90)
        canvas.grid(row=i, column=j)
        img = canvas.create_image(0, 0, anchor='nw',image=photo[i,j])

root.mainloop()



"""
