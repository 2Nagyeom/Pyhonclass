def add(a,b):
    return a + b
# 더하기 함수 생성

def minus(a,b):
    return a - b
# 빼기 함수 생성

def multi(a,b):
    return a * b
# 곱하기 함수 생성

def divi(a,b):
    return a // b
# 나누기 함수 생성

while True: #무한 반복문
    a=input("a : ") #a에 값을 입력받음
    if a != 'q': #만약 a에 q값을 입력받지않으면
        b = input("b : ")
        op = input("+,-,*,//: ")
        #b와 op(사칙연산기호)를 입력받음
        if op == "+" : #만약 op값이 +라면
            res = add(int(a), int(b)) #더하기 함수 호출
        elif op == "-" :  #만약 op값이 -라면
            res = minus(int(a), int(b)) #빼기 함수 호출
        elif op == "*" :  #만약 op값이 *라면
            res = multi(int(a), int(b)) #곱하기 함수 호출
        elif op == "//": #만약 op값이 //라면
            res = divi(int(a), int(b)) #나누기 함수 호출
        else:
            print("input error") #만약 op값이 그 외의 값이 들어오면 출력

        print("result : ", res) #결과 출력
        print("-----------------")
    else:
        print("good bye") #만약 a에 q값을 입력받았으면 출력
