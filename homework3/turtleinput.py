import turtle #turtle 불러오기
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navyblue', 'purple'] #펜의 색 배열 생
r = input("원의 반지름 : ") #반지름값을 입력받음
if r == "q": #만약 r에 q를 입력받으면
   print('프로그램 종료') #프로그램 종료 출력
   exit(); #실행종료
n = input("원의 개수 : ")  # n값 입력받
f = input("이동거리 : ") #q를 입력받지 않았다면 f값 입력받음

t = turtle.Turtle() #turtle의 새로운 객체는 t라고 지정
t.shape("turtle") # 거북이 모양의 펜이 그려줌

def circleDraw(tur, radius, forward, number): #circeDraw라는 함수생성
    global n  # global로 지역변수에서 받은 값이 전역변수로 적용될 수 있다
    global f #global로 지역변수에서 받은 값이 전역변수로 적용될 수 있다
    x = 0 #초기 x좌표 설정
    for i in range(int(n)): #입력받은 원의 개수만큼 그려지는 반복문 생성
     tur.color(colors[random.randrange(0,6)]) #색깔을 랜덤으로 계속 바뀌게 설정
     f = int(f) + 10  # 이동거리는 f의 값을 정수값으로 적용하여 10을 더한 값으로 이루어짐
     tur.circle(int(radius)) #반지름의 값을 정수값으로 적용하여 원을 그림
     x += int(int(f) / int(n)) #x좌표가 총거리를 개수만큼 나눠서 1회당 움직이게 설정
     t.goto(x, 0) #(f,0)좌표로 바로 이동한다

    return tur #tur값을 반환함

circleDraw(t,r,f,n) #함수 호출

turtle.mainloop() #이벤트 루프 시작
turtle.bye() #이벤트 루프 끝냄