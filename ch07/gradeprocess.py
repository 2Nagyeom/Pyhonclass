STUDENTS = 5 #변하지 않는 수 즉 상수를 뜻하는 것은 대문자로 쓴다.
lst=[] #리스트 초기화
count=0

for i in range(STUDENTS): #for문을 다섯번 돌림
    value = int(input("성적을 입력하시오: "))
    lst.append(value) #

print("성적평균 = ",sum(lst)/len(lst))
print("최고점수 = ", max(lst))
print("최소점수 = ", min(lst))

for value in lst:
    if value >= 80:
        count += 1
print("80점 이상 = ",count)

#print("sorting", lst.sort()) #본체의 리스트를 정렬해서 변환
print("sorting", sorted(lst)) #정렬한 새로운 리스트를 반환