from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("Checkers")

clickX = True
clickO = True

def checker(buttons):
         global clickX
         if buttons["text"] == "X" and clickX == True:
             buttons["text"] = " "
             clickX = False
         elif buttons["text"] == " " and clickX == False:
             buttons["text"] = "X"
             clickX = True
             
         global clickO
         if buttons["text"] == "O" and clickO == True:
             buttons["text"] = " "
             clickO = False
         elif buttons["text"] == " " and clickO == False:
             buttons["text"] = "O"
             clickO = True


#Old Button Layout:
#   1   2   3

#   4   5   6

#   7   8   9

#New Button Layout
#   1   2   3   4   5   6   7   8

#   9   10  11  12  13  14  15  16

#   17  18  19  20  21  22  23  24

#   25  26  27  28  29  30  31  32

#   33  34  35  36  37  38  39  40

#   41  42  43  44  45  46  47  48

#   49  50  51  52  53  54  55  56

#   57  58  59  60  61  62  63  64


buttons=StringVar()

button1 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button1))

button1.grid(row=1, column=0,sticky = S+N+E+W)


button2 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button2))

button2.grid(row=1, column=1,sticky = S+N+E+W)


button3 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button3))

button3.grid(row=1, column=2,sticky = S+N+E+W)


button4 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button4))

button4.grid(row=1, column=3,sticky = S+N+E+W)


button5 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button5))

button5.grid(row=1, column=4,sticky = S+N+E+W)


button6 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button6))

button6.grid(row=1, column=5,sticky = S+N+E+W)


button7 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button7))

button7.grid(row=1, column=6,sticky = S+N+E+W)


button8 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button8))

button8.grid(row=1, column=7,sticky = S+N+E+W)




button9 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button9))

button9.grid(row=2, column=0,sticky = S+N+E+W)


button10 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button10))

button10.grid(row=2, column=1,sticky = S+N+E+W)


button11 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button11))

button11.grid(row=2, column=2,sticky = S+N+E+W)


button12 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button12))

button12.grid(row=2, column=3,sticky = S+N+E+W)


button13 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button13))

button13.grid(row=2, column=4,sticky = S+N+E+W)


button14 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button14))

button14.grid(row=2, column=5,sticky = S+N+E+W)


button15 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button15))

button15.grid(row=2, column=6,sticky = S+N+E+W)


button16 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button16))

button16.grid(row=2, column=7,sticky = S+N+E+W)




button17 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button17))

button17.grid(row=3, column=0,sticky = S+N+E+W)


button18 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button18))

button18.grid(row=3, column=1,sticky = S+N+E+W)


button19 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button19))

button19.grid(row=3, column=2,sticky = S+N+E+W)


button20 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button20))

button20.grid(row=3, column=3,sticky = S+N+E+W)


button21 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button21))

button21.grid(row=3, column=4,sticky = S+N+E+W)


button22 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button22))

button22.grid(row=3, column=5,sticky = S+N+E+W)


button23 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button23))

button23.grid(row=3, column=6,sticky = S+N+E+W)


button24 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button24))

button24.grid(row=3, column=7,sticky = S+N+E+W)




button25 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button25))

button25.grid(row=4, column=0,sticky = S+N+E+W)


button26 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button26))

button26.grid(row=4, column=1,sticky = S+N+E+W)


button27 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button27))

button27.grid(row=4, column=2,sticky = S+N+E+W)


button28 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button28))

button28.grid(row=4, column=3,sticky = S+N+E+W)


button29 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button29))

button29.grid(row=4, column=4,sticky = S+N+E+W)


button30 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button30))

button30.grid(row=4, column=5,sticky = S+N+E+W)


button31 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button31))

button31.grid(row=4, column=6,sticky = S+N+E+W)


button32 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button32))

button32.grid(row=4, column=7,sticky = S+N+E+W)




button33 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button33))

button33.grid(row=5, column=0,sticky = S+N+E+W)


button34 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button34))

button34.grid(row=5, column=1,sticky = S+N+E+W)


button35 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button35))

button35.grid(row=5, column=2,sticky = S+N+E+W)


button36 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button36))

button36.grid(row=5, column=3,sticky = S+N+E+W)


button37 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button37))

button37.grid(row=5, column=4,sticky = S+N+E+W)


button38 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button38))

button38.grid(row=5, column=5,sticky = S+N+E+W)


button39 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button39))

button39.grid(row=5, column=6,sticky = S+N+E+W)


button40 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button40))

button40.grid(row=5, column=7,sticky = S+N+E+W)




button41 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button41))

button41.grid(row=6, column=0,sticky = S+N+E+W)


button42 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button42))

button42.grid(row=6, column=1,sticky = S+N+E+W)


button43 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button43))

button43.grid(row=6, column=2,sticky = S+N+E+W)


button44 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button44))

button44.grid(row=6, column=3,sticky = S+N+E+W)


button45 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button45))

button45.grid(row=6, column=4,sticky = S+N+E+W)


button46 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button46))

button46.grid(row=6, column=5,sticky = S+N+E+W)


button47 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button47))

button47.grid(row=6, column=6,sticky = S+N+E+W)


button48 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button48))

button48.grid(row=6, column=7,sticky = S+N+E+W)




button49 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button49))

button49.grid(row=7, column=0,sticky = S+N+E+W)


button50 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button50))

button50.grid(row=7, column=1,sticky = S+N+E+W)


button51 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button51))

button51.grid(row=7, column=2,sticky = S+N+E+W)


button52 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button52))

button52.grid(row=7, column=3,sticky = S+N+E+W)


button53 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button53))

button53.grid(row=7, column=4,sticky = S+N+E+W)


button54 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button54))

button54.grid(row=7, column=5,sticky = S+N+E+W)


button55 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button55))

button55.grid(row=7, column=6,sticky = S+N+E+W)


button56 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button56))

button56.grid(row=7, column=7,sticky = S+N+E+W)




button57 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button57))

button57.grid(row=8, column=0,sticky = S+N+E+W)


button58 = Button(tk,text="X",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button58))

button58.grid(row=8, column=1,sticky = S+N+E+W)


button59 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button59))

button59.grid(row=8, column=2,sticky = S+N+E+W)


button60 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button60))

button60.grid(row=8, column=3,sticky = S+N+E+W)


button61 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button61))

button61.grid(row=8, column=4,sticky = S+N+E+W)


button62 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button62))

button62.grid(row=8, column=5,sticky = S+N+E+W)


button63 = Button(tk,text=" ",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button63))

button63.grid(row=8, column=6,sticky = S+N+E+W)


button64 = Button(tk,text="O",font = ('Times 26 bold'), height = 2 , width = 4 , command=lambda:checker(button64))

button64.grid(row=8, column=7,sticky = S+N+E+W)


tk.mainloop()
