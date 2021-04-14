t = ['apple','bannana','melon']

print(t) #t를 팩킹
print(*t) #t를 언팩킹
print(t[1]) #banana 출력

#안의 원소 한개씩 출력
for i in range(3):
    print(t[i])

#안의 원소를 모두 3번씩 출력
for i in  range(3):
    print(*t)

#배열의 길이
print(len(t))

#역순으로 팩킹방식 출력하는 방법 [::1]
rev = t[::-1]
print(rev)

#원소 한개씩 거꾸로 출력하는 방법,함수사용
for i in reversed(t):
    print(i)

#원소 한개씩 거꾸로 출력하는 방법
for i in range(-1,2):
    print(t[i])