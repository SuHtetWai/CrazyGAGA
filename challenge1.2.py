from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "firstImage" : 10,
    "secondImage": 14,
    "thirdImage" : 13,
    "fourthImage": 15,
}

w1 = Tk()
w1.title("This is GAGA shop")
w1.minsize(500,500)
def orderId():
    numbers =[0,1,2,3,4,5,6,7,8,9]
    letters = ['A','B','C','D']

    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters = random.choice(letters)
        random_digits = str(random.choice(numbers))

    order_id = random_letters + random_digits
    return order_id
def add():
    current = orderTransaction.cget("text")
    added_order = displayLabel.cget("text")
    updated_order = current + added_order
    orderTransaction.configure(text=updated_order)

    # total = orderTotalLabel.cget("text").replace("Total : ","")
    # total = total.replace("$","")
    # updated_total =total+str(prices[displayLabel.cget("text")])
    # orderTotalLabel.configure(text="Total :"+str(updated_total)+"$")

def add1():
    current1 = orderTransaction1.cget("text")
    added_order1 = displayLabel1.cget("text")
    updated_order1 = current1 + added_order1
    orderTransaction1.configure(text=updated_order1)

    # total1 = orderTotalLabel1.cget("text").replace("Total : ","")
    # total1 = total1.replace("$","")
    # updated_total1 = int(total1)+prices[displayLabel1.cget("text")]
    # orderTotalLabel1.configure(text="Total :"+str(updated_total1)+"$")

def add2():
    current2 = orderTransaction2.cget("text")
    added_order2=displayLabel2.cget("text")
    updated_order2=current2 + added_order2
    orderTransaction2.configure(text=updated_order2)

    # total2 = orderTotalLabel2.cget("text").replace("Total : ","")
    # total2 = total2.replace("$","")
    # updated_total2 = int(total2)+prices[displayLabel2.cget("text")]
    # orderTotalLabel2.configure(text="Total :"+str(updated_total2)+"$")

def add3():
    current3 = orderTransaction3.cget("text")
    added_order3=displayLabel3.cget("text")
    updated_order3=current3 + added_order3
    orderTransaction3.configure(text=updated_order3)

    # total3 = orderTotalLabel3.cget("text").replace("Total : ","")
    # total3 = total3.replace("$","")
    # updated_total3 = int(total3)+prices[displayLabel3.cget("text")]
    # orderTotalLabel3.configure(text="Total :"+str(updated_total3)+"$")

# def order():
#     new_order = orderIDLabel.cget("text")
#     tranList = orderTransaction.cget("text")
#     order_day = datetime.today()
#     order_time = datetime.now()
#
#
#     with open(new_order,"w") as file:
#         file.write("The Binary")
#         file.write("\n")
#         file.write("....................................")
#         file.write("\n")
#         file.write(order_day.strftime("%x"))
#         file.write("\n")
#         file.write(order_time.strftime("%X"))
#         file.write("\n\n")
#         for item in tranList:
#             file.write(item + "\n")
#         file.write("\n\n")
#         file.write(orderTotalLabel.cget("text"))
#     orderTotalLabel.configure("Total+0$")

main_frame = Frame(w1,background='light blue')
main_frame.pack(fill=BOTH,expand=True)
page1 = Frame(main_frame)
page2 = Frame(main_frame)
page3 = Frame(main_frame)
page4 = Frame(main_frame)
page5 = Frame(main_frame)
page1.pack()
page1.place(anchor='center',relx=10,rely=10)
page1_label =Label(page1,text="Choose The Kind of Furniture want to buy",font=('Alice bold',20,'italic'))
page1_label.pack(pady=10)

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")

image1 = Image.open("C:/Users/acer/Pictures/furniture.jpg").resize((300,500))
newImage1 = ImageTk.PhotoImage(image1)
image2 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png").resize((300,500))
newImage2 = ImageTk.PhotoImage(image2)
image3 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png").resize((300,500))
newImage3 = ImageTk.PhotoImage(image3)
image4 = Image.open("C:/Users/acer/Downloads/table.png").resize((300,500))
newImage4 = ImageTk.PhotoImage(image4)

