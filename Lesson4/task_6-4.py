from itertools import count

for el in count(int(input('Введите начальное число: '))):
    print(el)
    if el > 10000:
        break

from itertools import cycle

c = 0
for el in cycle("1,2,3,4,5,6,7"):
    c = c + 1
    print(el)
    if c > 10:
        break
