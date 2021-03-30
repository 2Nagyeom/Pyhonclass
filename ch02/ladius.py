import turtle

t = turtle.Turtle()
t.shape("turtle")

t.color("blue")
t.pensize(3)
t.circle(30)
t.penup()
t.goto(50, 0)
t.pendown()

t.color("black")
t.pensize(3)
t.circle(30)
t.penup()
t.goto(100, 0)
t.pendown()

t.color("red")
t.pensize(3)
t.circle(30)
t.penup()
t.goto(80, -50)
t.pendown()

t.color("yellow")
t.pensize(3)
t.circle(30)
t.penup()
t.goto(30, -50)
t.pendown()

t.color("green")
t.pensize(3)
t.circle(30)
t.penup()
t.goto(40, -50)
t.pendown()

turtle.mainloop()
turtle.bye()
