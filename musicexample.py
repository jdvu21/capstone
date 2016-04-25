#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# the resemblence of a music player app

# sebsauvage.net/python/gui/#import


import Tkinter
import vlc
import os

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        menubar = Tkinter.Menu(self.parent)
        #self.parent.config(menu=menubar)

        fileMenu = Tkinter.Menu(menubar)
        fileMenu.add_command(label="Open", underline=0)
        fileMenu.add_command(label="Exit", underline=1)
        menubar.add_cascade(label="File", menu=fileMenu)  

        # pulling all .mp3's from ~/music
        for root, dirs, files in os.walk("~/music"):
            for file in files:
                if file.endswitch(".mp3"):
                    print(os.path.join(root,file))

    def initialize(self):
        self.grid()

        #self.entry = Tkinter.Entry(self)
        #self.entry.grid(column=0,row=0,sticky='EW')

        #button = Tkinter.Button(self,text=u"Click me !")
        #button.grid(column=1,row=0)

        Player = vlc.MediaPlayer("test1.mp3")
        
        def play():
            Player.play()

        def pause():
            Player.pause()

        def next():
            Player.stop()
            Player = vlc.MediaPlayer("test2.mp3")

        button = Tkinter.Button(self,text=u"Play",command=play)
        button.grid(column=1,row=1)

        button = Tkinter.Button(self,text=u"Pause",command=pause)
        button.grid(column=1,row=2)

        button = Tkinter.Button(self,text=u"Next",command=next)
        button.grid(column=1,row=3)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('music player')
    app.mainloop()
