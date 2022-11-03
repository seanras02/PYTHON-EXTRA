import turtle
t = turtle.Turtle()
turtle.speed(0)

turtle.color("green")
size = 1
for i in range(300):
    turtle.fd(size)
    turtle.rt(91)
    size += 1

turtle.done()