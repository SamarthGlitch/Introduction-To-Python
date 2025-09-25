import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
s.bgcolor("black")
t.speed('fastest')
t.hideturtle()
while True:
    for u in range(200):
        t.pencolor(colors[u%len(colors)])
        t.width(u/100 + 1)
        t.forward(u)
        t.left(59)
    t.right(239)
    for u in range(200, 0, -1):
        t.pencolor('black')
        t.width(u/100 + 7)
        t.forward(u)
        t.right(59)