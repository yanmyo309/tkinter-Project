from tkinter import *
from tkinter import scrolledtext
import tkinter as tk

root =Tk()
text =scrolledtext.ScrolledText(root,width =30,height=30,wrap=tk.WORD).pack()

button = Button(root,text="Click")
button.pack()



root.mainloop()