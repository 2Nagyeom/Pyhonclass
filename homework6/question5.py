#학점을 지정해줄 함수를 생성한다.
def getGrade(score):
    if score >= 90:
        print("성적은 A 입니다")
    elif score >= 80:
        print("성적은 B 입니다")
    elif score >= 70:
        print("성적은 C 입니다")
    elif score >= 60:
        print("성적은 D 입니다")
    elif score < 60:
        print("성적은 F 입니다")

score = int(input("점수를 입력하세요: ")) #성적을 입력받을 변수를 생성한다.
getGrade(score) #함수를 호출한다.
