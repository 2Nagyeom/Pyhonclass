import turtle #터틀을 임포트한다

t = turtle.Turtle() # t를 터틀의 객체로 생성한다.
t.shape("turtle") #그림펜을 터틀 모양으로 한다.
t.width(3) #펜의 굵기를 3으로 한다.
t.shapesize(3,3) #거북이의 사이즈를 3배 확대한다.

# 필요한 변수를 입력받는다.
rad = int(input("각도입력 : "))
move = int(input("거리입력 : "))

#왼쪽으로 선을 긋는 함수를 생성한다.
def turtleMoveLeft(t, rad, move):
   t.left(rad) #rad만큼 왼쪽으로 각도를 튼다.
   t.forward(move) #move만큼 앞으로 나아간다.

#오른쪽으로 선을 긋는 함수를 생성한다.
def turtleMoveRight(t, rad, move):
    t.right(rad) #rad만큼 오른쪽으로 각도를 튼다.
    t.forward(move) #move만큼 앞으로 나아간다.

#무한반복문 실행
while True:
    command = input("명령을 입력하시오: ")
    if command == "l":
        turtleMoveLeft(t, rad, move) #l를 입력받았을 때 turtleMoveLeft 함수 실행
    if command == "r":
        turtleMoveRight(t, rad, move) #r를 입력받았을 때 turtleMoveRight 함수 실행
    if command == "q":
        break #q를 입력받았을 때 반복문 중단

turtle.mainloop()
turtle.bye() #터틀함수가 종료됌