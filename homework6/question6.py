import turtle #터틀 라이브러리를 임포트 한다.
t = turtle.Turtle() #터틀의 객체를 t라고 지정한다.
t.shape("turtle") #펜의 모양을 거북이로 지정한다.

def draw_square(size): #size크기로 그리는 함수를 생성한다.
    for i in range(50): #50번만큼 반복문을 실행한다.
        t.forward(size) #size만큼 나아간다
        t.left(90) #왼쪽으로 90만큼 이동한다
        size = size + 5 #바깥쪽으로 퍼지게끔 그려준다

draw_square(5) #간격이 5만큼 그려진다

turtle.mainloop()
turtle.bye() #터틀이 종료된다
