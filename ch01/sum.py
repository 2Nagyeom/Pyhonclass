# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print('sum = ' + str(sum))
# print(type('sum ='))
# print('type of sum=', type('sum ='))

# def sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum
#
# s = sum(100)
# print("sum = ", s)

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    return a // b

while True:
    print(' 종료 하려면 : 0 ')
    number1 = int(input(' 첫번째 수 : '))
    if number1 == 0:
        print(' Good - Bye! ')
        break
    oper = str(input(' +, -, *, / : '))
    number2 = int(input(' 두번째 수 : '))

    if oper == '+':
        res = plus(number1, number2)
    elif oper == '-':
        res = minus(number1, number2)
    elif oper == '*':
        res = multi(number1, number2)
    elif oper == '/':
        res = divi(number1, number2)
    else:
        print('{} 연산자 없음'.format(oper))
    print(' 결과 : {} {} {} = {}'.format(number1, oper, number2, res))

