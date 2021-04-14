item = ["First","Second", "Third"]

for val in enumerate(item):
    print(val)

for i,val in enumerate(item):
    print("{}번째 값은 {}입니다.".format(i,val))