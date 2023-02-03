from images import show_images
import images
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Captcha import get_captcha

root1 = tkinter.Tk()
length = 25
kol = 25
ph1,chars1 = show_images(length,kol)
for i in range(0,kol):
    pos = (i // 10)
    lbl = Label(root1, text=chars1[i], font=("Arial Bold", 20))
    lbl.grid(row=i-(10 * pos), column=2 * pos + 1)
    canvas = tkinter.Canvas(root1, width=length*25, height=90)
    canvas.grid(row=i-(10 * pos), column=2 * pos)
    img = canvas.create_image(0, 0, anchor='nw',image=ph1[i])
root1.mainloop()



