from Tkinter import *
import tkMessageBox

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( )
E1 = Entry(top, bd =5)

E1.pack()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", E1.get())

B = Button(top, text ="Display", command = helloCallBack)
B.pack()
top.mainloop()
