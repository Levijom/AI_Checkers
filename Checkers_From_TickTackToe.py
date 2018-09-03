from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("Checkers")

click = True

def checker(buttons):
         global click
         if buttons["text"] == "X" and click == True:
             buttons["text"] = " "
             click = False
         elif buttons["text"] == " " and click == False:
             buttons["text"] = "X"
             click = True


#Button Layout:
#   1   2   3
#   4   5   6
#   7   8   9

buttons=StringVar()

button1 = Button(tk,text="X",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button1))

button1.grid(row=1, column=0,sticky = S+N+E+W)


button2 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button2))

button2.grid(row=1, column=1,sticky = S+N+E+W)


button3 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button3))

button3.grid(row=1, column=2,sticky = S+N+E+W)


button4 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button4))

button4.grid(row=2, column=0,sticky = S+N+E+W)


button5 = Button(tk,text="O",font = ('Times 26 bold'), height = 4 , width =8 , command=lambda:checker(button5))

button5.grid(row=2, column=1,sticky = S+N+E+W)


button6 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button6))

button6.grid(row=2, column=2,sticky = S+N+E+W)


button7 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button7))

button7.grid(row=3, column=0,sticky = S+N+E+W)


button8 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button8))

button8.grid(row=3, column=1,sticky = S+N+E+W)


button9 = Button(tk,text=" ",font = ('Times 26 bold'), height = 4 , width = 8 , command=lambda:checker(button9))

button9.grid(row=3, column=2,sticky = S+N+E+W)


tk.mainloop()
