from tkinter import *
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
from tkinter.ttk import *
root = Tk()
root.title("Welcome to GAGA's shop")
root.configure(background="grey")
root.maxsize(1500,1500)
root.minsize(200,200)
root.geometry("360x360+50+50")
text = Label(root,text="This is all Item ",font=('Verdana',16)).pack(side=TOP,pady=10)

photo = PhotoImage(file=r"C:\Users\acer\Pictures\furniture.jpg")
photoimage=photo.subsample(3,3)
Button(root,text='click here',image=photoimage,compound=LEFT).pack(side=TOP)

# quit_buttom = Button(root, text="Exit",command=root.quit)
# quit_buttom.pack()
root.mainloop()
