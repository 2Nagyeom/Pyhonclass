# temp = [2,3,6,5,1]
#
# 얕은 복사
# value = temp
# print(temp)
# value[3] = 59
# print(temp)
#
#리스트 객체의 생성자, 객체를 생성하고 초기화하는 함수. 따라서 temp와 다르게 나옴
#깊은 복사
# values = list(temp)
# print(temp)
# print(values)
#
# temp[1] = 200
# print(temp)
# print(values)

meter_list = [3,7,9,10]

centi_meter_list = [100*i for i in meter_list if i%2 != 0]
print(centi_meter_list)