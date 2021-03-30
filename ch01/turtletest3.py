import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor("yellow")
for i in range(1, 31):
    t.shape("turtle")
    t.forward(100 + i*2)
    t.left(90 + i)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)

turtle.mainloop()
turtle.bye()
