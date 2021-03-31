import turtle
import random

t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navyblue', 'purple'] #펜의 색 배열 생
t.shape("turtle")
turtle.bgcolor("black")

while True:
    r = random.randint(1, 100)
    m = random.randint(1, 100)
    t.color(colors[random.randrange(0, 6)])
    t.forward(m)
    t.left(r)
    t.forward(m)
    t.forward(r)
    print('r = {}, m = {}'.format(r,m))

turtle.mainloop()
turtle.bye()




