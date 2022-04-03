import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.title("Russian Flag")
s.setup(width=800, height=600)

# Title on the window

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("The Russian Flag", align="center",font=("Arial", 24, "normal"))

t.up()
t.goto(-100, -100)
t.down()

# Red

t.color("red")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()

# Move for next color

t.up()
t.goto(100, -50)
t.down()

# Blue
t.color("blue")
t.begin_fill()
t.left(90)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.end_fill()

# Move for next color
t.up()

t.goto(100, 0)

t.down()

# White
t.color("white")
t.begin_fill()
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.end_fill()

while True:
    s.update()
