from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from tkinter import scrolledtext, messagebox
from sql import *
import sql
import tkinter
from tkinter import *
from PIL import Image, ImageTk

def push_btn_show():
    if get_count() >=20:
        show_images(20)
    else:
        messagebox.showwarning('Ашипко!','Мало записей в базе. Добавьте записи соответствующей кнопкой')



def push_btn_clear():
    lbl_work.configure(text='Working')
    clear_table()
    lbl.configure(text='There are ' + str(get_count()) + ' records in a database')
    lbl_work.configure(text=' Done')

def push_btn_add():
    lbl_work.configure(text='Working')
    insert_query(100,5)
    lbl.configure(text='There are ' + str(get_count()) + ' records in a database')
    lbl_work.configure(text=' Done')

window = tkinter.Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1000x800')

lbl = Label(window, text='There are ' + str(get_count()) + ' records in a database', font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl_work = Label(window, text=' Done', font=("Arial Bold", 10))
lbl_work.grid(column=1, row=0)

btn_show = Button(window, text='''Show some records''', command=push_btn_show)
btn_show.grid(column=0, row=1)

btn_clear = Button(window, text='''Clear records''', command=push_btn_clear)
btn_clear.grid(column=0, row=2)

btn_add = Button(window, text='''Add 100 records''', command=push_btn_add)
btn_add.grid(column=0, row=3)

window.mainloop()