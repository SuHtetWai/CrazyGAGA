# import tkinter as tk
# from tkinter import ttk
#
# window = tk.Tk()
# # window.iconbitmap("D:/National Cyber City Uni/ncc.ico")
# window.title("NCC-Cycle-Ticket")
# # window.geometry('500x500')
# window.configure(bg="#5c5e12")
# # e = Entry(window, width=35, borderwidth=5)
#
# number = 0
# one = "00"
# two = '0'
#
#
# def button_click():
#     global frame
#     global label
#
#     ll = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009"]
#     # label = ttk.Button(master=frame, text=good)
#
#     a = ttk.Button.cget(label, 'text')
#     print(a)
#
#     # for gcc in ll:
#     #     if gcc == a:
#     #         print("same")
#     #         break
#     # print(a)
#
#
#
#     # for ii in range(1, len(number1)):
#     #     r = number1[ii]
#     #     c = number1[ii+1]
#     #     break
#     #
#     # frame = tk.Frame(
#     #     master=frame,
#     #     relief=tk.FLAT,
#     #     borderwidth=5, bg="#0a0606"
#     # )
#     #
#     # frame.grid(row=r, column=c, padx=5, pady=5)
#
#
# for i in range(10):
#     window.columnconfigure(i, weight=1, minsize=25)
#     window.rowconfigure(i, weight=1, minsize=25)
#
#     for j in range(10):
#         # number += 1
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RIDGE,
#             borderwidth=1, bg="#51ff45"
#         )
#         good = ''
#         frame.grid(row=i, column=j, padx=3, pady=3)
#         if number < 10:
#             good = one + str(number)
#             label = tk.Button(master=frame, text=good, command=button_click)
#         elif 10 <= number < 100:
#             good = two + str(number)
#             b = good
#             label = tk.Button(master=frame, text=good, command=button_click)
#         else:
#             c = str(number)
#             label = tk.Button(master=frame, text=str(number), command=button_click)
#         label.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
#         number += 1
#
# window.mainloop()

import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

# window = tk.Tk()
# window.title("NCC-Cycle-Ticket")
# # window.geometry('500x500')
#
# image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
# image1 = image1.resize((300,300),Image.ANTIALIAS)
# newImage = ImageTk.PhotoImage(image1)
#
# btn1 = Button(window, text="Bed",compound=BOTTOM,image=newImage)
# btn1.pack(side=LEFT, padx=10, pady=10)
# for i in range(5):
#     window.columnconfigure(i, weight=1, minsize=25)
#     window.rowconfigure(i, weight=1, minsize=25)
#
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RIDGE,
#             borderwidth=1, bg="#51ff45"
#         )
#         frame.grid(row=i, column=j, padx=3, pady=3)
#         label = tk.Label(master=frame, text=f"row {i} \n column {j}")
#         label.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
#
# window.mainloop()

# import tkinter as tk
# from tkinter import *
# my_w = tk.Tk()
# my_w.geometry("410x200")  # Size of the window
#
# #my_w.columnconfigure(0,weight=1)
# #my_w.rowconfigure(0, weight=1)
# #my_w.rowconfigure(1, weight=1) # change weight to 4
# #my_w.rowconfigure(2, weight=1)
#
# frame_top=tk.Frame(my_w,bg='red')
# frame_middle=tk.Frame(my_w,bg='yellow')
# frame_bottom=tk.Frame(my_w,bg='blue')
# #placing in grid
# frame_top.grid(row=0,column=0,sticky='WENS')
# frame_middle.grid(row=1,column=0,sticky='WENS')
# frame_bottom.grid(row=2,column=0,sticky='WENS')
# #adding labels to frame
# l1=tk.Label(frame_top,text='frame_top')
# l1.grid(row=0,column=0,padx=10,pady=2)
#
# l2=tk.Label(frame_middle,text='frame_middle')
# l2.grid(row=0,column=0,padx=10,pady=2)
#
# l3=tk.Label(frame_bottom,text='frame_bottom')
# l3.grid(row=0,column=0,padx=10,pady=2)
# my_w.mainloop()  # Keep the window open


# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("Vinayak App")

# Constructing the first frame, frame1
frame1 = LabelFrame(app, text="Fruit", bg="green",fg="white", padx=15, pady=15)

# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0)

# Constructing the button b1 in frame1
b1 = Button(frame1, text="Apple")

# Displaying the button b1
b1.pack()

# Constructing the second frame, frame2
frame2 = LabelFrame(app, text="Vegetable", bg="yellow", padx=15, pady=15)

# Displaying the frame2 in row 0 and column 1
frame2.grid(row=0, column=1)

# Constructing the button in frame2
b2 = Button(frame2, text="Tomato")

# Displaying the button b2
b2.pack()

frame3 = LabelFrame(app, text="Orange", bg="red", padx=25, pady=25)
frame3.grid(row=0, column=2)
b3 = Button(frame2, text="Orange")
b3.pack()
frame3 = LabelFrame(app, text="Orange", bg="red", padx=25, pady=25)
frame3.grid(row=0, column=2)
b3 = Button(frame2, text="Orange")
b3.pack()
# Make the loop for displaying app
app.mainloop()
