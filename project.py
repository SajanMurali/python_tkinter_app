from cProfile import label
from tkinter import *
from turtle import bgcolor, title
from unicodedata import name
root = Tk()
root.title("Registration Form")
root.geometry("500x300")

Label(root, text="Python Programming Registration Form", font="arial 15 bold").grid(row=0, column=3)


name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="Paymentmode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue=StringVar
paymentmodevalue=StringVar
checkvalue=IntVar

nameentry =Entry(root,textvariable=namevalue)
phoneentry =Entry(root,textvariable=phonevalue)
genderentry =Entry(root,textvariable=gendervalue)
paymententry =Entry(root,textvariable=paymentmodevalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymententry.grid(row=4,column=3)
emergencyentry.grid(row=5,column=3)


checkbtn=Checkbutton(text="remember me ?", variable=checkvalue)
checkbtn.grid(row=6,column=3)
root.mainloop()