# MODULES
from level_2 import *
from tkinter.ttk import *
import time
import math
import random
from tkinter import *

# create a play function:
# from Play_game import Play


def Level_1():
    global close
    import turtle
    # create a window:
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A MAZE GAME")
    screen_1=wn.getcanvas().winfo_toplevel()
    screen_1.state("zoom")
    wn.tracer(0)
    # upload a images:
    images = ["coin.gif", "police2.gif", "player.gif", "brick.gif"]
    for image in images:
        turtle.register_shape(image)


    # create point class:
    # for outer look of maze:
    # brick for walls of maze:
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
    # create a maze in 25x25 size:
    level_1= [
        "xxxxxxxxxxxxxxxxxxxxxxxxx",
        "xPxx         S         xx",
        "x xxxxxxxx  xxxx    xx xx",
        "x     Txxxx   T   xxxx xx",
        "xxxx xxxxxxxxxxxxxxxxx xx",
        "xxxx                   xx",
        "xxxx  xxxxxxxxxxxxx x xxx",
        "xxxx    xxxxxxxxxxx   xxx",
        "xxxxxxx   xxxxxxxxx  xxxx",
        "xxxxxxx             xxxxx",
        "xxxxxxxx xxxxxx xxxx xxxx",
        "xxxxx        S   Txx xxxx",
        "xxxx  xxxxxxxxxxxxxx xxxx",
        "xxxx           xxxxx xxxx",
        "xxxx  x xxxxxx    S  xxxx",
        "xxx     xxxxx Txxxxx xxxx",
        "xxx xxxxxxxxxxxxxxxx xxxx",
        "xxx xxxx        xxxx xxxx",
        "xxx xxxx xxxxxx      xxxx",
        "xxx       xxxxxxxxxxxxxxx",
        "xxxxxxxx               xx",
        "xxxxxxxxxxxxxxxxxxxxxx xx",
        "xx  T     S         xx xx",
        "xx xxxxxxxxxx      xxx xx",
        "xx                   T xx",
        "xxxxxxxxxxxxxxxxxxxxxxxxx"

    ]

    # create a empty list of
    treasures = []
    Securities = []

    # Add maze to mazes list
    levels.append(level_1)

    # Create Level Setup Function
    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                # define a variable char:
                character = level[y][x]
                screen_x = -288 + (x * 24)# each square of maze has 24 pixel size.
                screen_y = 288 - (y * 24)
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


                # after get 600 points player get won the game:
                # here assigning the points each coin how much it:
                if Player.gold == 600:
                    wn.bye()
                    Win_1 = Tk()
                    Win_1.state("zoom")
                    #Win.geometry("700x400")
                    Win_1.title("You won")
                    won = PhotoImage(file="you won.png")
                    label1 = Label(Win_1, image=won)
                    label1.place(x=600, y=9.0)
                    Bye = Label(Win_1,text="""😎😎😎\nBye Bye Police !!!\n
                    Meet you next level_2...\nIf it is possible.. """, font=('Chiller Bold', 20))
                    Bye.place(x=100, y=100)
                    Next = PhotoImage(
                        file="next.png")
                    def exit():
                        Win_1.destroy()
                        Level_2()

                    button = Button(Win_1, image=Next, borderwidth=0, command=exit, border=7)
                    button.place(y=270, x=240)

                # the time player die when security hits:
        for Security in Securities:
            if Player.is_collision(Security):
                time.sleep(0.5)
                pass
                close_1()
        # to update when player playing the game:
        wn.update()


        # for lose the game :
        # define a close:
        def close_1():
            wn.bye()
            Result_1 = Tk()
            Result_1.state("zoom")
            #Result.geometry("400x700")
            Result_1.title("Game over you lost !!")
            Result_1.config(bg="white")
            bgOver = PhotoImage(file="you lost.png")
            label2 = Label(Result_1, image=bgOver)

            label2.place(x=600, y=50)
            label3= Label(Result_1,text="""Hey!!!
             You lost the game....
            Do you want to play again...""",font=('Chiller Bold',20))
            label3.place(x=100,y=100)


            # buttons
            # for exit the game:
            Exit = PhotoImage(
                file="Exit(1).png")
            button = Button(Result_1, image=Exit, borderwidth=0, command=Result_1.destroy)
            button.place(y=300, x=220)

            def Both_1():
                Result_1.destroy()
                Level_1()

            # for replay the game:
            restart = PhotoImage(
                file="Replay.png")
            button = Button(Result_1, image=restart, borderwidth=0, command=Both_1)
            button.place(y=300, x=30)
            mainloop()
#Level_1()