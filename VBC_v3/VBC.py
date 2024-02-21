#Name: Hendry
#Date 12/9/23
#Course name: SE116.11
#Project Title: The Very Bad Calculator v3
#Program description: A basic calculator that allows the user to do 4 basic functions (addition, subtraction, multiplication, division) - With functions!! (NOW WITH GUI)
#VARIABLE DICTIONARY:
#add = function that adds 2 numbers
#sub = function that subtracts 2 numbers
#mult = function that multiplies 2 numbers
#div = function that divides 2 numbers
#num1 = first number(float) that will be added/subtracted/multiplied/divided
#num2 = second number(float) that will be added/subtracted/multiplied/divided
#root.geometry = GUI size
#frm = frame where buttons will be on the GUI
#b1 - b6 = buttons 1 - 6

#--------------------------------------CODE START---------------------------------------
from tkinter import *
from math import *

root = Tk()

#FUNCTIONS---------------------------------------------------
def add():

  #delete anything that is inputed into "blank" row
  blank.delete(0, END)

  #equation (num1 + num2)
  ans = float(num1.get()) + float(num2.get())

  #enter 0 into the blank row for answer
  blank.insert(0, ans)



def sub():

  blank.delete(0, END)
  ans = float(num1.get()) - float(num2.get())
  blank.insert(0, ans)



def mult():

  blank.delete(0, END)
  ans = float(num1.get()) * float(num2.get())
  blank.insert(0, ans)



def div():

  blank.delete(0, END)
  ans = float(num1.get()) / float(num2.get())
  blank.insert(0, ans)



def clear():
  blank.delete(0, END)
  num2.delete(0, END)
  num1.delete(0, END)

#---------------------------------------------------------


#Title and canvas geometry
root.geometry("500x150")
root.title("The Very Bad Calculator v3")

#FRAME-----------------------------------
frm = Frame(root)
frm.columnconfigure(0, weight = 1)
frm.columnconfigure(1, weight = 1)

frm.rowconfigure(0, weight = 1)
frm.rowconfigure(1, weight = 1)
#-----------------------------------

#USER ENTRY-----------------------------------------
Label(frm, text = "Num 1:").grid(row = 0)
Label(frm, text = "Num 2:").grid(row = 1)
Label(frm, text = "Answer:").grid(row = 2)

#input
num1 = Entry(frm)
num1.grid(row = 0, column = 1, sticky = "we")

num2 = Entry(frm)
num2.grid(row = 1, column = 1, sticky = "we")

#output
blank = Entry(frm)
blank.grid(row = 2, column = 1, sticky = "we")
#-----------------------------------------------------

#BUTTONS (function call)-------------------------------------------------------------------
b1 = Button(frm, text = "+", command = add)
b1.grid(row = 3, column = 0, sticky = "we")

b2 = Button(frm, text = "-", command = sub)
b2.grid(row = 3, column = 1, sticky = "we")

b3 = Button(frm, text = "x", command = mult)
b3.grid(row = 4, column = 0, sticky = "we")

b4 = Button(frm, text = "/", command = div)
b4.grid(row = 4, column = 1, sticky = "we")

b5 = Button(frm, text = "quit", command = root.destroy)
b5.grid(row = 5, column = 0, sticky = "we")

b6 = Button(frm, text = "clear", command = clear)
b6.grid(row = 5, column = 1, sticky = "we")
#-------------------------------------------------------------------------------------------

frm.pack(fill = "x")

root.mainloop()