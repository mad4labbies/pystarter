from tkinter import *
from tkinter import ttk

root=Tk()

root.option_add('*tearOff', FALSE)

frame =ttk.Frame(root)
win = Toplevel(frame)
menubar = Menu(win)
#appmenu = Menu(menubar, name='apple')
#menubar.add_cascade(menu=appmenu)
#appmenu.add_command(label='About My Application')
#appmenu.add_separator()
win['menu'] = menubar
