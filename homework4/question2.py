#짝수인지 홀수인지 판별하는 함수 생성
def checkEvenOdd(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"

#무한반복문 실행
while True:
    number = int(input("정수를 입력하시오: "))
    if number == 0000:
        print("실행종료") #만약 숫자 0000을 입력받았을 때 실행종료라고 출력 및 반복문 중단
        break
    else:
        print(f'{number} 입니다', checkEvenOdd(number)) #슷자를 입력받았을 때
                                                       # checkEvenOdd에서 짝홀 판별 후 출력
