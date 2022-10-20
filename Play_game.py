# MODULES
from Levels_calling import*
from tkinter.ttk import *
import time
import math
import random
from tkinter import *
# This module for just shows the
# create a play function:
def Play():
    #global close
    import turtle
    # create a window:
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("very_simple_level")
    screen = wn.getcanvas().winfo_toplevel()
    screen.state("zoom")
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
        # create func destroy for disappeared treasure:
        def Destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()
# create a class for security :
    class Security(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("police2.gif")
            self.penup()
            self.speed(0)
            self.gold = 25
            self.goto(x, y)
            # for moving we given random choice :
            self.direction = random.choice(["up", "down", "left", "right"])
        # create a func movements of security:
        def move(self):
            # move up when y-coro(24)
            if self.direction == "up":
                dx = 0
                dy = 24
            # move down when y-coro(-24)
            elif self.direction == "down":
                dx = 0
                dy = -24
            # move left when x-coro(-24)
            elif self.direction == "left":
                dx = -24
                dy = 0
                self.shape("police2.gif")
            # move right when x-
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
    level_0= [
        "xxxxxxxxxxxxxxxxxxxxxxxxx",
        "xT xxxxxx              Px",
        "x  xxxxxx   xxxxx   xxxxx",
        "x          xxxxxx   xxxxx",
        "x     xx  xxx         xxx",
        "xxxxxx xx  xxx         xx",
        "xxxxxx xx  xxxxx    xxxxx",
        "xxxxxx xx    xxxx   xxxxx",
        "x  xxx xx    xxxx   xxxxx",
        "x   xxx   xxxxxxxxxx   xx",
        "x        xxxxxxxxxxxxxx x",
        "x                xxxxxx x",
        "xxxxxxxxxxx      xxxxx  x",
        "xxxxxxxxxxx xxx  xxxxx  x",
        "xxxxxxxxxxx xxx  xxxxx  x",
        "xxxxxxxxxxxxxxx         x",
        "xxxT xxxxxxxxxx         x",
        "xxx                     x",
        "xxx       xxxxxxxxxxxxxxx",
        "xxxxxxxxx  xxxxxxxxxxxxxx",
        "xxx       xxxxxxxxxxxxxxx",
        "xxx xxxxx               x",
        "xx  xxxxx               x",
        "xx  xxxxx               x",
        "xT xxxxxxxxxxxxxx  xxxxxx",
        "xxxxxxxxxxxxxxxxxxxxxxxxx"
        ]

    # create a empty list of
    treasures = []
    Securities = []

    # Add maze to mazes list
    levels.append(level_0)

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
                    # calling x into graphic mood:
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
        # assign a treasure :
        for treasure in treasures:
            if Player.is_collision(treasure):
                Player.gold += treasure.gold
                print("Player Gold: {}".format(Player.gold))
                treasure.Destroy()
                treasures.remove(treasure)

                # after get 300 points player get won the game:
                # here assigning the points each coin how much it:
                if Player.gold == 300:
                    wn.bye()
                    Win = Tk()
                    #Win.geometry("700x400")
                    Win.state("zoom")
                    Win.title("You won")
                    won = PhotoImage(file="you won.png")
                    label1 = Label(Win, image=won)
                    label1.place(x=600, y=9.0)
                    Bye = Label(Win, text="""😎😎😎\nHey!!! you won the game...Byee
                    Meet you next Next...\nIf it is possible.. """, font=('Chiller Bold', 20))
                    Bye.place(x=100, y=100)
                    Next = PhotoImage(
                        file="next.png")
                    def exit():
                        Win.destroy()
                        LEVELS()
                    button = Button(Win, image=Next, borderwidth=0, command=exit,border=7)
                    button.place(y=240, x=240)

                    mainloop()

                    Win.state("zoom")
                # the time player die when security hits:
        for Security in Securities:
            if Player.is_collision(Security):
                time.sleep(0.5)
                pass
                #close()
                mainloop()

        # to update when player playing the game:
        wn.update()

#Play()