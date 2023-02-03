import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Captcha import get_captcha

def show_images(len,kol):
    # root = tkinter.Tk()
    photo = {}
    chars = {}
    for j in range(0,kol):
         pic,symbols = get_captcha(len)
    #    lbl = Label(root, text=symbols, font=("Arial Bold", 20))
    #    lbl.grid(row=i, column=j+1)
    #    canvas = tkinter.Canvas(root, width=len*25, height=90)
    #    canvas.grid(row=i, column=j)
         img = Image.open(pic)
         photo[j] = ImageTk.PhotoImage(img)
    #    img = canvas.create_image(0, 0, anchor='nw',image=photo[i,j])
         chars[j] = symbols
    # root.mainloop()
    return photo, chars
