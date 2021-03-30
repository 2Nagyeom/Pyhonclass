import turtle

c = ["red", "green", "blue", "yellow"]
# print(len(c))
# m = 0
# r = 30

c = input("색깔 : ")
m = input("이동거리 : ")
r = input("원의 반지름 : ")
t = turtle.Turtle()
t.shape("turtle")

while True:
 def myTurtleMake(tur, color, move, radius):
    global m
    tur.color(color)
    tur.circle(int(radius))
    m = int(m) + 50
    t.goto(m, 0)
    return tur

 myTurtleMake(t, c, m, r)

turtle.mainloop()
turtle.bye()