from random import randint

a = [randint(0, 100) for i in range(10)]
print(*a)
a = [a[-1]] + a[0:len(a) - 1]
print(*a)
