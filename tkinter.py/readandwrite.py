from tkinter import *

def result():
    num1=float(e1.get())
    num2=float(e2.get())
    res=set(num1+num2)

app=Tk()
app.title("calculator")
l1=Label(app,text="enter first number")
l1.pack()
e1=Entry(app)
e1.pack()
l2=Label(app,text="enter first number")
l2.pack()
e2=Entry(app)
e2.pack()
btn=Button(app,text="sum",command=result)
btn.pack()
res=StringVar()
res.set("result")
l3=Label(app,textvariable=res)
l3.pack()
app.mainloop()



""""""