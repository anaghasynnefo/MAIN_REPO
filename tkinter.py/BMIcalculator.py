from tkinter import *

root= Tk() 
root.geometry("312x324")  
root.resizable(0,0)  
root.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input.set(expression)
   
    
def bt_clear(): 
    global expression 
    expression = "" 
    input.set("")

def bt_equal():
    global expression
    result = str(eval(expression)) 
    input.set(result)
    expression = ""


expression = ""
btns = Frame(width=312, height=272.5, bg="black")
 
btns.pack()


input= StringVar()

input = Frame(width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input.pack(side=TOP)

input= Entry(input, font=('arial', 18, 'bold'), textvariable=input, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input.grid(row=0, column=0)
input.pack(ipady=10)

btns = Frame(width=312, height=272.5, bg="black")
 
btns.pack()





