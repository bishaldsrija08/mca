from tkinter import *
def do():
    f = Toplevel()
    button = Button(f, text="Do everything")
    button.pack()

main = Tk()
mb = Menu(main, tearoff=0)
filem = Menu(mb, tearoff=0)
filem.add_command(label="New", command=do)
filem.add_command(label="Open", command=do)
filem.add_command(label="Save", command=do)
filem.add_command(label="Save as...", command=do)

filem.add_separator()
filem.add_command(label="Exit", command=main.quit)
mb.add_cascade(label="File", menu=filem)

editm = Menu(mb, tearoff=0)
editm.add_command(label="Cut", command=do)
editm.add_command(label="Copy", command=do)
editm.add_command(label="Paste", command=do)

editm.add_separator()
editm.add_command(label="Select all", command=do)
mb.add_cascade(label="Edit", menu=editm)
main.config(menu=mb)

helpm = Menu(mb, tearoff=0)
helpm.add_command(label="Help", command=do)
helpm.add_command(label="About", command=do)
mb.add_cascade(label="Help", menu=helpm)

main.config(menu=mb)
main.mainloop()