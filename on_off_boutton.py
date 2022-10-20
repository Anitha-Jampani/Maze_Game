from tkinter import *
from Music_Of_On import *
def Music_but():
    root = Tk()
    # root.title('Toggle Button')
    root.geometry("200x150")

    def on():
        Music_2()
        tog.configure(file="Toggle.png")

        tog_button.configure(command=off)
        onoff.configure(text="On")


    def off():
        Music_Of()
        tog.configure(file="Toggle_off.png")
        tog_button.configure(command=on)
        onoff.configure(text="Off")

    tog = PhotoImage(file='Toggle_off.png')
    tog_button = Button(root,image=tog,border=0,command=on)
    tog_button.place(x=25,y=40)

    onoff = Label(root,text="Off",border=0,font=("bold",20))
    onoff.place(x=25,y=0)
    root.mainloop()