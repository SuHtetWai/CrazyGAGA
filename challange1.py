from tkinter import *
from PIL import ImageTk, Image
w1 = Tk()

page1 = Frame(w1)
page2 = Frame(w1)
page3 = Frame(w1)
page4 = Frame(w1)
page5 = Frame(w1)
page6 = Frame(w1)
page7 = Frame(w1)
page8 = Frame(w1)
page1.pack()
page1.place(anchor='center',relx=10,rely=10)


page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
# page6.grid(row=0, column=0, sticky="nsew")

"""For page1"""
page1_label = Label(page1, text="Choose the kinds of furniture do you want to buy", font=('Alice bold', 18),background='grey')
page1_label.pack(pady=10)
image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
image1 = image1.resize((300, 300), Image.ANTIALIAS)
newImage1 = ImageTk.PhotoImage(image1)
image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png")
image2 = image2.resize((300, 300), Image.ANTIALIAS)
newImage2 = ImageTk.PhotoImage(image2)
image3 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png")
image3 = image3.resize((300,300),Image.ANTIALIAS)
newImage3 = ImageTk.PhotoImage(image3)
image4 = Image.open("C:/Users/acer/Downloads/table.png")
image4 = image4.resize((300,300),Image.ANTIALIAS)
newImage4 = ImageTk.PhotoImage(image4)
"""For Settee Page2"""
page2_label = Label(page2, text="This is All Settee Items",font=('Arial bold',18,'italic'),background='ghost white')
page2_label.pack(pady=10)
image5 = Image.open("C:/Users/acer/Downloads/Arthur Chenille 5 Seater Large Corner Sofas.jpg")
image5 = image5.resize((200, 200), Image.ANTIALIAS)
newImage5 = ImageTk.PhotoImage(image5)
newImage5_label = Label(page2,image=newImage5,borderwidth=0)
newImage5_label.place(x=50,y=130)
newImage5_info =Label(page2,text="5 Seater Large Corner Sofas\n10500 kyats",font=('Times New Roman',10,'bold'))
newImage5_info.place(x=40,y=230)
newImage5_sb = Spinbox(page2,from_=0,to=10,width=5)
newImage5_sb.place(x=80,y=270)
image6 = Image.open("C:/Users/acer/Downloads/Five Design trends from High Point Market Spring 2018.jpg")
image6 = image6.resize((200, 200), Image.ANTIALIAS)
newImage6 = ImageTk.PhotoImage(image6)
newImage6_label = Label(page2,image=newImage6,borderwidth=0)
newImage6_label.place(x=200,y=130)
newImage6_info =Label(page2,text="Five Design trends\n10500 kyats",font=('Times New Roman',10,'bold'))
newImage6_info.place(x=210,y=230)
newImage6_sb = Spinbox(page2,from_=0,to=10,width=5)
newImage6_sb.place(x=225,y=270)
image7 = Image.open("C:/Users/acer/Downloads/Lanciano Grey Lint Sofa 62_99D - 94.48D _ Grey")
image7 = image7.resize((200,200),Image.ANTIALIAS)
newImage7 = ImageTk.PhotoImage(image7)
newImage7_label = Label(page2,image=newImage7,borderwidth=0)
newImage7_label.place(x=350,y=130)
newImage7_info =Label(page2,text="Lanciano Grey Lint Sofa\n10500 kyats",font=('Times New Roman',10,'bold'))
newImage7_info.place(x=300,y=230)
newImage7_sb = Spinbox(page2,from_=0,to=10,width=5)
newImage7_sb.place(x=80,y=270)
image8 = Image.open("C:/Users/acer/Downloads/Charles Left Hand Corner Sofa, black.jpg")
image8 = image8.resize((200,200),Image.ANTIALIAS)
newImage8 = ImageTk.PhotoImage(image8)
newImage8_label = Label(page2,image=newImage8,borderwidth=0)
newImage8_label.place(x=200,y=130)
newImage8_info =Label(page2,text="Charles Left Hand Corner Sofa",font=('Times New Roman',10,'bold'))
newImage8_info.place(x=210,y=230)
newImage8_sb = Spinbox(page2,from_=0,to=10,width=5)
newImage8_sb.place(x=225,y=270)