btn1 = Button(page1, text="Designer Settee", image=newImage1, command=lambda: page2.tkraise(), compound=BOTTOM)
btn1.pack(side=LEFT,padx=15,pady=30)
btn2 = Button(page1, text="Designer Desk Chair", image=newImage2, command=lambda: page3.tkraise(), compound=BOTTOM)
btn2.pack(side=LEFT,padx=15,pady=30)
btn3 = Button(page1, text="Designer Bed", image=newImage3, command=lambda: page4.tkraise(), compound=BOTTOM)
btn3.pack(side=LEFT,padx=15,pady=30)
btn4 = Button(page1, text="Designer Table", image=newImage4, command=lambda: page5.tkraise(), compound=BOTTOM)
btn4.pack(side=LEFT,padx=15,pady=30)
page1.tkraise()

s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('ImageFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )
"""For page2"""


LogoImageObject = Image.open("C:/Users/acer/Pictures/furniture.jpg").resize((300, 300))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("C:/Users/acer/Pictures/furniture.jpg").resize((800, 300))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)


displayDefaultImageObject = Image.open("C:/Users/acer/Pictures/furniture.jpg").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

firstImageObject = Image.open("C:/Users/acer/Downloads/Arthur Chenille 5 Seater Large Corner Sofas.jpg").resize((350,334))
firstImage = ImageTk.PhotoImage(firstImageObject)

secondImageObject = Image.open("C:/Users/acer/Downloads/Five Design trends from High Point Market Spring 2018.jpg").resize((350,334))
secondImage = ImageTk.PhotoImage(secondImageObject)

thirdImageObject = Image.open("C:/Users/acer/Downloads/Lanciano Grey Lint Sofa 62_99D - 94.48D _ Grey").resize((350,334))
thirdImage = ImageTk.PhotoImage(thirdImageObject)

fourthImageObject = Image.open("C:/Users/acer/Downloads/Charles Left Hand Corner Sofa, black.jpg").resize((350,334))
fourthImage = ImageTk.PhotoImage(fourthImageObject)

