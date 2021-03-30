import turtle #turtle 불러오기

t = turtle.Turtle() #turtle 객체의 이름은 t라고 지정한다

t.penup() #펜을 들고 그림을 시작한다
t.goto(-100, -50) #(-100, -50)부터 그림을 그린다
t.pendown() #펜을 놓는다

radius = 50 #반지름이 50인 원을 그릴 것이다
t.color("red") #원의 색깔은 빨간색이다
t.circle(radius) #반지름만큼 원을 반시계 방향으로 그린다

t.color("blue") #원의 색깔은 파란색이다
t.forward(30) #30만큼 앞으로 움직인다
t.circle(radius) #반지름만큼 원을 반시계 방향으로 그린다

t.color("green") #원의 색깔은 초록색이다
t.forward(30) #30만큼 앞으로 움직인다
t.circle(radius) #반지름만큼 원을 반시계 방향으로 그린다

#밑에부터 반복
t.color("red")
t.forward(30)
t.circle(radius)

t.color("blue")
t.forward(30)
t.circle(radius)

t.color("green")
t.forward(30)
t.circle(radius)

t.color("red")
t.forward(30)
t.circle(radius)

t.color("blue")
t.forward(30)
t.circle(radius)

t.color("green")
t.forward(30)
t.circle(radius)

turtle.mainloop() #이벤트 루프를 시작한다
turtle.bye() #이벤트 루프를 끝낸다