import random

count = 0

x = random.randint(1,100)
y = random.randint(1,100)

#answer = int(input(f"{x} + {y} = "))
answer = int(input('x{} + y{}').format(x, y))

flag = (answer == (x+y))
print(flag)
if flag == True:
    count += 1
else:
    count -= 1




# a = 'a'
# print(f'a is {a}')
#
# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
# print(f'a is {x}, {y}, {z}')
#
# name = 'Eunbi'
# family = 'Lee'
# print(f'My name is {name} {family},I am {family} {name}')


# print('I love {] for "{}!"'.format('Geeks', 'Geeks'))
# print('{0} and {1}'.format('Geeks', 'Portal'))
# print('{1} and {0}'.format('Geeks', 'Geeks'))