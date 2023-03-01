# from tkinter import *
# root = Tk()
# root.title("This is GAGA Shop")
# root.minsize(height=500,width=500)
# root.maxsize(height=1000,width=1500)
# root.configure(background='GhostWhite')
# lb = Label(text="Welcome to GaGa's Shop",font=('Arial Bold',30,'italic'),fg='purple')
# lb.configure(background='DarkSlateGray3',width=57,height=2)
# lb.pack()
# bt = Button(root, text="Exit",command=root.quit,compound=LEFT,font=('Arial bold',20))
# bt.configure(background='DarkSlateGray3',height=1,width=10,fg='purple')
# bt.pack(side=BOTTOM)
# root.mainloop()

#
# from tkinter import *
# from PIL import ImageTk,Image
#
# master=Tk()
# master.geometry("400x300")
#
# image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
# image1 = image1.resize((100, 100), Image.ANTIALIAS)
# newImage1 = ImageTk.PhotoImage(image1)
# image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png")
# image2 = image2.resize((100, 100), Image.ANTIALIAS)
# newImage2 = ImageTk.PhotoImage(image2)
#
# frame1=Frame(master, width=200, height=150, background="Blue")
# frame1.grid(row=0, column=0)
#
# frame2=Frame(master, width=200, height=150, background="Red")
# frame2.grid(row=1, column=0)
#
# frame3=Frame(master, width=200, height=150, background="Green")
# frame3.grid(row=0, column=1)
#
# frame4=Frame(master, width=200, height=150, background="Yellow")
# frame4.grid(row=1, column=1)
#
# master.mainloop()
#
# import tkinter
# from tkinter import *
#
# root = tkinter.Tk()
# root.configure(background='white')
# root.title('Pop Up')
# root.geometry('300x200')
#
# photo = PhotoImage(file='C:/Users/acer/Downloads/Designer Chairs - High End Seating.png')
#
# w = Label(root, image=photo)
# text = Label(root, text="Hello world!")
#
# w.grid(row=3, column=3)
# text.grid(row=3, column=3)
#
# root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
# canvas1.pack()
#
# label1 = tk.Label(root, text='Calculate the Square Root')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 25, window=label1)
#
# label2 = tk.Label(root, text='Type your Number:')
# label2.config(font=('helvetica', 10))
# canvas1.create_window(200, 100, window=label2)
#
# entry1 = tk.Entry(root)
# canvas1.create_window(200, 140, window=entry1)
#
#
# def get_square_root():
#     x1 = entry1.get()
#
#     label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
#     canvas1.create_window(200, 210, window=label3)
#
#     label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)
#
#
# button1 = tk.Button(text='Get the Square Root', command=get_square_root, bg='brown', fg='white',
#                     font=('helvetica', 9, 'bold'))
# canvas1.create_window(200, 180, window=button1)
#
# root.mainloop()

import tkinter as tk
from tkinter import *
window = Tk()
def increase():

    value = int(lbl_value["text"])

    lbl_value["text"] = f"{value + 1}"

def decrease():
        value = int(lbl_value["text"])

        lbl_value["text"] = f"{value - 1}"
btn_decrease = tk.Button(master=window, text="-", command=decrease)

btn_decrease.grid(row=0, column=0, sticky="nsew")


lbl_value = tk.Label(master=window, text="0")

lbl_value.grid(row=0, column=1)


btn_increase = tk.Button(master=window, text="+", command=increase)

btn_increase.grid(row=0, column=2, sticky="nsew")


window.mainloop()