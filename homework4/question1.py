import random  # 랜덤 임포트

# 횟수, 점수를 측정하는 변수 생성
count = 0
score = 0

# 다섯번 동안 실행할 반복문 생성
while count < 5:
    # x,y는 다섯번동안 난수를 생성함
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    answer = int(input('{0} + {1}'.format(x, y)))  # answer는 난수로 생성된 x,y값을 가져와 합을 입력받음
    # format 향식으로 만듦
    flag = (answer == (x + y))  # true인지 false인지 확인하는 변수 생성

    if flag == True:
        count += 1
        score += 10  # flag가 참이면 점수를 10점 증가
    else:
        count += 1
        score -= 10  # flag가 거짓이면 점수를 10점 감소

print("최종 점수: " + score + "횟수: " + count)  # 최종점수 및 횟수 출력