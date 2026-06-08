from tkinter import *
top = Tk()

top.geometry = ("400x400")

v1 = IntVar()
def show1():
    msg = "Horizontal scale value = " + str(v1.get())
    lbl1.config(text=msg, font =("Courier", 12))
lbl1= Label(top, text = "price: ", bg="White", fg="Blue")
lbl1.pack()

scale = Scale(top, from_=100, to=1000, orient=HORIZONTAL, variable=v1)
scale.pack(anchor=CENTER)

b1 = Button(top, text="Display Horizontal", command=show1, bg="blue")
b1.pack(anchor=CENTER)

lbl1 = Label(top, text="price", bg="white", fg="blue")
lbl1.pack()

top.mainloop()