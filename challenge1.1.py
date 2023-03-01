from tkinter import *
from  PIL import ImageTk,Image
w1= Tk()
w1.title("This is GAGA shop")
main_frame = Frame(w1,background='light blue')
main_frame.pack(fill=BOTH,expand=True)
page1 = Frame(main_frame)
page2 = Frame(main_frame)
page3 = Frame(main_frame)
page4 = Frame(main_frame)
page5 = Frame(main_frame)
page6 = Frame(main_frame)
page7 = Frame(main_frame)
page8 = Frame(main_frame)
page9 = Frame(main_frame)
page10 = Frame(main_frame)
page11 = Frame(main_frame)
page12 = Frame(main_frame)
page13 = Frame(main_frame)
page14 = Frame(main_frame)
page15 = Frame(main_frame)
page16 = Frame(main_frame)
page17 = Frame(main_frame)
page18 = Frame(main_frame)
page19 = Frame(main_frame)
page20 = Frame(main_frame)
page21 = Frame(main_frame)
page1.pack()
page1.place(anchor='center',relx=10,rely=10)


page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
page6.grid(row=0, column=0, sticky="nsew")
page7.grid(row=0, column=0, sticky="nsew")
page8.grid(row=0, column=0, sticky="nsew")
page9.grid(row=0, column=0, sticky="nsew")
page10.grid(row=0, column=0, sticky="nsew")
page11.grid(row=0, column=0, sticky="nsew")
page12.grid(row=0, column=0, sticky="nsew")
page13.grid(row=0, column=0, sticky="nsew")
page14.grid(row=0, column=0, sticky="nsew")
page15.grid(row=0, column=0, sticky="nsew")
page16.grid(row=0, column=0, sticky="nsew")
page17.grid(row=0, column=0, sticky="nsew")
page18.grid(row=0, column=0, sticky="nsew")
page19.grid(row=0, column=0, sticky="nsew")
page20.grid(row=0, column=0, sticky="nsew")
page21.grid(row=0, column=0, sticky="nsew")

"""For page 1"""

image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg")
image1 = image1.resize((300, 500), Image.ANTIALIAS)
newImage1 = ImageTk.PhotoImage(image1)
image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png")
image2 = image2.resize((300, 500), Image.ANTIALIAS)
newImage2 = ImageTk.PhotoImage(image2)
image3 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png")
image3 = image3.resize((300,500),Image.ANTIALIAS)
newImage3 = ImageTk.PhotoImage(image3)
image4 = Image.open("C:/Users/acer/Downloads/table.png")
image4 = image4.resize((300,500),Image.ANTIALIAS)
newImage4 = ImageTk.PhotoImage(image4)

"""For page1 button"""
btn1 = Button(page1, text="Designer Settee", image=newImage1, command=lambda: page2.tkraise(), compound=BOTTOM)
btn1.pack(side=LEFT,padx=15,pady=30)
btn2 = Button(page1, text="Designer Desk Chair", image=newImage2, command=lambda: page3.tkraise(), compound=BOTTOM)
btn2.pack(side=LEFT,padx=15,pady=30)
btn3 = Button(page1, text="Designer Bed", image=newImage3, command=lambda: page4.tkraise(), compound=BOTTOM)
btn3.pack(side=LEFT,padx=15,pady=30)
btn4 = Button(page1, text="Designer Table", image=newImage4, command=lambda: page5.tkraise(), compound=BOTTOM)
btn4.pack(side=LEFT,padx=15,pady=30)
page1.tkraise()

"""For page2"""

image5 = Image.open("C:/Users/acer/Downloads/Arthur Chenille 5 Seater Large Corner Sofas.jpg")
image5 = image5.resize((300, 200), Image.ANTIALIAS)
newImage5 = ImageTk.PhotoImage(image5)
image6 = Image.open("C:/Users/acer/Downloads/Five Design trends from High Point Market Spring 2018.jpg")
image6 = image6.resize((300, 200), Image.ANTIALIAS)
newImage6 = ImageTk.PhotoImage(image6)
image7 = Image.open("C:/Users/acer/Downloads/Lanciano Grey Lint Sofa 62_99D - 94.48D _ Grey")
image7 = image7.resize((300,200),Image.ANTIALIAS)
newImage7 = ImageTk.PhotoImage(image7)
image8 = Image.open("C:/Users/acer/Downloads/Charles Left Hand Corner Sofa, black.jpg")
image8 = image8.resize((300,200),Image.ANTIALIAS)
newImage8 = ImageTk.PhotoImage(image8)
"""For page 2 Button"""
btn5 = Button(page2, text="Arthur Chenille 5 Seater Large Corner Sofas", image=newImage5, command=lambda: page6.tkraise(), compound=BOTTOM)
btn5.pack(side=LEFT,padx=15,pady=30)
btn6 = Button(page2, text="Five Design trends from High Point Market Spring", image=newImage6, command=lambda: page7.tkraise(), compound=BOTTOM)
btn6.pack(side=LEFT,padx=15,pady=30)
btn7 = Button(page2, text="Lanciano Grey Lint Sofa ", image=newImage7, command=lambda: page8.tkraise(), compound=BOTTOM)
btn7.pack(side=LEFT,padx=15,pady=30)
btn8 = Button(page2, text="Charles Left Hand Corner Sofa", image=newImage8, command=lambda: page9.tkraise(), compound=BOTTOM)
btn8.pack(side=LEFT,padx=15,pady=30)


