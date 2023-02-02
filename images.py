import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Captcha import get_captcha

root = tkinter.Tk()
# frame = tkinter.Frame(root)
# frame.pack()
length = 10
photo = {}
for j in range(1,6,2):
    for i in range(1,10):
        a,b = get_captcha(length)
        lbl = Label(root, text=b, font=("Arial Bold", 20))
        lbl.grid(row=i, column=j)
        canvas = tkinter.Canvas(root, width=length*25, height=90)
        canvas.grid(row=i, column=j+1)
        img = Image.open('demo.png')
        photo[i,j] = ImageTk.PhotoImage(img)
        img = canvas.create_image(0, 0, anchor='nw',image=photo[i,j])



root.mainloop()