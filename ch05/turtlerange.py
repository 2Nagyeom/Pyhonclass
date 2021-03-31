import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(200):
    t.circle(i)
    t.forward(2+i/4)


turtle.mainloop()
turtle.bye()