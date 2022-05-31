from math import *
from random import  *
from tkinter import *
class Calculator:
    def __init__(self):
        self.root = Tk()
        self.e = Entry(self.root, width = 35, borderwidth = 5)
        self.e.grid(row = 0,  column =  0, columnspan  = 3, padx = 10, pady = 10)
    def start(self):
        #we set  window's title.
        self.root.title("Calculator")
        #we define buttons and them size
        button_1  = Button(self.root, text= "1", padx= 40,  pady = 20, command =  lambda: self.button_click(1))
        button_2  = Button(self.root, text= "2", padx= 40,  pady = 20, command = lambda: self.button_click(2))
        button_3  = Button(self.root, text= "3", padx= 40,  pady = 20, command = lambda: self.button_click(3))
        button_4  = Button(self.root, text= "4", padx= 40,  pady = 20, command = lambda: self.button_click(4))
        button_5  = Button(self.root, text= "5", padx= 40,  pady = 20, command = lambda: self.button_click(5))
        button_6  = Button(self.root, text= "6", padx= 40,  pady = 20, command = lambda: self.button_click(6))
        button_7  = Button(self.root, text= "7", padx= 40,  pady = 20, command = lambda: self.button_click(7))
        button_8  = Button(self.root, text= "8", padx= 40,  pady = 20, command = lambda: self.button_click(8))
        button_9  = Button(self.root, text= "9", padx= 40,  pady = 20, command = lambda: self.button_click(9))
        button_0  = Button(self.root, text= "0", padx= 40,  pady = 20, command = lambda: self.button_click(0))
        button_sum = Button(self.root, text= "+", padx= 39,  pady = 20, command =  self.button_sum)
        button_minus = Button(self.root, text= "-", padx= 40,  pady = 20, command = lambda: self.button_click())
        button_multi = Button(self.root, text= "*", padx= 40,  pady = 20, command = lambda: self.button_click())
        button_div = Button(self.root, text= "/", padx= 40,  pady = 20, command = lambda: self.button_click())
        button_eq =  Button(self.root, text= "=", padx= 40,  pady = 20, command = self.button_equal)
        button_clear = Button(self.root, text= "clear", padx= 40,  pady = 20, command =  self.button_clear)
        #we set buttons on gui
        button_1.grid(row = 3, column = 0) 
        button_2.grid(row = 3, column = 1) 
        button_3.grid(row = 3, column = 2) 
        button_4.grid(row = 2, column = 0) 
        button_5.grid(row = 2, column = 1) 
        button_6.grid(row = 2, column = 2) 
        button_7.grid(row = 1, column = 0) 
        button_8.grid(row = 1, column = 1) 
        button_9.grid(row = 1, column = 2) 
        button_0.grid(row = 4, column = 0) 
        button_sum.grid(row = 4, column = 1)
        button_minus.grid(row = 4, column = 2)
        button_multi.grid(row = 5, column = 0)
        button_div.grid(row = 5, column  =  1)
        button_eq.grid(row = 5, column = 2)
        button_clear.grid(row = 6, column= 0)
        self.root.mainloop()
    def button_click(self, number):
        current =  self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))
    def button_clear(self):
        self.e.delete(0, END)
    def button_sum(self):
        first_number = self.e.get()
        global  f_num 
        f_num = int(first_number)
        self.e.delete(0, END)
    def  button_equal(self):
        second_number = self.e.get()
        self.e.delete(0,  END)
        self.e.insert(0, f_num  + int(second_number))
if __name__ == "__main__":
    Calculator().start()