"""For Desk Chair page"""
page3_label = Label(page3, text="This is All Designer Desk Chair",font=("Arial bold",18))
page3_label.pack(pady=10)
image9 = Image.open("C:/Users/acer/Downloads/Desk Chair for Teens Velvet Task Chair Home Office Chair Adjustable Swivel Rolling Vanity Chair with Wheels for Bedroom Study Room, Teal Blue.jpg")
image9 = image9.resize((300, 300), Image.ANTIALIAS)
newImage9 = ImageTk.PhotoImage(image9)
image10 = Image.open("C:/Users/acer/Downloads/677d8e3e-bdb0-48d9-bca1-f34eeedaa425.jpg")
image10= image10.resize((300, 300), Image.ANTIALIAS)
newImage10 = ImageTk.PhotoImage(image10)
image11 = Image.open("C:/Users/acer/Downloads/alki lan chair holds self-adjusting mechanisms within clean curving form.jpg")
image11= image11.resize((300,300),Image.ANTIALIAS)
newImage11 = ImageTk.PhotoImage(image11)
image12 = Image.open("C:/Users/acer/Downloads/Series 430 Chair Vidar 472 – Black – Artilleriet.jpg")
image12 = image12.resize((300,300),Image.ANTIALIAS)
newImage12 = ImageTk.PhotoImage(image12)

"""For bed page"""
page4_label = Label(page4,text="This is All Designer Bed",font=('Arial bold',18))
page4_label.pack(pady=10)
image13 = Image.open("C:/Users/acer/Downloads/Mid-Century Platform Bed – Walnut.jpg")
image13 = image13.resize((300, 300), Image.ANTIALIAS)
newImage13 = ImageTk.PhotoImage(image13)
image14 = Image.open("C:/Users/acer/Downloads/Two Minimalist White Homes with Creative Light and Texture.jpg")
image14= image14.resize((300, 300), Image.ANTIALIAS)
newImage14 = ImageTk.PhotoImage(image14)
image15 = Image.open("C:/Users/acer/Downloads/15 cabeceros originales para tu dormitorio.jpg")
image15= image15.resize((300,300),Image.ANTIALIAS)
newImage15 = ImageTk.PhotoImage(image15)
image16 = Image.open("C:/Users/acer/Downloads/coastal lake house bedroom decor.jpg")
image16 = image16.resize((300,300),Image.ANTIALIAS)
newImage16 = ImageTk.PhotoImage(image16)

"""For Table page"""
page5_label = Label(page5, text="This is All Designer Table",font=("Arial bold",18))
page5_label.pack(pady=10)
image17 = Image.open("C:/Users/acer/Downloads/Cabin In The Woods By Jay Lalka.jpg")
image17 = image17.resize((300, 300), Image.ANTIALIAS)
newImage17 = ImageTk.PhotoImage(image17)
image18 = Image.open("C:/Users/acer/Downloads/Εντυπωσιακές τραπεζαρίες για το σπίτι σου! _ ediva_gr.png")
image18= image18.resize((300, 300), Image.ANTIALIAS)
newImage18 = ImageTk.PhotoImage(image18)
image19 = Image.open("C:/Users/acer/Downloads/Industrial Living Room Collection.jpg")
image19= image19.resize((300,300),Image.ANTIALIAS)
newImage19 = ImageTk.PhotoImage(image19)
image20 = Image.open("C:/Users/acer/Downloads/How To Make a DIY Concrete and Wood Dining Table.jpg")
image20 = image20.resize((300,300),Image.ANTIALIAS)
newImage20 = ImageTk.PhotoImage(image20)

