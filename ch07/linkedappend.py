fruits = []
fruits.append("grape")
fruits.append("apple")
fruits.append("banana")
fruits.append("lemon")

print(fruits)

#fruits.insert(2,"mango")
#fruits.insert(2,"banana")

for i in range(len(fruits)):
    print(fruits[i])

for i in range(-1,len(fruits)):
    print(fruits[i])

fruits.remove("banana")
fruits.pop(2)
print(fruits)