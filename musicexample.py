#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# a simple, do nothing gui app

# sebsauvage.net/python/gui/#import


import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        button = Tkinter.Button(self,text=u"Click me !")
        button.grid(column=1,row=0)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('music player')
    app.mainloop()
