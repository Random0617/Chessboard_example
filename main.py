import turtle

t = turtle.Turtle()

t.pensize(2)
t.speed(0)

def draw_square():
    for i in range(4):
        t.forward(40)
        t.right(90)
    t.forward(40)

for i in range(8):
    t.penup()
    t.goto(0, 320 - i*40)
    t.pendown()

    for x in range(8):
        if (x + i) % 2 == 0:
            color = "black"
        else:
            color = "white"

        t.fillcolor(color)
        t.begin_fill()
        draw_square()
        t.end_fill()

t.hideturtle()
turtle.done()
