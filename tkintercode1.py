from tkinter import *

top=Tk()
top.title("main")
top.geometry('400x400')
def r():
    import tkintercode3
    top.destroy()

btn=Button(top,text="Create New Account",command=r).grid(row=0,column=0)
btn=Button(top,text="Deposit").grid(row=1,column=0)
btn=Button(top,text="update account").grid(row=2,column=0)

btn=Button(top,text="show accoount").grid(row=0,column=4)
btn=Button(top,text="Withdraw").grid(row=1,column=4)
btn=Button(top,text="Drop  Account").grid(row=2,column=4)

btn=Button(top,text="back to menu").grid(row=6,column=6)



