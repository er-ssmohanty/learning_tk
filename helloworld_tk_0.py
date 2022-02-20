from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT,"Hello World!")
text.pack()
root.height(2)
root.width(10)
root.mainloop()
