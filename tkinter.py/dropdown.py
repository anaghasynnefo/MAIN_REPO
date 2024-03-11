from tkinter import *
root=Tk()
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="EDIT",menu=submenu)
submenu.add_cascade(label='UNDO')
submenu.add_cascade(label='REDO')
submenu.add_separator()

submenu.add_cascade(label='CUT')
submenu.add_cascade(label='COPY')
submenu.add_cascade(label='PASTE')
submenu.add_separator()

submenu.add_cascade(label='FIND')
submenu.add_cascade(label='REPLACE')
submenu.add_separator()

submenu.add_cascade(label='FIND IN FILES')
submenu.add_cascade(label='REPLACE IN FILES')
submenu.add_separator()


submenu.add_command(label='Save')
newmenu=Menu(mymenu)

mymenu.add_cascade(label="TERMINAL",menu=newmenu)
newmenu.add_cascade(label='NEW TERMINAL')
newmenu.add_cascade(label='SPLIT TERMINAL')
newmenu.add_separator()

menu1=Menu(mymenu)
menu1.add_cascade(label="SELECTION",menu=menu1)
menu1.add_cascade(label='EXPAND ')
menu1.add_cascade(label='SHRINK')
newmenu.add_separator()

menu1.add_cascade(label='COPY LINE UP')
menu1.add_cascade(label='COPY LINE DOWN')
menu1.add_cascade(label='MOVE LINE UP')
menu1.add_cascade(label='MOVE LINE DOWN')
menu1.add_cascade(label='DUPLICATE SELECTION')
newmenu.add_separator()

menu2=Menu(mymenu)
menu2.add_cascade(label="GO",menu=menu2)
menu2.add_cascade(label='BACK')
menu2.add_cascade(label='FORWARD')
newmenu.add_separator()

menu2.add_cascade(label='SWITCH EDITOR')
menu2.add_cascade(label='SWITCH GROUP')
newmenu.add_separator()

toolbar=Frame(root,bg='grey')
btn1=Button(toolbar,text='crop')
btn1.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(fill='x',side=TOP)
statusbar=Label(root,text='This is status bar',anchor=W,bg='black',fg='green')
statusbar.pack(fill='x',side=BOTTOM)

root.mainloop()


