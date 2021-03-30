n = int(input("정수를 입력하시오:"))
fact = n
#factorial 역순
for i in range(1, n-1):
    fact = fact * (n-i)
print(n,"!은",fact,"이다.")

#factorial
for i in range(1, 1+n):
   fact = fact * i
print(n, "!은", fact, "이다.")