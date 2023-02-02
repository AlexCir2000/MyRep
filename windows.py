from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from tkinter import scrolledtext, messagebox

def clicked():
    if chk.state():
        res = combo.get()
        # res = 'hellow {}'.format(txt.get())
        lbl.configure(text='Hello, ' + res)
    else:
        pass
def RadoiClick():
    combo.current(selected.get()-1)
    clicked()

def clicked2():
    scroll.delete(1.0, END)
    ans = messagebox.askokcancel('Select','Select one')
    scroll.insert(INSERT,ans)
    # messagebox.showinfo('Haha', 'Info')
    # messagebox.showwarning('Ohoho','Warning')
    # messagebox.showerror('NOOO', 'Error')

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1000x800')
lbl = Label(window, text='Hello', font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10, state='disabled')
txt.grid(column=1, row=0)
txt.focus()
btn = Button(window, text='''Don't push''', bg='White', fg='Red', command=clicked)
btn.grid(column=2, row=0)
combo = Combobox(window)
combo['values'] = ['Alex', 'Peter', 'Mickhael', 'Tony']
combo.current(0)
combo.grid(column=4, row=0)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Write?', var=chk_state)
chk.grid(column=0, row=1)
selected = IntVar()
Rad1 = Radiobutton(window, text = 'Alex', value=1, variable=selected, command=RadoiClick)
Rad2 = Radiobutton(window, text = 'Peter', value=2, variable=selected, command=RadoiClick)
Rad3 = Radiobutton(window, text = 'Mickhael', value=3, variable=selected, command=RadoiClick)
Rad4 = Radiobutton(window, text = 'Tony', value=4, variable=selected, command=RadoiClick)
Rad1.grid(column=0, row=2)
Rad2.grid(column=0, row=3)
Rad3.grid(column=0, row=4)
Rad4.grid(column=0, row=5)

scroll = scrolledtext.ScrolledText(window, width=40, height=10)
scroll.insert(INSERT, 'Текстовое поле со всякой ерундой')
scroll.grid(column=1, row=2)
btn2 = Button(window, text='Clear text', bg='White', command=clicked2)
btn2.grid(column=1, row=3)
window.mainloop()
