a = int(input("정수를 입력하시오: ")) #숫자를 입력할 변수 생성
for i in range(1,a+1): #행을 출력할 for문 생성
    for j in range(i): #열을 출력할 for문 생성
        print(j+1, end=' ')  #end를 사용하여 숫자를 이어서 출력할 수 있게끔 함
    print() #전체 출력 