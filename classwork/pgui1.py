import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
C = Tkinter.Button(top, text ="Hello2", command = helloCallBack)

B.pack()
C.pack()
top.mainloop()
