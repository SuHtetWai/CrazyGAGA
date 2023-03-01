# from tkinter import *
#
# import tkinter
#
# root = Tk()
# root.title("GAGA shop")
# root.minsize(300, 300)
# root.maxsize(1500, 1500)
# root.configure(background="dark grey")
# lb = Label(text="Welcome to GaGa's shop", font=('Arial Bold', 18, 'italic'), fg='black')
# lb.configure(height=2, width=95, background='white')
# lb.pack()
# image1 = PhotoImage(name='Bts', file=r"C:\Users\acer\Downloads\BTS.png")
# photo = image1.subsample(3, 5)
# root.mainloop()

# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
#
# num = 0
# canvas = Canvas(root, width=200, height=200)
#
# img_0 = ImageTk.PhotoImage(Image.open("C:/Users/acer/Downloads/Charles Left Hand Corner Sofa, black.jpg"))
# img_1 = ImageTk.PhotoImage(Image.open("C:/Users/acer/Downloads/Lanciano Grey Lint Sofa 62_99D - 94.48D _ Grey"))
#
#
# def task():
#     global num
#
#     canvas.delete("all")
#     canvas.create_text(20, 20, text="loop " + str(num))
#
#     if num % 2 == 0:
#         canvas.create_image(20, 40, anchor=NW, image=img_0)
#
#     if num % 2 == 1:
#         canvas.create_image(20, 40, anchor=NW, image=img_1)
#
#     num += 1
#
#     root.after(2000, task)  # reschedule event in 2 seconds
#
#
# canvas.pack()
# canvas.create_text(20, 20, text="hallo")
#
# root.after(2000, task)
# root.mainloop()

from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("This is our pages")
root.geometry('200x200')

main_frame = Frame(root,bg='light blue')
main_frame.pack(fill=BOTH,expand=True)

page1 = Frame(main_frame)
# page1_lb = Label(page1,text="This is first page",font=('bold',18))
# page1_lb.pack()
page1.pack()

page2 = Frame(main_frame)
page2_lb = Label(page2,text="HOME",font=('bold',18))
page2_lb.pack()
page2.pack()

page3 = Frame(main_frame)
page3_lb = Label(page3,text="MENU",font=('bold',18))
page3_lb.pack()
page3.pack()

page4 = Frame(main_frame)
page4_lb = Label(page4,text="EXIT",font=('bold',18))
page4_lb.pack()
page4.pack()

pages = [page1,page2,page3,page4]
count = 0

def move_next_page():
    global count
    if not count > len(pages)-2:
        for p in pages:
            p.pack_forget()
        count +=1
        page = pages[count]
        page.pack(pady=20)

def move_back_page():
    global count
    if not count ==0:
        for p in pages:
            p.pack_forget()
        count -=1
        page = pages[count]
        page.pack(pady=20)