"""For page 3"""

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

"""For page 3 button"""
btn13 = Button(page3, text="Desk Chair for Teens Velvet Task Chair Home Office Chair", image=newImage9, command=lambda: page10.tkraise(), compound=BOTTOM)
btn13.pack(side=LEFT,padx=15,pady=30)
btn14 = Button(page3, text="Five Design trends from High Point Market Spring", image=newImage10, command=lambda: page11.tkraise(), compound=BOTTOM)
btn14.pack(side=LEFT,padx=15,pady=30)
btn15 = Button(page3, text="Alki lan chair holds self-adjusting mechanisms ", image=newImage11, command=lambda: page12.tkraise(), compound=BOTTOM)
btn15.pack(side=LEFT,padx=15,pady=30)
btn16 = Button(page3, text="Series 430 Chair Vidar", image=newImage12, command=lambda: page13.tkraise(), compound=BOTTOM)
btn16.pack(side=LEFT,padx=15,pady=30)

"""For page 4"""

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

"""For page 4 button"""
btn17 = Button(page4, text="Desk Chair for Teens Velvet Task Chair Home Office Chair", image=newImage13, command=lambda: page14.tkraise(), compound=BOTTOM)
btn17.pack(side=LEFT,padx=15,pady=30)
btn18 = Button(page4, text="Five Design trends from High Point Market Spring", image=newImage14, command=lambda: page15.tkraise(), compound=BOTTOM)
btn18.pack(side=LEFT,padx=15,pady=30)
btn19 = Button(page4, text="Alki lan chair holds self-adjusting mechanisms ", image=newImage15, command=lambda: page16.tkraise(), compound=BOTTOM)
btn19.pack(side=LEFT,padx=15,pady=30)
btn20 = Button(page4, text="Series 430 Chair Vidar", image=newImage16, command=lambda: page17.tkraise(), compound=BOTTOM)
btn20.pack(side=LEFT,padx=15,pady=30)


"""For page 5"""


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

"""For page 5 Button"""
btn21 = Button(page4, text="Desk Chair for Teens Velvet Task Chair Home Office Chair", image=newImage17, command=lambda: page15.tkraise(), compound=BOTTOM)
btn21.pack(side=LEFT,padx=15,pady=30)
btn22 = Button(page4, text="Five Design trends from High Point Market Spring", image=newImage18, command=lambda: page16.tkraise(), compound=BOTTOM)
btn22.pack(side=LEFT,padx=15,pady=30)
btn23 = Button(page4, text="Alki lan chair holds self-adjusting mechanisms ", image=newImage19, command=lambda: page17.tkraise(), compound=BOTTOM)
btn23.pack(side=LEFT,padx=15,pady=30)
btn24 = Button(page4, text="Series 430 Chair Vidar", image=newImage20, command=lambda: page18.tkraise(), compound=BOTTOM)
btn24.pack(side=LEFT,padx=15,pady=30)

"""Display site"""
image_1 = Image.open("C:/Users/acer/Downloads/Arthur Chenille 5 Seater Large Corner Sofas.jpg")
image_1 = image_1.resize((500, 500), Image.ANTIALIAS)
newImage_1 = ImageTk.PhotoImage(image_1)
image5_display = Label(page6,text="Arthur Chenille 5 Seater Large Corner Sofas",image=newImage_1)
image5_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image5_display.configure(background="light blue")

