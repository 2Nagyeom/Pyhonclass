import turtle

t = turtle.Turtle()
t.shape("turtle")

#t.forward(100)
#t.left(90)
#t.forward(50)
#t.left(90)
#t.forward(100)
#t.left(90)
#t.forward(50)
#turtle.mainloop()
#turtle.bye()


t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(200)
t.circle(90,200)
t.right(130)
t.circle(90,200)
t.forward(200)

t.end_fill()

turtle.mainloop()
turtle.bye()
