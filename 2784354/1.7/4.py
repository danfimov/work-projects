from random import randint

a = [randint(0, 4) for i in range(100)]
x = int(input())
print(a.count(x))
