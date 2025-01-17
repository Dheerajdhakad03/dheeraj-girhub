from tkinter import *

top=Tk()
top.geometry('400x400')
def rn():
    import tkintercode1
    top.destroy()

btn=Button(text="Customer menu",command=rn).grid(row=0,column=0)
btn=Button(text="Employee menu").grid(row=0,column=1)

