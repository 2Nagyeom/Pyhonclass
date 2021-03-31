mylist = [11,22,23,99,81,93,35] #mylist라는 배열에 배열값 넣기
sum = 0 #정수들의 합을 계산하는 변수 하나 생성함
for i in range(6): #배열원소의 갯수만큼 폴문 형성
    sum += mylist[i] #mylist의  i번째마다 sum이라는 변수에 더함


print('정수들의 합은 {}'.format(sum)) #폴맷함수로 정수의 합 출력

