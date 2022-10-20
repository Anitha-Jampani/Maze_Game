# MODULES
#from Levels_calling import*
from tkinter.ttk import *
import time
import math
import random
from tkinter import *

# create a play function:
#from Play_game import Play


def Level_3():
    global close
    import turtle
    # create a window:
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A MAZE GAME")
    screen_3 = wn.getcanvas().winfo_toplevel()
    screen_3.state("zoom")
    wn.tracer(0)
    # upload a images:
    images = ["coin.gif", "police2.gif", "player.gif", "brick.gif"]
    for image in images:
        turtle.register_shape(image)

    # create point class:
    # for outer look of maze:
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("brick.gif")
            self.penup()
            self.speed(0)

    # create a player class:
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("player.gif")
            self.penup()
            self.speed(0)
            self.gold = 0  # starting Score

        # how player want to do:
        # this is for move up:
        def go_up(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24
            # here checks:
            # move on:
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        # move down:
        def go_down(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24
            # here checks:
            # move on:
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        # move left:
        def go_left(self):
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()

            self.shape("player.gif")
            # here checks:
            # move on:
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        # move right:
        def go_right(self):
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()

            self.shape("player.gif")
            # here checks:
            # move on:
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        # for disappeared of Treasure:
        def is_collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            # distance formula:
            # for disappeared of Treasure.
            distance = math.sqrt((a ** 2) + (b ** 2))


            # less 5 pixel disappeared:
            # one pixel = 0.26mm:
            if distance < 5:  # 5 pixels
                return True
            # otherwise is appeared:
            else:
                return False

    # create a final point class:
    class Treasure(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("coin.gif")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)

        def Destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    class Security(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("police2.gif")
            self.penup()
            self.speed(0)
            self.gold = 25
            self.goto(x, y)
            self.direction = random.choice(["up", "down", "left", "right"])

        def move(self):
            if self.direction == "up":
                dx = 0
                dy = 24
            elif self.direction == "down":
                dx = 0
                dy = -24
            elif self.direction == "left":
                dx = -24
                dy = 0
                self.shape("police2.gif")
            elif self.direction == "right":
                dx = 24
                dy = 0
                self.shape("police2.gif")
            else:
                dx = 0
                dy = 0

            if self.is_close(Player):
                if Player.xcor() > self.xcor():
                    self.direction = "right"
                elif Player.xcor() < self.xcor():
                    self.direction = "left"
                elif Player.ycor() < self.ycor():
                    self.direction = "down"
                elif Player.ycor() > self.ycor():
                    self.direction = "up"

            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", "down", "left", "right"])

            turtle.ontimer(self.move, t=random.randint(100, 300))

        def is_close(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 75:
                return True
            else:
                return False

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Create levels list
    levels = [""]

    # Define first level
    # create a maze in 27x55  size:
    level_3= [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xT xx  xx    xx xxxx    xx ST xxxx      x x   xx S  Txx",
        "x Sxx  x              x x  xx      x x  x xx  xx xxx  x",
        "x      x  x x x xxxxx   xx  x  xx xx xxxx xxx         x",
        "xxx    xxxx x x  S  x  xxx xx  xx x   x     xx x x   xx",
        "x  x x x    xx  x x x x       xxx x  xxxx x x  x xxx xx",
        "x    x x xx xxx x x xxx    xx xxx x  xx   x xxxx x    x",
        "x   xx   xxx    xxx    xxx xx S x x  xxxx xx     x x xx",
        "xxx xx x   xxxx   xxxx  xx xxx  x xx   xx x  xxx x x xx",
        "x   xxxxxx   xxxx   xxx     P   x  xxx x   xxxx    x  x",
        "xxx     xxxx xx xx x  S xx  x x   xxxx S   xx    xxxx x",
        "xx  xxx x    xx      xx xx xx x   xx  xxxx  xxx   S   x",
        "x  xxx x xxx xx xxx     xx    x   xxxT     xxxxx xx  xx",
        "x    x x   x x  x    xx    x  x     xxxx  xxx        xx",
        "xxx xx xxxxx xx xxx    xxx x xx x x    xx x   xx xx  xx",
        "xTx  x    xxTS    xx x   x x  xxx xxxx xx        xxxxxx",
        "xSx xx xx xxx x   xx xx  x x   xx x  x xx xxx xx     xx",
        "x      xx   x x  xxx xxx x x      x ST xx xxx xx     xx",
        "x   xx xxx  S      x   x   x   xx xx xxxx   x    x x xx",
        "xx xxx xxxxxx x xxxxxx xxx x  xxx xx    x x  xxx x x  x",
        "xx   x xx     x    xxx xx  x xxxx xx    x x  xxx x S xx",
        "xx   x xx xxxxx xx xxx x      xxx xx  x x xx   x xx T x",
        "x  xxx xx     x xx     x x xx  xx xxx x   S  x x xx x x",
        "xS       xxxx xSxx xxxxxxx xxx      x xxx x x     S x x",
        "xTxxxx x      xTxx   xxx   x    xx x    xx x  xx xx  Tx",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        ]

    # create a empty list of
    treasures = []
    Securities = []

    # Add maze to mazes list
    levels.append(level_3)

    # Create Level Setup Function
    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                # define a variable char:
                character = level[y][x]
                screen_x = -650 + (x * 24)
                screen_y = 310 - (y * 24)# each square of maze has 24 pixel size.

                # x means squares
                if character == "x":
                    Pen.goto(screen_x, screen_y)
                    #  in place x print square (define in point class )
                    Pen.stamp()
                    # add the walls x and y(coord) screens:
                    walls.append((screen_x, screen_y))
                # p means player:
                if character == "P":
                    Player.goto(screen_x, screen_y)
                    # T means treasure:
                if character == "T":
                    treasures.append(Treasure(screen_x, screen_y))
                if character == "S":
                    Securities.append(Security(screen_x, screen_y))

    # calling the point class by assign a variable pen:
    Pen = Pen()
    # calling the player class by assign a variable pen:
    Player = Player()
    # create empty list:
    walls = []
    # calling the maze function into levels:
    setup_maze(levels[1])
    # key call function:
    turtle.listen()
    turtle.onkey(Player.go_left, "Left")
    turtle.onkey(Player.go_right, "Right")
    turtle.onkey(Player.go_up, "Up")
    turtle.onkey(Player.go_down, "Down")
    wn.tracer()
# self movements of Security:
    for Security in Securities:
        turtle.ontimer(Security.move, t=250)
    # loop of the Treasure of treasure:
    while True:
        for treasure in treasures:
            if Player.is_collision(treasure):
                Player.gold += treasure.gold
                print("Player Gold: {}".format(Player.gold))
                treasure.Destroy()
                treasures.remove(treasure)
                # after get 1100 points player get won the game:
                # here assigning the points each coin how much it:
                if Player.gold == 1100:
                    wn.bye()
                    Win_3= Tk()
                    #Win.geometry("700x400")
                    Win_3.title("You won")
                    Win_3.state("zoom")
                    won = PhotoImage(file="you won.png")
                    label1 = Label(Win_3, image=won)
                    label1.place(x=600, y=9.0)
                    Bye = Label(Win_3, text="""😎😎😎\nBye Bye Police !!!\n
                    THE LEVELS ARE OVER...\nYou cann't catch me\n If is possible meet you next place.??. """, font=('Chiller Bold', 20))
                    Bye.place(x=100, y=100)


                    Exit = PhotoImage(
                        file="Exit(1).png")
                    button = Button(Win_3, image=Exit, borderwidth=0, command=Win_3.destroy)
                    button.place(y=300, x=220)









                #the time player die when security hits:
        for Security in Securities:
            if Player.is_collision(Security):
                time.sleep(0.5)
                pass
                close()
        # to update when player playing the game:
        wn.update()



        # for lose the game :
        # define a close:
        def close():
            wn.bye()
            Result = Tk()
            #Result.geometry("400x700")
            Result.title("Game over you lost !!")
            Result.config(bg="white")
            bgOver = PhotoImage(file="you lost.png")
            label2 = Label(Result, image=bgOver)
            label2.place(x=600, y=50)
            label3= Label(Result,text="""Hey!!!\n You lost the game....\n
            Do you want to play again...""",font=('Chiller Bold',20))
            label3.place(x=100,y=100)
            Result.state("zoom")



            # buttons
            # for exit the game:
            Exit = PhotoImage(
                file="Exit(1).png")
            button = Button(Result, image=Exit, borderwidth=0, command=Result.destroy)
            button.place(y=300, x=220)

            def Both_2():
                Result.destroy()
                Level_3()

            # for replay the game:
            restart = PhotoImage(
                file="Replay.png")
            button = Button(Result, image=restart, borderwidth=0, command=Both_2)
            button.place(y=300, x=30)
            mainloop()

#Level_3()