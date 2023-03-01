import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
window = Tk()
frame = tkinter.Frame()
frame.pack()
root.title("My shop")
# root.geometry("360x400")
root.maxsize(1500, 1500)
root.minsize(300, 300)

# e = Entry(root,width=50)
# e.pack()
# def clicked():
#     label = Label(text="Hello....."+e.get())
#     label.pack()
# but = Button(root,text="click",command=clicked)
# but.pack()

my_image1 = Image.open("C:/Users/acer/Downloads/BTS.png")
my_image2 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
my_image3 = Image.open("C:/Users/acer/Downloads/BTS.png")
my_image4 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
my_image5 = Image.open("C:/Users/acer/Downloads/BTS.png")
my_image1 = my_image1.resize((800, 500), Image.ANTIALIAS)
my_image2 = my_image2.resize((800, 500), Image.ANTIALIAS)
my_image3 = my_image3.resize((800, 500), Image.ANTIALIAS)
my_image4 = my_image4.resize((800, 500), Image.ANTIALIAS)
my_image5 = my_image5.resize((800, 500), Image.ANTIALIAS)

newImage1 = ImageTk.PhotoImage(my_image1)
newImage2 = ImageTk.PhotoImage(my_image2)
newImage3 = ImageTk.PhotoImage(my_image3)
newImage4 = ImageTk.PhotoImage(my_image4)
newImage5 = ImageTk.PhotoImage(my_image5)


image_list = [newImage1, newImage2, newImage3, newImage4, newImage5]
image_lb1 = tkinter.Label(image=newImage1)
image_lb2 = tkinter.Label(image=newImage2)
image_lb3 = tkinter.Label(image=newImage3)
image_lb4 = tkinter.Label(image=newImage4)
image_lb5 = tkinter.Label(image=newImage5)
image_lb1.grid(row=0,column=1)
image_lb2.grid(row=0,column=1)
image_lb3.grid(row=0,column=1)
image_lb4.grid(row=0,column=1)
image_lb5.grid(row=0,column=1)

def back():
    global image_lab
    global back
    global forward


def forward(image_number):
    global image_lab
    global back
    global forward
    image_lab.grid_forget()
    image_lab = Label(image=image_list[image_number - 1])
    my_but1 = Button(root, text="Back", command=back)
    my_but3 = Button(root, text="Next", command=lambda: forward(2))
    image_lab.grid(row=0, column=0, columnspan=3)
    my_but1 = Button(root, text="Back", command=back)
    my_but3 = Button(root, text="Next", command=lambda: forward(2))



my_but1 = Button(root, text="Back", command=back)
my_but2 = Button(root, text="Exit", command=root.quit)
my_but3 = Button(root, text="Next", command=lambda: forward(2))

my_but1.grid(row=1, column=0)
my_but2.grid(row=1, column=1)
my_but3.grid(row=1, column=2)
root.mainloop()
