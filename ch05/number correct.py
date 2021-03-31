import random

r = random.randint(1,100)
count = 0

print('1부터 100사이의 숫자를 맞추시오!')
while True:
    b = int(input('숫자입력 : '))
    if b < r:
        print('숫자가 너무 작아요')
        count += 1
    elif b > r:
        print('숫자가 너무 커요')
        count += 1
    elif b == r:
        print('숫자를 맞췄습니다!')
        break

print('시도횟수는 {}'.format(count))