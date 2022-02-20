from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("300x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

B.place(x = 50,y = 50)
top.mainloop()
