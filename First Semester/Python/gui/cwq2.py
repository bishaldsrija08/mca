from tkinter import *
import tkinter

main = Tk()

mb = Menubutton(main, text='file', relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb['menu']=mb.menu

new=IntVar()
save = IntVar()

saveas = IntVar()

mb.menu.add_checkbutton(label="New", variable=new)
mb.menu.add_checkbutton(label="Save", variable=save)
mb.menu.add_checkbutton(label="Save As", variable=saveas)

mb.pack()
main.mainloop()