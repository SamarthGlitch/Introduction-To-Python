import turtle

turtle.Screen().bgcolor("Black")

t=turtle.Turtle()

sc = turtle.Screen()
sc.setup(600, 300)

turtle.title("Welcome to turtle window")

#Rectangle
t.fillcolor("Red")
t.begin_fill()
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    i+=1
t.end_fill()

t.penup()
t.goto(200, 0)
t.pendown()

#Equilateral Triangle
t.fillcolor("Orange")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
    i+=1
t.end_fill()

t.penup()
t.goto(-100, 0)
t.pendown()

#Hexagon
t.fillcolor("Blue")
t.begin_fill()
for i in range(6):
    t.forward(50)
    t.left(60)
    i+=1
t.end_fill()

turtle.done()