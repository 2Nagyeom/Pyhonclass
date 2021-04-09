import turtle #터틀을 임포트한다.
t = turtle.Turtle() #turtle객체를 t라고 지정한다.
t.shape("turtle") #그리는 펜의 모양을 거북이모양으로 한다.

def circle(radius): #원을 그리는 함수를 생성한다.

    for i in range(3):  #3번 반복
        t.circle(radius)    #반지름의 길이만큼 원을 그린다.
        t.pendown()         #펜을 내린다.
        t.penup()           #펜을 올린다.
        t.forward(90)       #90만큼 떨어진 후
        t.pendown()         #펜을 내린다.

circle(40);     #반지름이 90인 원을 그린다.


turtle.mainloop()
turtle.bye() #터틀을 실행종료한다.