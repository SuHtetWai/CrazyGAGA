from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("This is GAGA's Shop")
lab = Label(root, text='Welcome to Our shop', font=('Verdana', 15))
lab.pack(side=TOP, pady=10)
root.maxsize(1500,1500)
root.minsize(500,500)
photo = PhotoImage(file=r"C:\Users\acer\Downloads\BTS.png")
# photo1 = PhotoImage(file=r"C:\Users\acer\Pictures\furniture.jpg")
photoimage = photo.subsample(3,5)

def clicked():
    lab.configure(text="This is All items for you")

but =Button(root, text='Click here !', image=photoimage,compound=LEFT,command=clicked).pack(side=TOP)

buttom = Button(root,text="Exit",command=root.quit,compound=LEFT)
buttom.pack(side=BOTTOM)
root.mainloop()

