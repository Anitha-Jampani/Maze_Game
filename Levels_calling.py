import tkinter
from tkinter import *
from level_1 import Level_1
from level_2 import Level_2
from level_3 import Level_3

# create a Levels func:
def LEVELS():
    # create win_window:
        win = Tk()
        win.geometry("400x250")
        win.title("Welcome to LEVELS :")
        def block_1():
            win.destroy()
            Level_1()
        # create button:
        butt_1=Button(win, text='Level_1', command=block_1,font=('Bodoni MT Black',20))
        butt_1.place(x=30,y=40)
        def block_2():
            win.destroy()
            Level_2()
        # create button:
        butt_2 =Button(win, text='Level_2',command=block_2,font=('Bodoni MT Black',20))
        butt_2.place(x=137,y=100)
        def block_3():
            win.destroy()
            Level_3()
        # create button:
        butt_3 =Button(win, text='Level_3',command=block_3,font=('Bodoni MT Black',20))
        butt_3.place(x=230,y=160)
        win.mainloop()


#LEVELS()