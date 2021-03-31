import turtle #turtle 임포트
import random #난수생성 임포트

t = turtle.Turtle() #turtle 객체 생성
t.shape("turtle") #펜의 모양을 거북이로 결정

for i in range(1,10): #원을 총 10개 그림
    m = random.randint(1, 100) #원의 중심을 난수로 정할 변수 생성
    r = random.randint(1, 100) #원의 반지름을 난수로 정할 변수 생성
    t.pendown() #펜이동시 라인을 그림
    t.circle(r) #원을 반지름이 r만큼 그린다
    t.penup() #펜이동시 라인을 그리지 않음
    t.goto(r,r) #좌표가 (r,r)로 이동

turtle.mainloop()
turtle.bye() #터틀함수 종료