#     t k P h o n e . p y
#
from Tkinter import *
#from phones  import *
import pickle

def whichSelected () :
    print "At %s of %d" % (select.curselection(), len(phonelist))
    return int(select.curselection()[0])

def addEntry () :
    phonelist.append ([nameVar.get(), phoneVar.get()])
    setSelect ()
    saveEntry()

def updateEntry() :
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
    setSelect ()
    saveEntry()

def deleteEntry() :
    del phonelist[whichSelected()]
    setSelect ()
    saveEntry()

def loadEntry  () :
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def saveEntry  () :
    #name, phone = phonelist[whichSelected()]
    pickle.dump(phonelist,open( 'phones1.py', "wb" ))
    #nameVar.set(name)
    #phoneVar.set(phone)
    
def makeWindow () :
    global nameVar, phoneVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    #b5 = Button(frame2,text=" Save ",command=saveEntry)
    #b1.pack(side=LEFT); b2.pack(side=LEFT)
    #b3.pack(side=BOTTOM); b4.pack(side=LEFT)
    #b5.pack(side=BOTTOM)
    b1.grid(row=0, column=0, sticky=W)
    b2.grid(row=0, column=1, sticky=W)
    b3.grid(row=0, column=2, sticky=W)
    b4.grid(row=0, column=3, sticky=W)
    #b5.grid(row=1, column=1, sticky=W)
    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

def setSelect () :
    phonelist.sort()
    #print phonelist
    select.delete(0,END)
    for name,phone in phonelist :
        select.insert (END, name)

win = makeWindow()
phonelist = pickle.load(open( 'phones1.py', "rb" ))
setSelect ()
win.mainloop()