"""Settee"""
btn1 = Button(page1, text="Designer Settee", image=newImage5, command=lambda: page2.tkraise(), compound=BOTTOM)
btn1.pack(side=LEFT,padx=10,pady=10)
my_text =  Text(page2,width=10,height=10,font=("Alice bold",18))
my_text.pack(pady=20,padx=20,side=RIGHT)
btn2 = Button(page2, text="Designer Settee", image=newImage6, command=lambda: page3.tkraise(),compound=BOTTOM)
btn2.pack(side=LEFT,padx=20,pady=20)
btn3 = Button(page2, text="Designer Settee", image=newImage7, command=lambda: page4.tkraise(), compound=BOTTOM)
btn3.pack(side=LEFT,padx=20,pady=20)
btn4 = Button(page2, text="Designer Settee", image=newImage8, command=lambda: page5.tkraise(), compound=BOTTOM)
btn4.pack(side=LEFT,padx=20,pady=20)
"""Desk chair"""
btn5 = Button(page3, text="Designer Desk Chair", image=newImage9, command=lambda: page2.tkraise(), compound=BOTTOM)
btn5.pack(side=LEFT,padx=10,pady=10)
my_text =  Text(page3,width=10,height=10,font=("Alice bold",18))
my_text.pack(pady=20,padx=20,side=RIGHT)
btn6 = Button(page3, text="Designer Desk Chair", image=newImage10, command=lambda: page3.tkraise(),compound=BOTTOM)
btn6.pack(side=LEFT,padx=20,pady=20)
btn7 = Button(page3, text="Designer Desk Chair", image=newImage11, command=lambda: page4.tkraise(), compound=BOTTOM)
btn7.pack(side=LEFT,padx=20,pady=20)
btn8 = Button(page3, text="Designer Desk Chair", image=newImage12, command=lambda: page5.tkraise(), compound=BOTTOM)
btn8.pack(side=LEFT,padx=20,pady=20)

"""Bed"""
btn9 = Button(page4, text="Designer Bed", image=newImage13, command=lambda: page2.tkraise(), compound=BOTTOM)
btn9.pack(side=LEFT,padx=10,pady=10)
my_text =  Text(page4,width=10,height=10,font=("Alice bold",18))
my_text.pack(pady=20,padx=20,side=RIGHT)
btn10 = Button(page4, text="Designer Bed", image=newImage14, command=lambda: page3.tkraise(),compound=BOTTOM)
btn10.pack(side=LEFT,padx=20,pady=20)
btn11 = Button(page4, text="Designer Bed", image=newImage15, command=lambda: page4.tkraise(), compound=BOTTOM)
btn11.pack(side=LEFT,padx=20,pady=20)
btn12 = Button(page4, text="Designer Bed", image=newImage16, command=lambda: page5.tkraise(), compound=BOTTOM)
btn12.pack(side=LEFT,padx=20,pady=20)

"""Table"""
btn13 = Button(page5, text="Designer Table", image=newImage1, command=lambda: page2.tkraise(), compound=BOTTOM)
btn13.pack(side=LEFT,padx=10,pady=10)
my_text = Text(page5,width=10,height=10,font=("Alice bold",18))
my_text.pack(pady=20,padx=20,side=RIGHT)
btn14 = Button(page5, text="Designer Table", image=newImage2, command=lambda: page3.tkraise(),compound=BOTTOM)
btn14.pack(side=LEFT,padx=20,pady=20)
btn15 = Button(page5, text="Designer Table", image=newImage3, command=lambda: page4.tkraise(), compound=BOTTOM)
btn15.pack(side=LEFT,padx=20,pady=20)
btn16 = Button(page5, text="Designer Table", image=newImage4, command=lambda: page5.tkraise(), compound=BOTTOM)
btn16.pack(side=LEFT,padx=20,pady=20)

"""Next and back bottom"""
def tab1():
    def tab2():
        buttom1.destroy()
        def back():
            buttom2.destroy()
        buttom2 = Button(page1,text='BACK',font=('Arial',10),command=back)
        buttom2.pack(side=BOTTOM)
    buttom1 = Button(page2,text='NEXT',font=('Arial',10),command=tab2,activebackground='light blue')
    buttom1.pack(side=BOTTOM)

tab1()
"""For page 2"""


w1.geometry('500x500')
w1.title("This is first window")

w1.mainloop()

# def open():
#     w2 = Toplevel()
#     w2.title("This is second page")
#     w2.geometry('500x500')
#     w2.label=Label(w2,text="This is second window").pack(pady=10)
#     btnClose = Button(w2,text="close",command=w2.destroy).pack(pady=10)
#
# btn = Button(w1,text="to open second window",command=open).pack(pady=20)