orderBtn = Button(page6,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page6,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_2 = Image.open("C:/Users/acer/Downloads/Five Design trends from High Point Market Spring 2018.jpg")
image_2 = image_2.resize((500, 500), Image.ANTIALIAS)
newImage_2 = ImageTk.PhotoImage(image_2)
image6_display = Label(page7,text="Five Design trends from High Point Market Spring",image=newImage_2)
image6_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image6_display.configure(background="light blue")

orderBtn = Button(page7,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page7,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_3 = Image.open("C:/Users/acer/Downloads/Lanciano Grey Lint Sofa 62_99D - 94.48D _ Grey")
image_3 = image_3.resize((500, 500), Image.ANTIALIAS)
newImage_3 = ImageTk.PhotoImage(image_3)
image7_display = Label(page8,text="Lanciano Grey Lint Sofa",image=newImage_3)
image7_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image7_display.configure(background="light blue")

orderBtn = Button(page8,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page8,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_4 = Image.open("C:/Users/acer/Downloads/Charles Left Hand Corner Sofa, black.jpg")
image_4 = image_4.resize((500, 500), Image.ANTIALIAS)
newImage_4 = ImageTk.PhotoImage(image_4)
image8_display = Label(page9,text="Arthur Chenille 5 Seater Large Corner Sofas",image=newImage_4)
image8_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image8_display.configure(background="light blue")

orderBtn = Button(page9,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page9,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_5 = Image.open("C:/Users/acer/Downloads/Desk Chair for Teens Velvet Task Chair Home Office Chair Adjustable Swivel Rolling Vanity Chair with Wheels for Bedroom Study Room, Teal Blue.jpg")
image_5 = image_5.resize((500, 500), Image.ANTIALIAS)
newImage_5 = ImageTk.PhotoImage(image_5)
image9_display = Label(page10,text="Arthur Chenille 5 Seater Large Corner Sofas",image=newImage_5)
image9_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image9_display.configure(background="light blue")

orderBtn = Button(page10,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page10,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')


image_6 = Image.open("C:/Users/acer/Downloads/677d8e3e-bdb0-48d9-bca1-f34eeedaa425.jpg")
image_6 = image_6.resize((500, 500), Image.ANTIALIAS)
newImage_6 = ImageTk.PhotoImage(image_6)
image10_display = Label(page11,text="Designer Chair",image=newImage_6)
image10_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image10_display.configure(background="light blue")

orderBtn = Button(page11,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page11,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_7 = Image.open("C:/Users/acer/Downloads/alki lan chair holds self-adjusting mechanisms within clean curving form.jpg")
image_7= image_7.resize((500, 500), Image.ANTIALIAS)
newImage_7 = ImageTk.PhotoImage(image_7)
image11_display = Label(page12,text="Alki lan chair holds self-adjusting mechanisms ",image=newImage_7)
image11_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image11_display.configure(background="light blue")

orderBtn = Button(page12,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page12,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_8 = Image.open("C:/Users/acer/Downloads/Series 430 Chair Vidar 472 – Black – Artilleriet.jpg")
image_8 = image_8.resize((500, 500), Image.ANTIALIAS)
newImage_8 = ImageTk.PhotoImage(image_8)
image12_display = Label(page13,text="Series 430 Chair",image=newImage_8)
image12_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image12_display.configure(background="light blue")

orderBtn = Button(page13,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page13,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

image_9 = Image.open("C:/Users/acer/Downloads/Arthur Chenille 5 Seater Large Corner Sofas.jpg")
image_9 = image_9.resize((500, 500), Image.ANTIALIAS)
newImage_9 = ImageTk.PhotoImage(image_9)
image13_display = Label(page14,text="Arthur Chenille 5 Seater Large Corner Sofas",image=newImage_9)
image13_display.grid(row=0,column=0,sticky='nsew',columnspan=2)
image13_display.configure(background="light blue")

orderBtn = Button(page14,text="Add to Order")
orderBtn.grid(row=1,column=0,padx=2,sticky='nsew')

deleteBtn=Button(page14,text="Remove order")
deleteBtn.grid(row=1,column=1,padx=2,sticky='nsew')

pages = [page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11,page12,page13,page15,page16,page17,page18,page19,page20,page21]
count = 0
def move_back_page():
    global count
    if not count ==0:
        for p in pages:
            p.pack_forget()
        count -=1
        page = pages[count]
        page.pack(pady=20)

def saveinfo():
    orderInfo = order.get()
    file = open("user.txt","w")
    file.write("Your order number"+orderInfo)
    file.close()


order = Label(text="Order")
order.pack()
button_frame = Frame(w1)
back_button = Button(button_frame,text='Back',font=("Arial",10),command=move_back_page)
back_button.pack(side=LEFT,padx=0)
button_frame.pack()
w1.mainloop()