#
# def clicked():
#     image1_total = int(newImage1_sb.get())+5
#     image2_total = int(newImage1_sb.get())+10
#     image3_total = int(newImage1_sb.get())+15
#     image4_total = int(newImage1_sb.get())+3
#     image5_total = int(newImage1_sb.get())+2
#     image6_total = int(newImage1_sb.get())+5
#     image7_total = int(newImage1_sb.get())+5
#     image8_total = int(newImage1_sb.get())+5
#     total_bill = image1_total+ image2_total +image3_total+image4_total+image5_total+image6_total+image7_total+image8_total
#     total_amount = Label(text=f"Your Total Bill{total_bill}",font=("Arial",10))
#     total_amount.place(x=150,y=600)
#
# resto_name = Label(page1,text="this is our shop",font=("Times New Roman",20,'bold'),bg="Tomato")
# resto_name.grid(column=1,row=0)
#
# quote_label = Label(page1,text="this is our shop",font=("Times New Roman",20,'bold'),bg="Tomato")
# quote_label.grid(row=2,column=1)
#
# food_label = Label(page1,text="this is our shop",font=("Times New Roman",20,'bold'),bg="Tomato")
# food_label.grid(column=0,row=3)
# image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
# image1 = image1.resize((100, 100), Image.ANTIALIAS)
# newImage1 = ImageTk.PhotoImage(image1)
# newImage1_label = Label(image=newImage1,borderwidth=0)
# newImage1_label.place(x=50,y=130)
# newImage1_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage1_info.place(x=40,y=230)
# newImage1_sb = Spinbox(from_=0,to=10,width=5)
# newImage1_sb.place(x=80,y=270)
# image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png")
# image2 = image2.resize((100, 100), Image.ANTIALIAS)
# newImage2 = ImageTk.PhotoImage(image2)
# newImage2_label = Label(image=newImage2,borderwidth=0)
# newImage2_label.place(x=200,y=130)
# newImage2_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage2_info.place(x=210,y=230)
# newImage2_sb = Spinbox(from_=0,to=10,width=5)
# newImage2_sb.place(x=225,y=270)
# image3 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png")
# image3 = image3.resize((100,100),Image.ANTIALIAS)
# newImage3 = ImageTk.PhotoImage(image3)
# newImage3_label = Label(image=newImage3,borderwidth=0)
# newImage3_label.place(x=350,y=130)
# newImage3_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage3_info.place(x=350,y=230)
# newImage3_sb = Spinbox(from_=0,to=10,width=5)
# newImage3_sb.place(x=300,y=270)
# image4 = Image.open("C:/Users/acer/Downloads/table.png")
# image4 = image4.resize((100,100),Image.ANTIALIAS)
# newImage4 = ImageTk.PhotoImage(image4)
# newImage4_label = Label(image=newImage4,borderwidth=0)
# newImage4_label.place(x=200,y=130)
# newImage4_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage4_info.place(x=210,y=230)
# newImage4_sb = Spinbox(from_=0,to=10,width=5)
# newImage4_sb.place(x=225,y=270)
#
# # drink_label = Label(page1,text="this is our shop",font=("Times New Roman",20,'bold'),bg="Tomato")
# # drink_label.grid(x=0,y=350)
# image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
# image1 = image1.resize((100, 100), Image.ANTIALIAS)
# newImage6 = ImageTk.PhotoImage(image1)
# newImage6_label = Label(image=newImage1,borderwidth=0)
# newImage6_label.place(x=50,y=380)
# newImage6_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage6_info.place(x=40,y=480)
# newImage6_sb = Spinbox(from_=0,to=10,width=5)
# newImage6_sb.place(x=80,y=520)
# image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png")
# image2 = image2.resize((100, 100), Image.ANTIALIAS)
# newImage7 = ImageTk.PhotoImage(image2)
# newImage7_label = Label(image=newImage2,borderwidth=0)
# newImage7_label.place(x=200,y=380)
# newImage7_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage7_info.place(x=225,y=480)
# newImage7_sb = Spinbox(from_=0,to=10,width=5)
# newImage7_sb.place(x=230,y=520)
# image3 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png")
# image3 = image3.resize((100,100),Image.ANTIALIAS)
# newImage8 = ImageTk.PhotoImage(image3)
# newImage8_label = Label(image=newImage3,borderwidth=0)
# newImage8_label.place(x=350,y=380)
# newImage8_info =Label(text="This is designer chair\n10500 kyats",font=('Times New Roman',10,'bold'))
# newImage8_info.place(x=360,y=480)
# newImage8_sb = Spinbox(from_=0,to=10,width=5)
# newImage8_sb.place(x=375,y=520)
#
# finish = Button(text="order Finish",command=clicked)
# finish.place(x=210,y=560)
button_frame = Frame(root)
back_button = Button(button_frame,text='Back',font=("Arial",10),command=move_back_page)
back_button.pack(side=LEFT,padx=0)
next_button = Button(button_frame,text='Next',font=("Arial",10),command=move_next_page)
next_button.pack(side=RIGHT,padx=100)
button_frame.pack(side=BOTTOM,pady=10)
root.mainloop()
