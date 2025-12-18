import turtle

t = turtle.Turtle()

# t.circle(50)
# for i in range(4):
#     t.forward(50)
#     t.right(90)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
    # t.forward(100)

size = 120

t.speed(1)
t.pencolor("blue")
t.pensize("10")
t.penup()
t.goto(-size/2, size/2)
t.setheading(270)
t.forward(size)
t.penup()
t.goto(-size/2, size/2, size * 0.45)
t.pendown()
t.setheading(0)
t.forward(size * 0.45)