a = 80

print('1부터 100사이의 숫자를 맞추시오! :')

while True:
    b = int(input('숫자입력 : '))

    if b < a:
        print('숫자가 너무 작아요')
    elif b > a:
        print('숫자가 너무 커요')
    elif b == a:
        print('숫자를 맞췄습니다!')