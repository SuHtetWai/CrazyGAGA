from tkinter import *
import tkinter


top = tkinter.Tk()
top.title("Welcom to GAGA's Shop")
top.geometry('360x220')
lab = Label(top, text='What kind of Furniture do you want to buy?')
lab.grid()


def clicked():
    lab.configure(text="I just want to buy this type of furniture")

but = Button(top,text= "Click here" , fg= "blue" , command= clicked)

but.grid(row = 1,column= 1)
top.mainloop()
menu = Menu(top)
item = Menu(menu)