mainFrame = ttk.Frame(page2, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")
mainFrame.pack(padx=10)

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

image1Frame = ttk.Frame(menuFrame, style = "OrderFrame.TFrame")
image1Frame.grid(row = 1, column = 0, sticky = "NSEW")

image2Frame = ttk.Frame(menuFrame,style ="OrderFrame.TFrame")
image2Frame.grid(row = 2, column = 0, sticky ="NSEW")

image3Frame = ttk.Frame(menuFrame, style ="OrderFrame.TFrame")
image3Frame.grid(row = 3, column = 0, sticky ="NSEW")

image4Frame = ttk.Frame(menuFrame, style ="OrderFrame.TFrame")
image4Frame.grid(row = 4, column = 0, sticky ="NSEW")

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

bannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
bannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

def displayImage1():
    image1Frame.configure(
        relief="sunken",
        style="orderFrame.TFrame"
    )
    displayLabel.configure(
        image = firstImage,
        text="Seater Corner ..... 10$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage2():
    image1Frame.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel.configure(
        image = secondImage,
        text="High Point Spring..... 14$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage3():
    image1Frame.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel.configure(
        image = thirdImage,
        text="Grey Lint Sofa..... 23$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage4():
    image1Frame.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel.configure(
        image = fourthImage,
        text="Charles Sofa..... 15$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )
image1Label = ttk.Label(image1Frame, text ="Seater Corner ..... 10$", style ="MenuLabel.TLabel")
image1Label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image2Label = ttk.Label(image2Frame, text ="High Point Spring..... 14$", style ="MenuLabel.TLabel")
image2Label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image3Label = ttk.Label(image3Frame, text ="Grey Lint Sofa..... 23$", style ="MenuLabel.TLabel")
image3Label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image4Label = ttk.Label(image4Frame, text ="Charles Sofa..... 15$", style ="MenuLabel.TLabel")
image4Label.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

image1Button = ttk.Button(image1Frame, text ="Display",command=displayImage1)
image1Button.grid(row = 0, column = 1, padx = 10)

image2Button = ttk.Button(image2Frame, text ="Display",command=displayImage2)
image2Button.grid(row = 0, column = 1, padx = 10)

image3Button = ttk.Button(image3Frame, text ="Display",command=displayImage3)
image3Button.grid(row = 0, column = 1, padx = 10)

image4Button = ttk.Button(image4Frame, text ="Display",command=displayImage4)
image4Button.grid(row = 0, column = 1, padx = 10)



orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ITEMS ")
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

# orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : ", style = "orderTotalLabel.TLabel")
# orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER")
orderButton.grid(row = 4, column = 0, sticky = "EW")

displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER",command=add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE")
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")
"""For page 3"""

s1 = ttk.Style()
s1.configure('MainFrame.TFrame', background = "#2B2B28")
s1.configure('MenuFrame.TFrame', background = "#4A4A48")
s1.configure('DisplayFrame.TFrame', background = "#0F1110")
s1.configure('OrderFrame.TFrame', background = "#B7C4CF")
s1.configure('ImageFrame.TFrame', background = "#4A4A48", relief = "raised")
s1.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s1.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s1.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

image5 = Image.open("C:/Users/acer/Downloads/Desk Chair for Teens Velvet Task Chair Home Office Chair Adjustable Swivel Rolling Vanity Chair with Wheels for Bedroom Study Room, Teal Blue.jpg")
image5 = image5.resize((300, 500))
newImage5 = ImageTk.PhotoImage(image5)
image6 = Image.open("C:/Users/acer/Downloads/677d8e3e-bdb0-48d9-bca1-f34eeedaa425.jpg").resize((300,500))
newImage6 = ImageTk.PhotoImage(image6)
image7 = Image.open("C:/Users/acer/Downloads/alki lan chair holds self-adjusting mechanisms within clean curving form.jpg").resize((300,500))
newImage7 = ImageTk.PhotoImage(image7)
image8 = Image.open("C:/Users/acer/Downloads/Series 430 Chair Vidar 472 – Black – Artilleriet.jpg").resize((300,500))
newImage8 = ImageTk.PhotoImage(image8)

LogoImageObject1 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png").resize((300, 300))
LogoImage1 = ImageTk.PhotoImage(LogoImageObject1)

TopBannerImageObject1 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png").resize((800, 200))
TopBannerImage1 = ImageTk.PhotoImage(TopBannerImageObject1)

displayDefaultImageObject1 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png ").resize((350,360))
displayDefaultImage1 = ImageTk.PhotoImage(displayDefaultImageObject1)

firstImageObject1 = Image.open("C:/Users/acer/Downloads/Desk Chair for Teens Velvet Task Chair Home Office Chair Adjustable Swivel Rolling Vanity Chair with Wheels for Bedroom Study Room, Teal Blue.jpg").resize((350,334))
image_5 = ImageTk.PhotoImage(firstImageObject1)

secondImageObject1 = Image.open("C:/Users/acer/Downloads/677d8e3e-bdb0-48d9-bca1-f34eeedaa425.jpg").resize((350,334))
image_6 = ImageTk.PhotoImage(secondImageObject1)

thirdImageObject1 = Image.open("C:/Users/acer/Downloads/Designer Chairs - High End Seating.png").resize((350,334))
image_7 = ImageTk.PhotoImage(thirdImageObject1)

fourthImageObject1 = Image.open("C:/Users/acer/Downloads/Series 430 Chair Vidar 472 – Black – Artilleriet.jpg").resize((350,334))
image_8 = ImageTk.PhotoImage(fourthImageObject1)

mainFrame1 = ttk.Frame(page3, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame1.grid(row = 0, column = 0, sticky = "NSEW")
mainFrame1.pack(padx=10)
topBannerFrame1 = ttk.Frame(mainFrame1)
topBannerFrame1.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame1 = ttk.Frame(mainFrame1, style = 'MenuFrame.TFrame')
menuFrame1.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame1 = ttk.Frame(mainFrame1, style = "DisplayFrame.TFrame")
displayFrame1.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame1 = ttk.Frame(mainFrame1, style = "OrderFrame.TFrame")
orderFrame1.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

image1Frame1 = ttk.Frame(menuFrame1, style = "DishFrame.TFrame")
image1Frame1.grid(row = 1, column = 0, sticky = "NSEW")

image2Frame1 = ttk.Frame(menuFrame1,style ="DishFrame.TFrame")
image2Frame1.grid(row = 2, column = 0, sticky ="NSEW")

image3Frame1 = ttk.Frame(menuFrame1, style ="DishFrame.TFrame")
image3Frame1.grid(row = 3, column = 0, sticky ="NSEW")

image4Frame1 = ttk.Frame(menuFrame1, style ="DishFrame.TFrame")
image4Frame1.grid(row = 4, column = 0, sticky ="NSEW")

LogoLabel1 = ttk.Label(topBannerFrame1, image = LogoImage1, background = "#0F1110")
LogoLabel1.grid(row = 0, column = 0, sticky = "W")

bannerLabel1 = ttk.Label(topBannerFrame1, image = TopBannerImage1, background = "#0F1110")
bannerLabel1.grid(row = 0, column = 1, sticky = "NSEW")

MainMenuLabel1 = ttk.Label(menuFrame1, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel1.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel1.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

def displayImage5():
    image1Frame1.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel1.configure(
        image = image_5,
        text="Office Chair..... 10$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage6():
    image1Frame1.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel1.configure(
        image = image_6,
        text="Design trends..... 14$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage7():
    image1Frame1.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel1.configure(
        image = image_7,
        text="Self-Adjusting..... 23$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage8():
    image1Frame1.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel1.configure(
        image = image_8,
        text="Chair Vidar..... 15$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

image1Label1 = ttk.Label(image1Frame1, text ="Office Chair..... 10$", style ="MenuLabel.TLabel")
image1Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image2Label1 = ttk.Label(image2Frame1, text ="Design trends..... 14$", style ="MenuLabel.TLabel")
image2Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image3Label1 = ttk.Label(image3Frame1, text ="Self-Adjusting..... 23$", style ="MenuLabel.TLabel")
image3Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image4Label1 = ttk.Label(image4Frame1, text ="Chair Vidar ..... 15$", style ="MenuLabel.TLabel")
image4Label1.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

image1Button1 = ttk.Button(image1Frame1, text ="Display",command=displayImage5)
image1Button1.grid(row = 0, column = 1, padx = 10)

image2Button1 = ttk.Button(image2Frame1, text ="Display",command=displayImage6)
image2Button1.grid(row = 0, column = 1, padx = 10)

image3Button1 = ttk.Button(image3Frame1, text ="Display",command=displayImage7)
image3Button1.grid(row = 0, column = 1, padx = 10)

image4Button1 = ttk.Button(image4Frame1, text ="Display",command=displayImage8)
image4Button1.grid(row = 0, column = 1, padx = 10)



orderTitleLabel1 = ttk.Label(orderFrame1, text = "ORDER")
orderTitleLabel1.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel1.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel1 = ttk.Label(orderFrame1, text = "ORDER ID : " )
orderIDLabel1.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel1.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction1 = ttk.Label(orderFrame1, style = 'orderTransaction.TLabel')
orderTransaction1.grid(row = 2, column = 0, sticky = "NSEW")

# orderTotalLabel1 = ttk.Label(orderFrame1, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
# orderTotalLabel1.grid(row = 3, column = 0, sticky = "EW")

orderButton1 = ttk.Button(orderFrame1, text = "ORDER")
orderButton1.grid(row = 4, column = 0, sticky = "EW")

displayLabel1 = ttk.Label(displayFrame1, image = displayDefaultImage1)
displayLabel1.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel1.configure(background = "#0F1110")

addOrderButton1 = ttk.Button(displayFrame1, text = "ADD TO ORDER",command=add1)
addOrderButton1.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton1 = ttk.Button(displayFrame1, text = "REMOVE")
removeOrderButton1.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

"""For page 4"""

s2 = ttk.Style()
s2.configure('MainFrame.TFrame', background = "#2B2B28")
s2.configure('MenuFrame.TFrame', background = "#4A4A48")
s2.configure('DisplayFrame.TFrame', background = "#0F1110")
s2.configure('OrderFrame.TFrame', background = "#B7C4CF")
s2.configure('ImageFrame.TFrame', background = "#4A4A48", relief = "raised")
s2.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s2.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s2.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

image13 = Image.open("C:/Users/acer/Downloads/Mid-Century Platform Bed – Walnut.jpg").resize((300,500))
newImage13 = ImageTk.PhotoImage(image13)
image14 = Image.open("C:/Users/acer/Downloads/Two Minimalist White Homes with Creative Light and Texture.jpg").resize((300,500))
newImage14 = ImageTk.PhotoImage(image14)
image15 = Image.open("C:/Users/acer/Downloads/15 cabeceros originales para tu dormitorio.jpg").resize((300,500))
newImage15 = ImageTk.PhotoImage(image15)
image16 = Image.open("C:/Users/acer/Downloads/coastal lake house bedroom decor.jpg").resize((300,500))
newImage16 = ImageTk.PhotoImage(image16)

LogoImageObject2 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png").resize((300, 300))
LogoImage2 = ImageTk.PhotoImage(LogoImageObject2)

TopBannerImageObject2 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png").resize((700, 300))
TopBannerImage2 = ImageTk.PhotoImage(TopBannerImageObject2)

displayDefaultImageObject2 = Image.open("C:/Users/acer/Downloads/Best Gray Bedroom Ideas and Design Inspiration [Montenegro Stone House Renovation Vision Board].png ").resize((350,360))
displayDefaultImage2 = ImageTk.PhotoImage(displayDefaultImageObject2)

firstImageObject2 = Image.open("C:/Users/acer/Downloads/Mid-Century Platform Bed – Walnut.jpg").resize((350,334))
image_13 = ImageTk.PhotoImage(firstImageObject2)

secondImageObject2 = Image.open("C:/Users/acer/Downloads/Two Minimalist White Homes with Creative Light and Texture.jpg").resize((350,334))
image_14 = ImageTk.PhotoImage(secondImageObject2)

thirdImageObject2 = Image.open("C:/Users/acer/Downloads/15 cabeceros originales para tu dormitorio.jpg").resize((350,334))
image_15 = ImageTk.PhotoImage(thirdImageObject2)

fourthImageObject2 = Image.open("C:/Users/acer/Downloads/coastal lake house bedroom decor.jpg").resize((350,334))
image_16 = ImageTk.PhotoImage(fourthImageObject2)

mainFrame2 = ttk.Frame(page4, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame2.grid(row = 0, column = 0, sticky = "NSEW")
mainFrame2.pack(padx=10)
topBannerFrame2 = ttk.Frame(mainFrame2)
topBannerFrame2.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame2 = ttk.Frame(mainFrame2, style = 'MenuFrame.TFrame')
menuFrame2.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame2 = ttk.Frame(mainFrame2, style = "DisplayFrame.TFrame")
displayFrame2.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame2 = ttk.Frame(mainFrame2, style = "OrderFrame.TFrame")
orderFrame2.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

image1Frame2 = ttk.Frame(menuFrame2, style = "OrderFrame.TFrame")
image1Frame2.grid(row = 1, column = 0, sticky = "NSEW")

image2Frame2 = ttk.Frame(menuFrame2,style ="OrderFrame.TFrame")
image2Frame2.grid(row = 2, column = 0, sticky ="NSEW")

image3Frame2 = ttk.Frame(menuFrame2, style ="OrderFrame.TFrame")
image3Frame2.grid(row = 3, column = 0, sticky ="NSEW")

image4Frame2 = ttk.Frame(menuFrame2, style ="OrderFrame.TFrame")
image4Frame2.grid(row = 4, column = 0, sticky ="NSEW")

LogoLabel2 = ttk.Label(topBannerFrame2, image = LogoImage2, background = "#0F1110")
LogoLabel2.grid(row = 0, column = 0, sticky = "W")

bannerLabel2 = ttk.Label(topBannerFrame2, image = TopBannerImage2, background = "#0F1110")
bannerLabel2.grid(row = 0, column = 1, sticky = "NSEW")

MainMenuLabel2 = ttk.Label(menuFrame2, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel2.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel2.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

def displayImage9():
    image1Frame2.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel2.configure(
        image = image_13,
        text="Mid-Century BED ..... 10$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage10():
    image1Frame2.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel2.configure(
        image = image_14,
        text="Light & Texture ..... 14$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage11():
    image1Frame2.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel2.configure(
        image = image_15,
        text="Cabeceros BED ..... 23$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage12():
    image1Frame2.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel2.configure(
        image = image_16,
        text="lake house Bedroom ..... 15$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

image1Label2 = ttk.Label(image1Frame2, text ="Mid-Century BED ..... 10$", style ="MenuLabel.TLabel")
image1Label2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image2Label2 = ttk.Label(image2Frame2, text ="Light & Texture ..... 14$", style ="MenuLabel.TLabel")
image2Label2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image3Label2 = ttk.Label(image3Frame2, text ="Cabeceros BED ..... 23$", style ="MenuLabel.TLabel")
image3Label2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image4Label2 = ttk.Label(image4Frame2, text ="lake house Bedroom ..... 15$", style ="MenuLabel.TLabel")
image4Label2.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

image1Button2 = ttk.Button(image1Frame2, text ="Display",command=displayImage9)
image1Button2.grid(row = 0, column = 1, padx = 10)

image2Button2 = ttk.Button(image2Frame2, text ="Display",command=displayImage10)
image2Button2.grid(row = 0, column = 1, padx = 10)

image3Button2 = ttk.Button(image3Frame2, text ="Display",command=displayImage11)
image3Button2.grid(row = 0, column = 1, padx = 10)

image4Button2 = ttk.Button(image4Frame2, text ="Display",command=displayImage12)
image4Button2.grid(row = 0, column = 1, padx = 10)



orderTitleLabel2 = ttk.Label(orderFrame2, text = "ORDER")
orderTitleLabel2.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel2.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel2 = ttk.Label(orderFrame2, text = "ORDER ITEMS ")
orderIDLabel2.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel2.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction2 = ttk.Label(orderFrame2, style = 'orderTransaction.TLabel')
orderTransaction2.grid(row = 2, column = 0, sticky = "NSEW")

# orderTotalLabel2 = ttk.Label(orderFrame2, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
# orderTotalLabel2.grid(row = 3, column = 0, sticky = "EW")

orderButton2 = ttk.Button(orderFrame2, text = "ORDER")
orderButton2.grid(row = 4, column = 0, sticky = "EW")

displayLabel2 = ttk.Label(displayFrame2, image = displayDefaultImage2)
displayLabel2.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel2.configure(background = "#0F1110")

addOrderButton2 = ttk.Button(displayFrame2, text = "ADD TO ORDER",command=add2)
addOrderButton2.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton2 = ttk.Button(displayFrame2, text = "REMOVE")
removeOrderButton2.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

"""For page 5"""

s3 = ttk.Style()
s3.configure('MainFrame.TFrame', background = "#2B2B28")
s3.configure('MenuFrame.TFrame', background = "#4A4A48")
s3.configure('DisplayFrame.TFrame', background = "#0F1110")
s3.configure('OrderFrame.TFrame', background = "#B7C4CF")
s3.configure('ImageFrame.TFrame', background = "#4A4A48", relief = "raised")
s3.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s3.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s3.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

image17 = Image.open("C:/Users/acer/Downloads/Cabin In The Woods By Jay Lalka.jpg").resize((300,500))
newImage17 = ImageTk.PhotoImage(image17)
image18 = Image.open("C:/Users/acer/Downloads/Εντυπωσιακές τραπεζαρίες για το σπίτι σου! _ ediva_gr.png").resize((300,500))
newImage18 = ImageTk.PhotoImage(image18)
image19 = Image.open("C:/Users/acer/Downloads/Industrial Living Room Collection.jpg").resize((300,500))
newImage19 = ImageTk.PhotoImage(image19)
image20 = Image.open("C:/Users/acer/Downloads/How To Make a DIY Concrete and Wood Dining Table.jpg").resize((300,500))
newImage20 = ImageTk.PhotoImage(image20)

LogoImageObject3 = Image.open("C:/Users/acer/Downloads/table.png").resize((300, 300))
LogoImage3 = ImageTk.PhotoImage(LogoImageObject3)

TopBannerImageObject3 = Image.open("C:/Users/acer/Downloads/table.png").resize((700, 300))
TopBannerImage3 = ImageTk.PhotoImage(TopBannerImageObject3)

displayDefaultImageObject3 = Image.open("C:/Users/acer/Downloads/table.png").resize((350,360))
displayDefaultImage3 = ImageTk.PhotoImage(displayDefaultImageObject3)

firstImageObject3 = Image.open("C:/Users/acer/Downloads/Cabin In The Woods By Jay Lalka.jpg").resize((350,334))
image_17 = ImageTk.PhotoImage(firstImageObject2)

secondImageObject3 = Image.open("C:/Users/acer/Downloads/Εντυπωσιακές τραπεζαρίες για το σπίτι σου! _ ediva_gr.png").resize((350,334))
image_18 = ImageTk.PhotoImage(secondImageObject3)

thirdImageObject3 = Image.open("C:/Users/acer/Downloads/Industrial Living Room Collection.jpg").resize((350,334))
image_19 = ImageTk.PhotoImage(thirdImageObject3)

fourthImageObject3 = Image.open("C:/Users/acer/Downloads/How To Make a DIY Concrete and Wood Dining Table.jpg").resize((350,334))
image_20 = ImageTk.PhotoImage(fourthImageObject3)

mainFrame3 = ttk.Frame(page5, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame3.grid(row = 0, column = 0, sticky = "NSEW")
mainFrame3.pack(padx=10)
topBannerFrame3 = ttk.Frame(mainFrame3)
topBannerFrame3.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame3 = ttk.Frame(mainFrame3, style = 'MenuFrame.TFrame')
menuFrame3.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame3 = ttk.Frame(mainFrame3, style = "DisplayFrame.TFrame")
displayFrame3.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame3 = ttk.Frame(mainFrame3, style = "OrderFrame.TFrame")
orderFrame3.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

image1Frame3 = ttk.Frame(menuFrame3, style = "OrderFrame.TFrame")
image1Frame3.grid(row = 1, column = 0, sticky = "NSEW")

image2Frame3 = ttk.Frame(menuFrame3,style ="OrderFrame.TFrame")
image2Frame3.grid(row = 2, column = 0, sticky ="NSEW")

image3Frame3 = ttk.Frame(menuFrame3, style ="OrderFrame.TFrame")
image3Frame3.grid(row = 3, column = 0, sticky ="NSEW")

image4Frame3 = ttk.Frame(menuFrame3, style ="OrderFrame.TFrame")
image4Frame3.grid(row = 4, column = 0, sticky ="NSEW")

LogoLabel3 = ttk.Label(topBannerFrame3, image = LogoImage3, background = "#0F1110")
LogoLabel3.grid(row = 0, column = 0, sticky = "W")

bannerLabel3 = ttk.Label(topBannerFrame3, image = TopBannerImage3, background = "#0F1110")
bannerLabel3.grid(row = 0, column = 1, sticky = "NSEW")

MainMenuLabel3 = ttk.Label(menuFrame3, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel3.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel3.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

def displayImage13():
    image1Frame3.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel3.configure(
        image = image_17,
        text="Cabin Woods..... 10$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage14():
    image1Frame3.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel3.configure(
        image = image_18,
        text="Designer Table ..... 14$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage15():
    image1Frame3.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel3.configure(
        image = image_19,
        text="Industrial Table ..... 23$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

def displayImage16():
    image1Frame3.configure(
        relief="sunken",
        style="Select Image to order.TFrame"
    )
    displayLabel3.configure(
        image = image_20,
        text="Wood Dining Table ..... 15$",
        font=('Helvetica',14,"bold"),
        compound="bottom",
        foreground="white",
        padding=(5,5,5,5)
    )

image1Label3 = ttk.Label(image1Frame3, text ="Cabin Woods..... 10$", style ="MenuLabel.TLabel")
image1Label3.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image2Label3 = ttk.Label(image2Frame3, text ="Designer Table ..... 14$", style ="MenuLabel.TLabel")
image2Label3.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image3Label3 = ttk.Label(image3Frame3, text ="Industrial Table ..... 23$", style ="MenuLabel.TLabel")
image3Label3.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

image4Label3 = ttk.Label(image4Frame3, text ="Wood Dining Table ..... 15$", style ="MenuLabel.TLabel")
image4Label3.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

image1Button3 = ttk.Button(image1Frame3, text ="Display",command=displayImage13)
image1Button3.grid(row = 0, column = 1, padx = 10)

image2Button3 = ttk.Button(image2Frame3, text ="Display",command=displayImage14)
image2Button3.grid(row = 0, column = 1, padx = 10)

image3Button3 = ttk.Button(image3Frame3, text ="Display",command=displayImage15)
image3Button3.grid(row = 0, column = 1, padx = 10)

image4Button3 = ttk.Button(image4Frame3, text ="Display",command=displayImage16)
image4Button3.grid(row = 0, column = 1, padx = 10)




orderTitleLabel3 = ttk.Label(orderFrame3, text = "ORDER")
orderTitleLabel3.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel3.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel3 = ttk.Label(orderFrame3, text = "ORDER ITEMS ")
orderIDLabel3.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel3.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction3 = ttk.Label(orderFrame3, style = 'orderTransaction.TLabel')
orderTransaction3.grid(row = 2, column = 0, sticky = "NSEW")

# orderTotalLabel3 = ttk.Label(orderFrame3, text = "TOTAL ", style = "orderTotalLabel.TLabel")
# orderTotalLabel3.grid(row = 3, column = 0, sticky = "EW")

orderButton3 = ttk.Button(orderFrame3, text = "ORDER")
orderButton3.grid(row = 4, column = 0, sticky = "EW")

displayLabel3 = ttk.Label(displayFrame3, image = displayDefaultImage3)
displayLabel3.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel3.configure(background = "#0F1110")

addOrderButton3 = ttk.Button(displayFrame3, text = "ADD TO ORDER",command=add3)
addOrderButton3.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton3 = ttk.Button(displayFrame3, text = "REMOVE")
removeOrderButton3.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")


"""For page 2"""
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)

"""For page 3"""
mainFrame1.columnconfigure(2, weight = 1)
mainFrame1.rowconfigure(1, weight = 1)
menuFrame1.columnconfigure(0, weight = 1)
menuFrame1.rowconfigure(1, weight = 1)
menuFrame1.rowconfigure(2, weight = 1)
menuFrame1.rowconfigure(3, weight = 1)
menuFrame1.rowconfigure(4, weight = 1)
menuFrame1.rowconfigure(5, weight = 1)
menuFrame1.rowconfigure(6, weight = 1)
orderFrame1.columnconfigure(0, weight = 1)
orderFrame1.rowconfigure(2, weight = 1)

"""For page 4"""
mainFrame2.columnconfigure(2, weight = 1)
mainFrame2.rowconfigure(1, weight = 1)
menuFrame2.columnconfigure(0, weight = 1)
menuFrame2.rowconfigure(1, weight = 1)
menuFrame2.rowconfigure(2, weight = 1)
menuFrame2.rowconfigure(3, weight = 1)
menuFrame2.rowconfigure(4, weight = 1)
menuFrame2.rowconfigure(5, weight = 1)
menuFrame2.rowconfigure(6, weight = 1)
orderFrame2.columnconfigure(0, weight = 1)
orderFrame2.rowconfigure(2, weight = 1)

"""For page 5"""

mainFrame3.columnconfigure(2, weight = 1)
mainFrame3.rowconfigure(1, weight = 1)
menuFrame3.columnconfigure(0, weight = 1)
menuFrame3.rowconfigure(1, weight = 1)
menuFrame3.rowconfigure(2, weight = 1)
menuFrame3.rowconfigure(3, weight = 1)
menuFrame3.rowconfigure(4, weight = 1)
menuFrame3.rowconfigure(5, weight = 1)
menuFrame3.rowconfigure(6, weight = 1)
orderFrame3.columnconfigure(0, weight = 1)
orderFrame3.rowconfigure(2, weight = 1)
w1.mainloop()