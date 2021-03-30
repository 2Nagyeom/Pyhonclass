#무게, 키를 입력받을 변수 생성
g = float(input("무게를 입력하시오 : "))
m = float(input("키를 입력하시오(단 m로 나타내시오) : "))

#bmi를 측정할 변수 생성
bmi = (g / (m**2))

#정상, 과체중, 비만을 나타낼 조건문 생성
if bmi > 20:
    if bmi < 24.9:
        print("당신의 BMI: ", bmi)
        print("정상입니다")  #만약 bmi수치가 20~24.9사이일 때 정상이라고 출력
elif bmi > 25:
    if bmi < 29.9:
        print("당신의 BMI: ", bmi)
        print("과체중입니다")   #만약 bmi수치가 25~29.9사이일 때 정상이라고 출력
elif bmi > 30:
    print("당신의 BMI: ", bmi)
    print("비만입니다")   #만약 bmi수치가 30이상일 때 정상이라고 출력
else:
    print("무게를 잘못입력하셨네요. 다시입력해주세요.") #무게를 잘못입력시 출력