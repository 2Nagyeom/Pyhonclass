def calc(): #네개의 사칙연산을 실행할 함수를 생성한다.
    return a+b
    return a-b
    return a*b
    return a/b

#정수를 입력받을 변수를 생성한다.단 위의 매개변수랑 같게 한다.
a = int(input("첫 번째 정수를 입력하시오:"))
b = int(input("두 번째 정수를 입력하시오:"))
calc() #calc함수를 불러온다.
print('{}, {}, {}, {}이 반환되었습니다.'.format(a+b,a-b,a*b,a/b)) #위의 함수의 사칙연산을 모두 출력한다.