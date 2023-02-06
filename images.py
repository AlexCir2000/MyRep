import tkinter
from tkinter import *
from PIL import Image, ImageTk
from Captcha import get_captcha

def creata_captcha_array(len, kol):
    #root = tkinter.Tk()
    photo = {}
    chars = {}
    for j in range(0,kol):
        pic,symbols = get_captcha(len)
        #pos = j//10
        #lbl = Label(root, text=symbols, font=("Arial Bold", 20))
        #lbl.grid(row=j-(10 * pos), column=2 * pos + 1)
        #canvas = tkinter.Canvas(root, width=len*25, height=90)
        #canvas.grid(row=j-(10 * pos), column=2 * pos)
        img = Image.open(pic)
        photo[j] = ImageTk.PhotoImage(img)
        #img = canvas.create_image(0, 0, anchor='nw',image=photo[j])
        chars[j] = symbols
    #root.mainloop()
    return photo, chars
#show_images(5,10)