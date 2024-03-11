from tkinter import *
class myclass:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.okbtn=Button(frame,text="ok",command=self.oks)
        self.okbtn.pack()
        self.qbtn=Button(frame,text="quit",command=frame.quit)
        self.qbtn.pack()
    def oks(self):
        print("hello team")
root=Tk()
obj= myclass(root)


root.mainloop()