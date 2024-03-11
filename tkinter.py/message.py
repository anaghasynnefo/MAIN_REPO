from tkinter import *
from tkinter import messagebox
root=Tk()
def asd():
    messagebox.showinfo("Delete","are you sure to delete ?")
    # messagebox.showwarning("Delete","are you sure to delete ?")
    # messagebox.showerror("Delete","are you sure to delete ?")
    # messagebox.askokcancel("Delete","are you sure to delete ?")
    # messagebox.askquestion("Delete","are you sure to delete ?")
    # messagebox.askretrycancel("Delete","are you sure to delete ?")
    # messagebox.askyesno("Delete","are you sure to delete ?")

Button(root,text="ok",command=asd).pack()


root.mainloop()