# MODULES
from tkinter.ttk import *
import time
import math
import random
from tkinter import *
# from menu import you_won

def Play():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("A MAZE GAME")
    wn.setup(650, 650)
    wn.tracer(0)

    images = ["coin.gif", "police2.gif", "player.gif", "brick.gif"]
    for image in images:
        turtle.register_shape(image)

    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("brick.gif")
            self.penup()
            self.speed(0)

    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("player.gif")
            self.penup()
            self.speed(0)
            self.gold = 0  # starting Score

        def go_up(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_down(self):
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_left(self):
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()

            self.shape("player.gif")

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_right(self):
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()

            self.shape("player.gif")

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def is_collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 5:  # 5 pixels
                return True
            else:
                return False

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
    LEVELS =[""]

    # Define first level
    level_0 =[

        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xT xxxxxx  xxxxxxx Pxxxxxxxxxxxxxxxx",
        "x  xxxxxx  xxxxxx   xxxx           x",
        "xS         xxxxxx   xxxx      xxxxxx",
        "x          xxx              xxxxxxxx",
        "xxxxxx x          xxxxxxxxxxxxxxxxxx",
        "xxxxxx xx    xxx        xxxxxxxxxxxx",
        "xxxxxx xx    xxxx            xxxxxxx",
        "x  xxx xx    xxxx S xxx         xxxx",
        "x  xxxxx  xxxxxxxxx   T  xxxxxxxxxxx",
        "xS             xxxxxxxx xxx   xxxxxx",
        "x                xxxxxx xxxx    xxxx",
        "xx     Sxxxxxx   xxxxx  xxxxx    xxx",
        "x             xxxxxxxxx  xxxxx xxxxx",
        "xxxxx   xxxxxxx  xxxxx  xxxxxx    xx",
        "xxxxxx        S       S          xxx",
        "xxx    xxxxxxx  xxxxxxxxxxxx    xxxx",
        "xxxS                    xxxxx   xxxx",
        "xxx    xx    xxxxx  xxx  xxx   xxxxx",
        "xxxxxxxxx  xxxxxxxx   xxxxxxxxxxxxxx",
        "xxx S      xxxxxxxxxxxxxx   xxxxxxxx",
        "xxx xxxxx              S      xxxxxx",
        "xx Sxxxxx               xxxx    xxxx",
        "xx  x xxxxxxxxxxxx  xxxxxx    xxxxxx",
        "x T    xxxxxxxxxx  xxxxxxxx     xxxx",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ]

    treasures = []
    Securities = []

    # Add maze to mazes list
    LEVELS.append(level_0)
    # print(len(LEVELS))


    # Create Level Setup Function
    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "x":
                    Pen.goto(screen_x, screen_y)
                    Pen.stamp()
                    walls.append((screen_x, screen_y))

                if character == "P":
                    Player.goto(screen_x, screen_y)
                if character == "T":
                    treasures.append(Treasure(screen_x, screen_y))
                if character == "S":
                    Securities.append(Security(screen_x, screen_y))

    Pen = Pen()
    Player = Player()
    walls = []

    setup_maze(LEVELS[1])


    # setup_maze(LEVELS['level_2'])
    # setup_maze(LEVELS['level_3'])

    turtle.listen()
    turtle.onkey(Player.go_left, "Left")
    turtle.onkey(Player.go_right, "Right")
    turtle.onkey(Player.go_up, "Up")
    turtle.onkey(Player.go_down, "Down")

    wn.tracer()

    for Security in Securities:
        turtle.ontimer(Security.move, t=250)

    while True:
        for treasure in treasures:
            if Player.is_collision(treasure):
                Player.gold += treasure.gold
                print("Player Gold: {}".format(Player.gold))
                treasure.Destroy()
                treasures.remove(treasure)
                if Player.gold == 300:
                    wn.bye()
                    Win = Tk()
                    Win.geometry("1000x500")
                    Win.title("You won")
                    won = PhotoImage(file="you won.png")
                    label1 = Label(Win, image=won)
                    label1.place(x=0, y=0)
                    Bye = Label(Win, text="Bye Bye Police !!!", font=('Chiller Bold', 20))
                    Bye.place(x=260, y=100)
                    play_again=Label(Win,text="""Hey! you did good job🥳🥳...\nyou complete zero_level.. 
                    but \n
                    Do want to play NEXT level....""",font=('Chiller Bold', 20))
                    play_again.place(x=260,y=150)

                #buttons

                    button1 =Button(Win, text="level_1", command=setup_maze(LEVELS['level_1']))
                    button1.grid(column=100, row=150)
                    Win.mainloop()

                    # mainloop()









        for Security in Securities:
            if Player.is_collision(Security):
                time.sleep(0.5)
                print("Player dies!")
                close()

        wn.update()

        def close():
            wn.bye()
            Result = Tk()
            Result.geometry("400x370")
            Result.title("Game over you lost !!")
            Result.config(bg="black")
            bgOver = PhotoImage(file="you lost.png")
            label2 = Label(Result, image=bgOver)
            label2.place(x=50, y=70)

            # buttons
            Exit = PhotoImage(
                file="Exit(1).png")
            button = Button(Result, image=Exit, borderwidth=0, command=Result.destroy)
            button.place(y=300, x=220)

            def Both_3():
                Result.destroy()
                Play()

            # Rerty
            restart = PhotoImage(
                file="Replay.png")
            button = Button(Result, image=restart, borderwidth=0, command=Both_3)
            button.place(y=300, x=30)
            mainloop()

Play()