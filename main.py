
# imported modules :
from Rules import *
from tkinter import *
from Music_Of_On import *
from Play_game import Play

#create a window:
window = Tk()
# window size:
#window.geometry("750x500")
window.state("zoom")
#title:
window.title("THIS GAME DONE BY  SATISH, RAVI, RISHI  AND  Joseph...ENJOY THE GAME")
#Back gorund Image
bg =PhotoImage(file="BackGround.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

#Text to display:
text1 = Label(window,text="""W\nE\nL\nC\nO\nM\nE\n 
.TO.""",font=("Algerian",10),bg="light yellow" )
text1.place(x=180,y=290)
text1 = Label(window,text= "R\nO\nB\n\n T\nH\nE\n\n T\nR\nE\nA\nS\nU\nR\nE\n\n I\nF\n\n Y\nO\nU\n\n C\nA\nN\n\n..??...",font=('Algerian',16),bg="white")
text1.place(x=1310,y=1)
text2 = Label(window,text= "P\no\nl\ni\nc\ne\n\n H\nu\nn\nn\nt\ns\n\n M\nA\nZ\nE\nGame..!!",font=('Algerian',15),bg="black",fg="white")
text2.place(x=1210,y=70)





#Function to show game and close window
# calling the hele and play func from modules:
def Both():
    window.destroy()
    help()
    #Play()
# Button Exit:

Exit = PhotoImage(file="Exit.png")
button = Button(window, image=Exit, borderwidth=2,command=window.destroy)
button.place(y=645,x=90)

# Button Start:
Start = PhotoImage(file="Next_1.png")
button = Button(window, image=Start, borderwidth=2,command=Both,bg="white")
button.place(y=645,x=1150)

# define a music_button func for music:
def music_but():
    # music on:
    def on():
        Music_2()
        tog.configure(file="Toggle.png")

        tog_button.configure(command=off)
        onoff.configure(text="Music_On",bg="black",fg="white")

# music off:
    def off():
        Music_Of()
        tog.configure(file="Toggle_off.png")
        tog_button.configure(command=on)
        onoff.configure(text="Music_Off",bg="black",fg="white")



    tog = PhotoImage(file='Toggle_off.png')
    tog_button = Button(image=tog, border=0, command=on)
    tog_button.place(x=15, y=35)

    onoff = Label(text="Music_Off", border=0, font=("bold", 13))
    onoff.place(x=15, y=10)

# calling music func:
music_but()
mainloop()