def display(*args): #가변인자 '*args'를 함수에 입력한다.
    for i in range(args[1]): #args[1]은 20울 나타내므로 20만큼 반복한다.
        print(args[0]) #배열 args 원소 첫번째를 출력한다.

display("환영합니다.",20) #각각 args[0], args[1]을 뜻한다.
