
# This is the RULES modules:
from Play_game import*
from tkinter import *
# create function help for rules:
def help():
    window = Tk()
    window.geometry("800x500")
    window.title("Help")

    # Background Image
    bg = PhotoImage(file="Help.png")
    label1 = Label(window,image=bg)
    label1.place(x=0, y=0)
    # create a func for starting the game:
    def fun():
        # destroy the window and show play func from play_game module:
        window.destroy()
        Play()
    image = PhotoImage(file="Play.png")

    but = Button(window,image=image,border=1,command=fun)
    but.place(x=300,y=400)

    #window.state("zoom")
    mainloop()
#help()